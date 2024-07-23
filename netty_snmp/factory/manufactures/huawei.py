from netty_snmp.factory import consts
from netty_snmp.factory.snmp_factory import SnmpFactory, SnmpV3Params


class HuaweiSnmpFactory(SnmpFactory):
    def __init__(
        self,
        ip: str,
        port: int = consts.SNMP_DEFAULT_PORT,
        version: consts.SnmpVersion = consts.SnmpVersion.v2c,
        community: str | None = consts.SNMP_DEFAULT_COMMUNITY,
        v3_params: SnmpV3Params | None = None,
        model: str | None = None,
    ) -> None:
        super().__init__(ip, port, version, community, v3_params, model)

    @property
    def stack(self) -> dict:
        stack_running = self.session.get(consts.hwStackRun.oid).value
        if stack_running != "1":
            return {}
        stack_oids = [
            consts.hwMemberCurrentStackId,
            consts.hwMemberStackPriority,
            consts.hwMemberStackRole,
            consts.hwMemberStackMacAddress,
            consts.hwMemberStackDeviceType,
        ]
        return self._snmp_discovery_df(stack_oids).to_dict(orient="records")
