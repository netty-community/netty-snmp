from collections import defaultdict
from ipaddress import ip_interface
from typing import Any, Literal, TypedDict

from ezsnmp import EzSNMPError, Session

from netty_snmp._types import DiscoveryException, DiscoveryItem, Entity, Interface, LldpNeighbor, SnmpDiscoveryData
from netty_snmp.factory import consts
from netty_snmp.utils import mac_address_validator


class SnmpVersionError(Exception):
    pass


class SnmpConnectionError(Exception):
    pass


class SnmpV3Params(TypedDict):
    context_engine_id: str
    security_username: str
    security_level: Literal["no_auth_or_privacy", "auth_without_privacy", "auth_with_privacy"]
    auth_protocol: Literal["md5", "sha1", "sha224", "sha256", "sha384", "sha512"]
    auth_password: str
    privacy_protocol: Literal["des", "aes128", "aes192", "aes256"]
    privacy_password: str


class SnmpFactory:
    def __init__(
        self,
        ip: str,
        port: int = consts.SNMP_DEFAULT_PORT,
        version: consts.SnmpVersion = consts.SnmpVersion.v2c,
        community: str | None = consts.SNMP_DEFAULT_COMMUNITY,
        v3_params: SnmpV3Params | None = None,
        snmp_max_repetitions: int = consts.SNMP_MAX_REPETITIONS,
    ) -> None:
        """
        :param ip: network device ip, ipv4 or ipv6 address
        :param port: network device snmp agent port, default: 161
        :param version: SNMP version, default: v2c
        :param community: SNMP v2 community, default: public
        :param v3_params: SNMP v3 params
        :param snmp_max_repetitions: SNMP max repetitions for bulkwalk
        """
        self.ip = ip
        self.port = port
        self.version = version
        self.community = community
        self.v3_params = v3_params
        self.session = self._session()
        self.exceptions: list[DiscoveryException] = []
        self.snmp_max_repetitions = snmp_max_repetitions

    def _session(self) -> Session:
        """create session for snmp query"""
        if self.version == consts.SnmpVersion.v2c and self.community:
            return Session(
                hostname=self.ip,
                remote_port=self.port,
                community=self.community,
                version=consts.SnmpVersion.v2c.value,
                use_long_names=False,
                use_enums=False,
                use_sprint_value=True,
            )
        if self.version == consts.SnmpVersion.v3 and self.v3_params:
            return Session(
                hostname=self.ip,
                remote_port=self.port,
                version=consts.SnmpVersion.v3.value,
                **self.v3_params,
                use_long_names=False,
                use_enums=False,
                use_sprint_value=True,
            )
        raise SnmpVersionError(f"Unsupported SNMP version: {self.version}")

    @property
    def hostname(self) -> str | None:
        """
        collect network device hostname
        """
        try:
            return self.session.get(consts.sysName.oid).value
        except EzSNMPError as e:
            self.exceptions.append(DiscoveryException(item="hostname", exception=str(e)))
            return None

    @property
    def sys_descr(self) -> str | None:
        """
        collect network device system description, include model/version/patch information
        without structured data format
        """
        try:
            return self.session.get(consts.sysDescr.oid).value
        except EzSNMPError as e:
            self.exceptions.append(DiscoveryException(item="sys_descr", exception=str(e)))
            return None

    @property
    def uptime(self) -> str | None:
        """
        collect network device uptime`
        """
        try:
            return self.session.get(consts.sysUpTime.oid).value
        except EzSNMPError as e:
            self.exceptions.append(DiscoveryException(item="uptime", exception=str(e)))
            return None

    @property
    def chassis_id(self) -> str | None:
        """
        collect chassis id via `LLDP-MIB`.
        Special configuration for Huawei: snmp should include iso view and mib-2
        """
        try:
            return mac_address_validator(self.session.get(consts.lldpLocChassisId.oid).value)
        except EzSNMPError as e:
            self.exceptions.append(DiscoveryException(item="chassis_id", exception=str(e)))
            return None

    @property
    def if_port_mode(self) -> dict[str, str]:
        """
        collect interface port mode, need implement in manufacturer factory
        """
        return {}

    @property
    def interfaces(self) -> list[Interface]:
        """
        collect interfaces via `IF-MIB`, if filtering by the items, implement it the manufacturer factory
        """
        try:
            if_index = self.session.bulkwalk(consts.ifIndex.oid, max_repetitions=self.snmp_max_repetitions)
            if_name = self.session.bulkwalk(consts.ifDescr.oid, max_repetitions=self.snmp_max_repetitions)
            if_descr = self.session.bulkwalk(consts.ifAlias.oid, max_repetitions=self.snmp_max_repetitions)
            if_mtu = self.session.bulkwalk(consts.ifMtu.oid, max_repetitions=self.snmp_max_repetitions)
            if_speed = self.session.bulkwalk(consts.ifSpeed.oid, max_repetitions=self.snmp_max_repetitions)
            if_high_speed = self.session.bulkwalk(consts.ifHighSpeed.oid, max_repetitions=self.snmp_max_repetitions)
            if_type = self.session.bulkwalk(consts.ifType.oid, max_repetitions=self.snmp_max_repetitions)
            if_phys_addr = self.session.bulkwalk(consts.ifPhysAddr.oid, max_repetitions=self.snmp_max_repetitions)
            if_admin = self.session.bulkwalk(consts.ifAdminStatus.oid, max_repetitions=self.snmp_max_repetitions)
            if_oper = self.session.bulkwalk(consts.ifOperStatus.oid, max_repetitions=self.snmp_max_repetitions)
            if_addr_index = self.session.bulkwalk(consts.ifAdEntIfIndex.oid, max_repetitions=self.snmp_max_repetitions)
            if_addr_netmask = self.session.bulkwalk(
                consts.ifAdEntNetMask.oid, max_repetitions=self.snmp_max_repetitions
            )
            if_port_mode = self.if_port_mode
        except EzSNMPError as e:
            self.exceptions.append(DiscoveryException(item="interfaces", exception=str(e)))
            return []
        index_if_index = {x.oid_index: x.value for x in if_index}
        index_if_name = {x.oid_index: x.value for x in if_name}
        index_if_descr = {x.oid_index: x.value for x in if_descr}
        index_if_mtu = {x.oid_index: x.value for x in if_mtu}
        index_if_speed = {x.oid_index: x.value for x in if_speed}
        index_if_high_speed = {x.oid_index: x.value for x in if_high_speed}
        index_if_type = {x.oid_index: x.value for x in if_type}
        index_if_phys_addr = {x.oid_index: x.value for x in if_phys_addr}
        index_if_admin = {x.oid_index: x.value for x in if_admin}
        index_if_oper = {x.oid_index: x.value for x in if_oper}
        index_if_addr_index = defaultdict(list)
        index_if_addr_netmask = {x.oid_index: x.value for x in if_addr_netmask}
        for x in if_addr_index:
            netmask = index_if_addr_netmask[x.oid_index]
            index_if_addr_index[x.value].append(ip_interface(f"{x.oid_index}/{netmask}"))
        return [
            Interface(
                if_index=int(x),
                if_name=index_if_name.get(x),
                if_descr=index_if_descr.get(x),
                if_mtu=int(index_if_mtu.get(x)),
                if_speed=int(index_if_speed.get(x)),
                if_high_speed=int(index_if_high_speed.get(x)),
                if_type=index_if_type.get(x),
                if_phys_address=mac_address_validator(index_if_phys_addr.get(x)),
                if_admin_status=index_if_admin.get(x),
                if_oper_status=index_if_oper.get(x),
                if_ip_address=index_if_addr_index.get(x),
                if_port_mode=if_port_mode.get(x, consts.UNKNOWN_PORT_MODE),
            )
            for x in index_if_index
            if x is not None
        ]

    @property
    def lldp_neighbors(self) -> list[LldpNeighbor]:
        """
        collect lldp neighbors via `LLDP-MIB`
        Special configuration for network devices: include iso mib-2 view in snmp configuration
        lldpRemChassisID: snmp_index value the last of 2 is local portID's index(last of 1)
        """
        try:
            local_chassis_id = self.chassis_id
            local_if_name = self.session.bulkwalk(consts.lldpLoPortId.oid, max_repetitions=self.snmp_max_repetitions)
            local_if_descr = self.session.bulkwalk(
                consts.lldpLocPortDesc.oid, max_repetitions=self.snmp_max_repetitions
            )
            remote_chassis_id = self.session.bulkwalk(
                consts.lldpRemChassisId.oid, max_repetitions=self.snmp_max_repetitions
            )
            remote_hostname = self.session.bulkwalk(
                consts.lldpRemSysName.oid, max_repetitions=self.snmp_max_repetitions
            )
            remote_if_name = self.session.bulkwalk(consts.lldpRemPortId.oid, max_repetitions=self.snmp_max_repetitions)
            remote_if_descr = self.session.bulkwalk(
                consts.lldpRemPortDesc.oid, max_repetitions=self.snmp_max_repetitions
            )
        except EzSNMPError as e:
            self.exceptions.append(DiscoveryException(item="lldp_neighbors", exception=str(e)))
            return []
        index_local_if_name = {x.oid.split(".")[-1]: x.value for x in local_if_name}
        index_local_if_descr = {x.oid.split(".")[-1]: x.value for x in local_if_descr}
        index_remote_chassis_id = {x.oid.split(".")[-2]: mac_address_validator(x.value) for x in remote_chassis_id}
        index_remote_hostname = {x.oid.split(".")[-2]: x.value for x in remote_hostname}
        index_remote_if_name = {x.oid.split(".")[-2]: x.value for x in remote_if_name}
        index_remote_if_descr = {x.oid.split(".")[-2]: x.value for x in remote_if_descr}
        return [
            LldpNeighbor(
                local_chassis_id=local_chassis_id,
                local_hostname=self.hostname,
                local_if_name=index_local_if_name.get(x),
                local_if_descr=index_local_if_descr.get(x),
                remote_chassis_id=index_remote_chassis_id.get(x),
                remote_hostname_id=index_remote_hostname.get(x),
                remote_if_name=index_remote_if_name.get(x),
                remote_if_descr=index_remote_if_descr.get(x),
            )
            for x in index_remote_chassis_id
            if x is not None
        ]

    @property
    def entities(self) -> list[Entity]:
        """
        collect entities via `ENTITY-MIB`
        basically: chassis(3) should be the main module of device.
        but fuck huawei (3 or 9(module) for different product lines) because its unstandard implementation
        see value mapping in `consts.py`: ENTITY_PHYSICAL_CLASS_MAPPING
        so it may won't work for huawei in default factory.
        """
        try:
            ent_phy_class = self.session.bulkwalk(consts.entPhysicalClass.oid)
            index_ent_phy_class = {x.oid.split(".")[-1]: x.value for x in ent_phy_class if int(x.value) == 3}  # noqa: PLR2004
            oids = list(index_ent_phy_class.keys())
            if not oids:
                return []
            ent_phy_descr = self.session.get([consts.entPhysicalDescr.oid + "." + x for x in oids])
            ent_phy_name = self.session.get([consts.entPhysicalName.oid + "." + x for x in oids])
            ent_phy_software = self.session.get([consts.entPhysicalSoftwareRev.oid + "." + x for x in oids])
            ent_phy_serial = self.session.get([consts.entPhysicalSerialNum.oid + "." + x for x in oids])
        except EzSNMPError as e:
            self.exceptions.append(DiscoveryException(item="entities", exception=str(e)))
            return []
        index_ent_phy_descr = {x.oid.split(".")[-1]: x.value for x in ent_phy_descr}
        index_ent_phy_name = {x.oid.split(".")[-1]: x.value for x in ent_phy_name}
        index_ent_phy_software = {x.oid.split(".")[-1]: x.value for x in ent_phy_software}
        index_ent_phy_serial = {x.oid.split(".")[-1]: x.value for x in ent_phy_serial}
        return [
            Entity(
                ent_physical_class=int(x),
                ent_physical_descr=index_ent_phy_descr.get(x),
                ent_physical_name=index_ent_phy_name.get(x),
                ent_physical_software_rev=index_ent_phy_software.get(x),
                ent_physical_serial_num=index_ent_phy_serial.get(x),
            )
            for x in index_ent_phy_class
            if x is not None
        ]

    @property
    def stack(self) -> Any: ...

    @property
    def vlans(self) -> Any: ...

    @property
    def prefixes(self) -> Any: ...

    @property
    def routes(self) -> Any: ...

    @property
    def mac_address_table(self) -> dict[int, list[str]]:
        """collect mac address table via `DOT1D-MIB`
        if port index is `0` which indicated that the port number has not been learned, but that the
        bridge does have some forwarding/filtering information about this mac address.

        Returns:
            dict[int, list[str]]: dict[if_index, list[mac_address]]
        """
        try:
            dot1d_base_port_index = self.session.bulkwalk(
                oids=consts.dot1dBasePortIfIndex.oid, max_repetitions=self.snmp_max_repetitions
            )
            dot1d_tp_fdb_address = self.session.bulkwalk(
                oids=consts.dot1dTpFdbAddress.oid, max_repetitions=self.snmp_max_repetitions
            )
            dot1d_tp_fdb_port = self.session.bulkwalk(
                oids=consts.dot1dTpFdbPort.oid, max_repetitions=self.snmp_max_repetitions
            )
        except EzSNMPError as e:
            self.exceptions.append(DiscoveryException(item="mac_address_table", exception=str(e)))
            return {}
        index_dot1d_base_port_index = {x.oid.split(".")[-1]: x.value for x in dot1d_base_port_index}
        index_dot1d_base_port_index["0"] = "0"
        index_dot1d_tp_fdb_address = {}
        for x in dot1d_tp_fdb_address:
            index = ".".join(x.oid.split(".")[-6:])
            mac_address = mac_address_validator(x.value, True)
            if not mac_address:
                continue
            index_dot1d_tp_fdb_address[index] = mac_address
        index_dot1d_tp_fdb_port = {".".join(x.oid.split(".")[-6:]): x.value for x in dot1d_tp_fdb_port}
        results = defaultdict(list)
        for port_index, mac_address in index_dot1d_tp_fdb_address.items():
            results[int(index_dot1d_base_port_index[index_dot1d_tp_fdb_port[port_index]])].append(mac_address)
        return results

    @property
    def arp_table(self) -> dict[str, str]:
        try:
            arp_table = self.session.bulkwalk(
                oids=consts.ipNetToMediaPhysAddress.oid, max_repetitions=self.snmp_max_repetitions
            )
        except EzSNMPError as e:
            self.exceptions.append(DiscoveryException(item="arp_table", exception=str(e)))
            return {}
        return {".".join(x.oid_index.split(".")[-4:]): mac_address_validator(x.value, True) for x in arp_table}

    def discovery(self, items: list[DiscoveryItem] | None = None) -> SnmpDiscoveryData:
        """
        discovery network basic information via SNMP
        params:
            items: list of `DiscoveryItem` to collect, if not specified, all items will be collected
        returns:
            SnmpDiscoveryData: all collected items
        """
        if not items:
            return SnmpDiscoveryData(
                hostname=self.hostname,
                sys_descr=self.sys_descr,
                uptime=self.uptime,
                chassis_id=self.chassis_id,
                interfaces=self.interfaces,
                lldp_neighbors=self.lldp_neighbors,
                stack=self.stack,
                vlans=self.vlans,
                prefixes=self.prefixes,
                mac_address_table=self.mac_address_table,
                arp_table=self.arp_table,
                routes=self.routes,
                exceptions=self.exceptions,
            )
        return {x: getattr(self, x) for x in items}  # type: ignore  # noqa: PGH003
