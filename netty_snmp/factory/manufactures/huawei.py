from ezsnmp import EzSNMPError

from netty_snmp._types import DiscoveryException, StackMember
from netty_snmp.factory import consts
from netty_snmp.factory.snmp_factory import SnmpFactory, SnmpV3Params
from netty_snmp.utils import mac_address_validator


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
    def stack(self) -> list[StackMember]:
        stack_running = self.session.get(consts.hwStackRun.oid).value
        if stack_running != "1":
            return []
        try:
            hw_stack_id = self.session.bulkwalk(
                consts.hwMemberCurrentStackId.oid, max_repetitions=self.snmp_max_repetitions
            )
            hw_stack_priority = self.session.bulkwalk(
                consts.hwMemberStackPriority.oid, max_repetitions=self.snmp_max_repetitions
            )
            hw_stack_role = self.session.bulkwalk(
                consts.hwMemberStackRole.oid, max_repetitions=self.snmp_max_repetitions
            )
            hw_stack_mac_address = self.session.bulkwalk(
                consts.hwMemberStackMacAddress.oid, max_repetitions=self.snmp_max_repetitions
            )

        except EzSNMPError as e:
            self.exceptions.append(DiscoveryException(item="stack", exception=str(e)))
            return []
        index_hw_stack_id = {x.oid_index: x.value for x in hw_stack_id}
        index_hw_stack_priority = {x.oid_index: x.value for x in hw_stack_priority}
        index_hw_stack_role = {x.oid_index: x.value for x in hw_stack_role}
        index_hw_stack_mac_address = {x.oid_index: mac_address_validator(x.value) for x in hw_stack_mac_address}
        return [
            StackMember(
                id=index_hw_stack_id[x],
                priority=index_hw_stack_priority[x],
                role=index_hw_stack_role[x],
                mac_address=index_hw_stack_mac_address[x],
            )
            for x in index_hw_stack_id
        ]
