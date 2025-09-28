from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from ipaddress import ip_network

from gufo.snmp import Aes128Key, DesKey, Md5Key, Sha1Key, SnmpError, SnmpVersion, User
from gufo.snmp.sync_client import SnmpSession
from icmplib import ping
from tcppinglib import tcpping

from netty_snmp.device_type.device_types import Platform, get_device_type
from netty_snmp.factory import consts
from netty_snmp.factory.manufactures.arista import AristaSnmpFactory
from netty_snmp.factory.manufactures.aruba import ArubaSnmpFactory
from netty_snmp.factory.manufactures.cisco import CiscoSnmpFactory
from netty_snmp.factory.manufactures.fortinet import FortinetSnmpFactory
from netty_snmp.factory.manufactures.h3c import H3cSnmpFactory
from netty_snmp.factory.manufactures.huawei import HuaweiSnmpFactory
from netty_snmp.factory.manufactures.juniper import JuniperSnmpFactory
from netty_snmp.factory.manufactures.paloalto import PaloAltoSnmpFactory
from netty_snmp.factory.manufactures.ruijie import RuijieSnmpFactory
from netty_snmp.factory.snmp_factory import SnmpFactory, SnmpV3Params, SnmpVersionError
from netty_snmp.types import (
    DeviceType,
    DiscoveryData,
    DiscoveryException,
    DiscoveryItem,
    DiscoveryResponse,
    DispatchItem,
    IPvANyNetwork,
)


def get_factory(platform: Platform) -> type[SnmpFactory]:
    factories = {
        Platform.Arista: AristaSnmpFactory,
        Platform.CiscoIOS: CiscoSnmpFactory,
        Platform.CiscoIOSXE: CiscoSnmpFactory,
        Platform.CiscoIOSXR: CiscoSnmpFactory,
        Platform.CiscoNexusOS: CiscoSnmpFactory,
        Platform.FortiNet: FortinetSnmpFactory,
        Platform.H3C: H3cSnmpFactory,
        Platform.Huawei: HuaweiSnmpFactory,
        Platform.HuaweiVRP: HuaweiSnmpFactory,
        Platform.HuaweiVRPV8: HuaweiSnmpFactory,
        Platform.Arista: AristaSnmpFactory,
        Platform.Aruba: ArubaSnmpFactory,
        Platform.RuiJie: RuijieSnmpFactory,
        Platform.Juniper: JuniperSnmpFactory,
        Platform.PaloAlto: PaloAltoSnmpFactory,
    }

    return factories.get(platform, SnmpFactory)


class DispatchSnmpFactory:
    def __init__(
        self,
        prefix: str,
        port: int = consts.SNMP_DEFAULT_PORT,
        version: SnmpVersion = SnmpVersion.v2c,
        community: str | None = consts.SNMP_DEFAULT_COMMUNITY,
        v3_params: SnmpV3Params | None = None,
        snmp_max_repetitions: int = consts.SNMP_MAX_REPETITIONS,
        max_workers: int = 16,
    ) -> None:
        self.prefix: IPvANyNetwork = self.str_to_prefix(prefix)
        self.port: int = port
        self.version: SnmpVersion = version
        self.community: str | None = community
        self.v3_params: SnmpV3Params | None = v3_params
        self.max_workers: int = max_workers
        self.exceptions: dict[str, list[DiscoveryException]] = defaultdict(list)
        self.snmp_max_repetitions: int = snmp_max_repetitions

    def str_to_prefix(self, prefix: str) -> IPvANyNetwork:
        if "/" not in prefix:
            if ":" in prefix or "::" in prefix:
                prefix += "/128"
            else:
                prefix += "/32"
        try:
            return ip_network(prefix)
        except ValueError as e:
            raise ValueError(f"Invalid ip prefix: {prefix}") from e

    def snmp_reachable(self, session: SnmpSession) -> bool:
        try:
            result = session.getnext("1.3.6.1.2.1.1.1.0")
        except ConnectionError:
            result = None
        return result is not None

    def get_auth_key(self) -> Sha1Key | Md5Key | None:
        if not self.v3_params:
            return None
        auth_protocol = self.v3_params.get("auth_protocol")
        auth_password = self.v3_params.get("auth_password")
        if auth_protocol == "md5":
            return Md5Key(bytes(auth_password, "utf-8"))
        if auth_protocol == "sha1":
            return Sha1Key(bytes(auth_password, "utf-8"))
        return None

    def get_priv_key(self) -> Aes128Key | DesKey | None:
        if not self.v3_params:
            return None
        privacy_protocol = self.v3_params.get("privacy_protocol")
        privacy_password = self.v3_params.get("privacy_password")
        if privacy_protocol == "aes128":
            return Aes128Key(bytes(privacy_password, "utf-8"))
        if privacy_protocol == "des":
            return DesKey(bytes(privacy_password, "utf-8"))
        return None

    def sys_object_id(self, session: SnmpSession) -> str | None:
        try:
            result = session.get(consts.sysObjectID.oid)
            if result and isinstance(result, str):
                return result
        except SnmpError as e:
            self.exceptions["sys_object_id"].append(DiscoveryException(item="sys_object_id", exception=str(e)))
        return None

    def device_type(self, sys_object_id: str) -> "DeviceType":
        device_type = get_device_type(sys_object_id)
        if not device_type:
            return DeviceType(
                platform=consts.UNKNOWN_PLATFORM,
                manufacturer=consts.UNKNOWN_MANUFACTURER,
                model=consts.UNKNOWN_MODEL,
            )
        return device_type

    def get_snmp_session(self, ip: str) -> SnmpSession:
        if self.version == SnmpVersion.v2c and self.community:
            return SnmpSession(
                addr=ip,
                port=self.port,
                community=self.community,
                version=SnmpVersion.v2c,
            )
        if self.version == SnmpVersion.v3 and self.v3_params:
            return SnmpSession(
                addr=ip,
                port=self.port,
                version=SnmpVersion.v3,
                user=User(
                    name=self.v3_params["security_username"],
                    auth_key=self.get_auth_key(),
                    priv_key=self.get_priv_key(),
                ),
            )
        raise SnmpVersionError(f"Unsupported SNMP version: {self.version}")

    def _dispatch(self, ip_address: str, discovery_items: list[DiscoveryItem] | None = None) -> DiscoveryResponse:
        snmp_session = self.get_snmp_session(ip_address)
        icmp_reachable = self._is_icmp_reachable(ip_address)
        ssh_reachable = self._is_ssh_reachable(ip_address)
        snmp_reachable = self.snmp_reachable(snmp_session)

        discovery_response = DiscoveryResponse(
            ip=ip_address,
            data=None,
            snmp_reachable=snmp_reachable,
            icmp_reachable=icmp_reachable,
            ssh_reachable=ssh_reachable,
            sys_object_id=None,
            exceptions=None,
        )

        if not snmp_reachable:
            return discovery_response

        try:
            sys_object_id = self.sys_object_id(snmp_session)
        except SnmpError as e:
            self._handle_snmp_error(ip_address, "sys_object_id", e)
            return discovery_response

        if not sys_object_id:
            return discovery_response

        device_type = self.device_type(sys_object_id)
        factory = get_factory(Platform(device_type["platform"]))
        device_data = factory(
            ip=ip_address,
            port=self.port,
            version=self.version,
            community=self.community,
            v3_params=self.v3_params,
            snmp_max_repetitions=self.snmp_max_repetitions,
        ).discovery(discovery_items)

        discovery_data = DiscoveryData(
            device_type=device_type["model"],
            manufacturer=device_type["manufacturer"],
            platform=device_type["platform"],
            **device_data,
        )

        discovery_response["data"] = discovery_data
        discovery_response["sys_object_id"] = sys_object_id

        return discovery_response

    @staticmethod
    def _is_icmp_reachable(ip_address: str) -> bool:
        return ping(ip_address, count=2, interval=1, timeout=1, privileged=False).is_alive  # type: ignore  # noqa: PGH003

    @staticmethod
    def _is_ssh_reachable(ip_address: str) -> bool:
        return tcpping(ip_address, port=22, timeout=1, count=2, interval=0.2).is_alive

    def _handle_snmp_error(self, ip_address: str, item: DispatchItem, exception: SnmpError) -> None:
        self.exceptions.setdefault(ip_address, []).append(DiscoveryException(item=item, exception=str(exception)))
        self.exceptions[ip_address].append(DiscoveryException(item=item, exception=str(exception)))

    def dispatch(self, discovery_items: list[DiscoveryItem] | None = None) -> list[DiscoveryResponse]:
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = [executor.submit(self._dispatch, str(ip), discovery_items) for ip in self.prefix.hosts()]
            return [future.result() for future in as_completed(futures)]
