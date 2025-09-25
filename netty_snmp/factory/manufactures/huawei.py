from gufo.snmp import SnmpError, SnmpVersion

from netty_snmp._types import DiscoveryException, StackMember
from netty_snmp.factory import consts
from netty_snmp.factory.snmp_factory import SnmpFactory, SnmpV3Params
from netty_snmp.utils import mac_address_validator


class HuaweiSnmpFactory(SnmpFactory):
    def __init__(
        self,
        ip: str,
        port: int = consts.SNMP_DEFAULT_PORT,
        version: SnmpVersion = SnmpVersion.v2c,
        community: str | None = consts.SNMP_DEFAULT_COMMUNITY,
        v3_params: SnmpV3Params | None = None,
        snmp_max_repetitions: int = consts.SNMP_MAX_REPETITIONS,
    ) -> None:
        super().__init__(ip, port, version, community, v3_params, snmp_max_repetitions)

    @property
    def stack(self) -> list[StackMember]:
        stack_running = self.session.get(consts.hwStackRun.oid)
        if stack_running != "1":
            return []
        try:
            hw_stack_id = self.session.getbulk(
                consts.hwMemberCurrentStackId.oid, max_repetitions=self.snmp_max_repetitions
            )
            hw_stack_priority = self.session.getbulk(
                consts.hwMemberStackPriority.oid, max_repetitions=self.snmp_max_repetitions
            )
            hw_stack_role = self.session.getbulk(
                consts.hwMemberStackRole.oid, max_repetitions=self.snmp_max_repetitions
            )
            hw_stack_mac_address = self.session.getbulk(
                consts.hwMemberStackMacAddress.oid, max_repetitions=self.snmp_max_repetitions
            )

        except SnmpError as e:
            self.exceptions.append(DiscoveryException(item="stack", exception=str(e)))
            return []
        index_hw_stack_id = {x[0]: x[1] for x in hw_stack_id}
        index_hw_stack_priority = {x[0]: x[1] for x in hw_stack_priority}
        index_hw_stack_role = {x[0]: x[1] for x in hw_stack_role}
        index_hw_stack_mac_address = {x[0]: mac_address_validator(x[1]) for x in hw_stack_mac_address}
        return [
            StackMember(
                id=index_hw_stack_id.get(x),
                priority=index_hw_stack_priority.get(x),
                role=index_hw_stack_role.get(x),
                mac_address=index_hw_stack_mac_address.get(x),
            )
            for x in index_hw_stack_id
        ]
