from concurrent.futures import ThreadPoolExecutor, as_completed
from ipaddress import ip_network

from ezsnmp import EzSNMPError, Session
from icmplib import ping
from netty._types import DeviceType, DiscoveryData, DiscoveryResponse
from netty.device_type.device_types import Platform, get_device_type
from netty.factory import consts
from netty.factory.manufactures.arista import AristaSnmpFactory
from netty.factory.manufactures.aruba import ArubaSnmpFactory
from netty.factory.manufactures.cisco import CiscoSnmpFactory
from netty.factory.manufactures.fortinet import FortinetSnmpFactory
from netty.factory.manufactures.h3c import H3cSnmpFactory
from netty.factory.manufactures.huawei import HuaweiSnmpFactory
from netty.factory.manufactures.juniper import JuniperSnmpFactory
from netty.factory.manufactures.paloalto import PaloaltoSnmpFactory
from netty.factory.manufactures.ruijie import RuijieSnmpFactory
from netty.factory.snmp_factory import SnmpFactory, SnmpV3Params
from tcppinglib import tcpping


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
        Platform.PaloAlto: PaloaltoSnmpFactory,
    }

    return factories[platform]


class DispatchSnmpFactory:
    def __init__(
        self,
        prefix: str,
        port: int = consts.SNMP_DEFAULT_PORT,
        version: consts.SnmpVersion = consts.SnmpVersion.v2c,
        community: str | None = consts.SNMP_DEFAULT_COMMUNITY,
        v3_params: SnmpV3Params | None = None,
        max_workers: int = 16,
    ) -> None:
        self.prefix = ip_network(prefix)
        self.port = port
        self.version = version
        self.community = community
        self.v3_params = v3_params
        self.max_workers = max_workers

    def snmp_reachable(self, session: Session) -> bool:
        try:
            result = session.get_next(".1").value
        except EzSNMPError:
            result = None
        return result is not None

    def sys_object_id(self, session: Session) -> str:
        if not self.sys_object_id:
            iso_id = ".1.3.6.1.4.1."
            self.sys_object_id = (session.get(consts.sysObjectID.oid).value).split(iso_id)[1]
        return self.sys_object_id

    def device_type(self, sys_object_id: str) -> "DeviceType":
        device_type = get_device_type(sys_object_id)
        if not device_type:
            return DeviceType(
                platform=consts.UNKNOWN_PLATFORM,
                manufacturer=consts.UNKNOWN_MANUFACTURER,
                model=consts.UNKNOWN_MODEL,
            )
        return device_type

    def _dispatch(self, ip: str) -> DiscoveryResponse:
        if self.version == consts.SnmpVersion.v2c:
            session = Session(
                hostname=ip, remote_port=self.port, community=self.community, version=consts.SnmpVersion.v2c
            )
        if self.version == consts.SnmpVersion.v3:
            session = Session(hostname=ip, remote_port=self.port, version=consts.SnmpVersion.v3, **self.v3_params)

        icmp_reachable = ping(ip, count=2, interval=0.2, timeout=1, privileged=False).is_alive
        ssh_reachable = tcpping(ip, port=22, timeout=1, count=2, interval=0.2).is_alive
        snmp_reachable = self.snmp_reachable(session)
        discovery_response = DiscoveryResponse(
            ip=ip,
            data=None,
            snmp_reachable=snmp_reachable,
            icmp_reachable=icmp_reachable,
            ssh_reachable=ssh_reachable,
            sysObjectID=None,
        )
        if not snmp_reachable:
            return discovery_response
        _sys_object_id = self.sys_object_id(session)
        device_type = self.device_type(sys_object_id=_sys_object_id)
        factory = get_factory(device_type["platform"])
        device_data = factory(ip, self.port, self.version, self.community, self.v3_params).discovery()
        discovery_data = DiscoveryData(
            device_type=device_type["model"],
            manufacturer=device_type["manufacturer"],
            platform=device_type["platform"],
            **device_data,
        )
        discovery_response["data"] = discovery_data
        return discovery_response

    def dispatch(self) -> list[DiscoveryResponse]:
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = [executor.submit(self._dispatch, ip) for ip in self.prefix.hosts()]
            return [future.result() for future in as_completed(futures)]
