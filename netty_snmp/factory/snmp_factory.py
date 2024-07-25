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
    security_level: Literal["noAuthNoPriv", "authNoPriv", "authPriv"]
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
        model: str | None = None,
    ) -> None:
        """
        :param ip: network device ip, ipv4 or ipv6 address
        :param port: network device snmp agent port, default: 161
        :param version: SNMP version, default: v2c
        :param community: SNMP v2 community, default: public
        :param v3_params: SNMP v3 params
        :param model: network device model
        """
        self.ip = ip
        self.port = port
        self.version = version
        self.community = community
        self.v3_params = v3_params
        self.model = model
        self.session = self._session()
        self.exceptions: list[DiscoveryException] = []

    def _session(self) -> Session:
        """create session for snmp query"""
        if self.version == consts.SnmpVersion.v2c and self.community:
            return Session(
                hostname=self.ip,
                remote_port=self.port,
                community=self.community,
                version=consts.SnmpVersion.v2c,
                use_long_names=False,
                use_enums=False,
                use_sprint_value=True,
            )
        if self.version == consts.SnmpVersion.v3 and self.v3_params:
            return Session(
                hostname=self.ip,
                remote_port=self.port,
                version=consts.SnmpVersion.v3,
                **self.v3_params,
                use_long_names=False,
                use_enums=False,
                use_sprint_value=True,
            )
        raise SnmpVersionError(f"Unsupported SNMP version: {self.version}")

    @property
    def hostname(self) -> str:
        """
        collect network device hostname
        """
        try:
            return self.session.get(consts.sysName.oid).value
        except EzSNMPError as e:
            self.exceptions.append(DiscoveryException(item="hostname", exception=str(e)))
            return ""

    @property
    def sys_descr(self) -> str:
        """
        collect network device system description, include model/version/patch information
        without structured dataformat
        """
        try:
            return self.session.get(consts.sysDescr.oid).value
        except EzSNMPError as e:
            self.exceptions.append(DiscoveryException(item="sys_descr", exception=str(e)))
            return ""

    @property
    def uptime(self) -> str:
        """
        collect network device uptime`
        """
        try:
            return self.session.get(consts.sysUpTime.oid).value
        except EzSNMPError as e:
            self.exceptions.append(DiscoveryException(item="uptime", exception=str(e)))
            return ""

    @property
    def chassis_id(self) -> Any:
        """
        collect chasis id via `LLDP-MIB`.
        Special configuration for Huawei: snmp should include iso view and mib-2
        """
        try:
            return mac_address_validator(self.session.get(consts.lldpLocChassisId.oid).value)
        except EzSNMPError as e:
            self.exceptions.append(DiscoveryException(item="chassis_id", exception=str(e)))
            return ""

    @property
    def interfaces(self) -> list[Interface]:
        """
        collect interfaces via `IF-MIB`, if filtering by the items, implement it the manufacturer factory
        """
        try:
            if_index = self.session.bulkwalk(consts.ifIndex.oid)
            if_name = self.session.bulkwalk(consts.ifDescr.oid)
            if_mtu = self.session.bulkwalk(consts.ifMtu.oid)
            if_speed = self.session.bulkwalk(consts.ifSpeed.oid)
            if_type = self.session.bulkwalk(consts.ifType.oid)
            if_phys_addr = self.session.bulkwalk(consts.ifPhysAddr.oid)
            if_admin = self.session.bulkwalk(consts.ifAdminStatus.oid)
            if_oper = self.session.bulkwalk(consts.ifOperStatus.oid)
        except EzSNMPError as e:
            self.exceptions.append(DiscoveryException(item="interfaces", exception=str(e)))
            return []
        index_if_index = {x.oid_index: x.value for x in if_index}
        index_if_name = {x.oid_index: x.value for x in if_name}
        index_if_mtu = {x.oid_index: x.value for x in if_mtu}
        index_if_speed = {x.oid_index: x.value for x in if_speed}
        index_if_type = {x.oid_index: x.value for x in if_type}
        if_phys_addr = {x.oid_index: x.value for x in if_phys_addr}
        index_if_admin = {x.oid_index: x.value for x in if_admin}
        index_if_oper = {x.oid_index: x.value for x in if_oper}
        return [
            Interface(
                if_index=int(x),
                if_descr=index_if_name[x],
                if_mtu=int(index_if_mtu[x]),
                if_speed=int(index_if_speed[x]),
                if_type=index_if_type[x],
                if_phys_address=mac_address_validator(if_phys_addr[x]),
                if_admin_status=index_if_admin[x],
                if_oper_status=index_if_oper[x],
            )
            for x in index_if_index
        ]

    @property
    def lldp_neighbors(self) -> list[LldpNeighbor]:
        """
        collect lldp neighbors via `LLDP-MIB`
        Special configuration for network devices: include iso mib-2 view in snmp configuration
        lldpRemChassisID: snmp_index value the last of 2 is localportID's index(last of 1)
        """
        try:
            local_chassis_id = self.chassis_id
            local_if_name = self.session.bulkwalk(consts.lldpLoPortId.oid)
            local_if_descr = self.session.bulkwalk(consts.lldpLocPortDesc.oid)
            remote_chassis_id = self.session.bulkwalk(consts.lldpRemChassisId.oid)
            remote_hostname = self.session.bulkwalk(consts.lldpRemSysName.oid)
            remote_if_name = self.session.bulkwalk(consts.lldpRemPortId.oid)
            remote_if_descr = self.session.bulkwalk(consts.lldpRemPortDesc.oid)
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
                local_if_name=index_local_if_name[x],
                local_if_descr=index_local_if_descr[x],
                remote_chassis_id=index_remote_chassis_id[x],
                remote_hostname_id=index_remote_hostname[x],
                remote_if_name=index_remote_if_name[x],
                remote_if_descr=index_remote_if_descr[x],
            )
            for x in index_remote_chassis_id
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
            ent_phy_descr = self.session.bulkwalk(consts.entPhysicalDescr.oid)
            ent_phy_name = self.session.bulkwalk(consts.entPhysicalName.oid)
            ent_phy_software = self.session.bulkwalk(consts.entPhysicalSoftwareRev.oid)
            ent_phy_serial = self.session.bulkwalk(consts.entPhysicalSerialNum.oid)
        except EzSNMPError as e:
            self.exceptions.append(DiscoveryException(item="entities", exception=str(e)))
            return []
        index_ent_phy_class = {x.oid.split(".")[-1]: x.value for x in ent_phy_class if int(x.value) == 3}  # noqa: PLR2004
        index_ent_phy_descr = {x.oid.split(".")[-1]: x.value for x in ent_phy_descr}
        index_ent_phy_name = {x.oid.split(".")[-1]: x.value for x in ent_phy_name}
        index_ent_phy_software = {x.oid.split(".")[-1]: x.value for x in ent_phy_software}
        index_ent_phy_serial = {x.oid.split(".")[-1]: x.value for x in ent_phy_serial}
        return [
            Entity(
                ent_physical_class=int(x),
                ent_physical_descr=index_ent_phy_descr[x],
                ent_physical_name=index_ent_phy_name[x],
                ent_physical_software_rev=index_ent_phy_software[x],
                ent_physical_serial_num=index_ent_phy_serial[x],
            )
            for x in index_ent_phy_class
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
    def mac_address_table(self) -> Any: ...

    @property
    def arp_table(self) -> Any: ...

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
                routes=self.routes,
                exceptions=self.exceptions,
            )
        return {x: getattr(self, x) for x in items}  # type: ignore  # noqa: PGH003
