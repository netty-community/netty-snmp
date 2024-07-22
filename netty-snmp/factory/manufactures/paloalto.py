from netty.factory import consts
from netty.factory.snmp_factory import SnmpFactory, SnmpV3Params


class PaloaltoSnmpFactory(SnmpFactory):
    def __init__(
        self,
        ip: str,
        port: int = consts.SNMP_DEFAULT_PORT,
        version: consts.SnmpVersion = consts.SnmpVersion.v2c,
        community: str | None = consts.SNMP_DEFAULT_COMMUNITY,
        v3_params: SnmpV3Params | None = None,
    ) -> None:
        super().__init__(ip, port, version, community, v3_params)
