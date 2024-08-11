from netty_snmp.factory import consts
from netty_snmp.factory.snmp_factory import SnmpFactory, SnmpV3Params


class AristaSnmpFactory(SnmpFactory):
    def __init__(
        self,
        ip: str,
        port: int = consts.SNMP_DEFAULT_PORT,
        version: consts.SnmpVersion = consts.SnmpVersion.v2c,
        community: str | None = consts.SNMP_DEFAULT_COMMUNITY,
        v3_params: SnmpV3Params | None = None,
        snmp_max_repetitions: int = consts.SNMP_MAX_REPETITIONS,
    ) -> None:
        super().__init__(ip, port, version, community, v3_params, snmp_max_repetitions)
