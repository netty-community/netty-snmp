from types import TracebackType
from typing import Any, Literal, TypedDict

import pandas as pd
from ezsnmp import Session
from tcppinglib import tcpping

from netty_snmp.factory import consts


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
    privacy_passphrase: str


class SnmpFactory:
    session: Session | None = None
    hostname: str | None = None
    chasis_id: str | None = None
    sys_object_id: str | None = None

    def __init__(
        self,
        ip: str,
        port: int = consts.SNMP_DEFAULT_PORT,
        version: consts.SnmpVersion = consts.SnmpVersion.v2c,
        community: str | None = consts.SNMP_DEFAULT_COMMUNITY,
        v3_params: SnmpV3Params | None = None,
        model: str | None = None,
    ) -> None:
        self.ip = ip
        self.port = port
        self.version = version
        self.community = community
        self.v3_params = v3_params
        self.model = model

    @property
    def _ping(self) -> bool:
        return tcpping(self.ip, self.port).is_alive

    def _session(self) -> Session:
        if not self._ping:
            raise SnmpConnectionError(f"Failed to connect to SNMP port: {self.ip}:{self.port}")

        if self.version == consts.SnmpVersion.v2c:
            return Session(
                hostname=self.ip, remote_port=self.port, community=self.community, version=consts.SnmpVersion.v2c
            )
        if self.version == consts.SnmpVersion.v3:
            return Session(hostname=self.ip, remote_port=self.port, version=consts.SnmpVersion.v3, **self.v3_params)
        raise SnmpVersionError(f"Unsupported SNMP version: {self.version}")

    def _snmp_discovery_df(self, items: list[consts.SnmpItem]) -> pd.DataFrame:
        oid_mapping = {item.oid: item for item in items}
        results = self.session.get_bulk([item.oid for item in items])
        dfs = [[result.oid_index, oid_mapping[result.oid]["name"], result.value] for result in results]
        df = pd.DataFrame(dfs, columns=["snmp_index", "name", "value"])
        return df.pivot_table(index="snmp_index", columns="name", values="value")

    def _close(self) -> None:
        if not self.session:
            return
        self.session = None
        return

    def __enter__(self) -> "SnmpFactory":
        self.session = self._session()
        return self

    def __exit__(
        self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None
    ) -> None:
        self.close()

    @property
    def _hostname(self) -> str:
        return self.session.get(consts.sysName.oid).value

    @property
    def uptime(self) -> int:
        return self.session.get(consts.sysUpTime.oid).value

    @property
    def _chasis_id(self) -> Any:
        """
        collect chasis id via `LLDP-MIB`.
        Special configuration for Huawei: snmp should include iso view and mib-2
        """
        #  lldpLocChassisId  = "1.0.8802.1.1.2.1.3.2"
        # return self.session.get(lldpLocChassisId).value

    @property
    def interfaces(self) -> dict:
        interface_oids = [
            consts.ifIndex.oid,
            consts.ifDescr.oid,
            consts.ifType.oid,
            consts.ifMtu.oid,
            consts.ifSpeed.oid,
            consts.ifPhysAddr.oid,
            consts.ifAdminStatus.oid,
            consts.ifOperStatus.oid,
        ]
        return self._snmp_discovery_df(interface_oids).to_dict(orient="records")

    @property
    def lldp_neighbors(self) -> Any:
        local_if_index = self.session.get_bulk(consts.lldpLocalPortId.oid)
        lldp_oids = [
            consts.lldpRemChassisIdSubtype,
            consts.lldpRemChassisId,
            consts.lldpRemPortIdSubtype,
            consts.lldpRemPortId,
            consts.lldpRemPortDesc,
            consts.lldpRemSysName,
        ]
        return self._snmp_discovery_df(lldp_oids).to_dict(orient="records")

    @property
    def entities(self) -> Any:
        """
        collect entities via `ENTITY-MIB`
        basically: chassis(3) should be the main module of device.
        but fuck huawei (3 or 9(module) for different product lines) because its unstandard implementation
        """
        entities_oids = [
            consts.entPhysicalClass.oid,
            consts.entPhysicalDescr.oid,
            consts.entPhysicalName.oid,
            consts.entPhysicalFirmwareRev,
            consts.entPhysicalHardwareRev,
            consts.entPhysicalSerialNum,
        ]
        return self._snmp_discovery_df(entities_oids).to_dict(orient="records")

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


    def discovery(self) -> dict:
        return {
            "hostname": self._hostname,
            "chassis_id": self.chasis_id,
            "uptime": self.uptime,
            "interfaces": self.interfaces,
            "lldp_neighbors": self.lldp_neighbors,
            "stack": self.stack,
            "vlans": self.vlans,
            "prefixes": self.prefixes,
            "routes": self.routes,
        }
