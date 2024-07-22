from typing import NamedTuple, TypedDict


class DeviceType(TypedDict):
    platform: str
    manufacturer: str
    model: str


class SnmpDiscovery(NamedTuple):
    name: str
    oid: str
    snmp_index: str
    snmp_value: str | float | int


class Interface(TypedDict):
    if_index: int
    if_descr: str
    if_type: int
    if_mtu: int
    if_speed: int
    if_phys_address: str
    if_admin_status: int
    if_oper_status: int


class LldpNeighbor(TypedDict):
    local_chassis_id: str
    local_port_id: str
    remote_chassis_id: str
    remote_port_id: str


class DiscoveryData(TypedDict):
    hostname: str
    uptime: str
    device_type: str | None
    chassis_id: str
    manufacturer: str
    platform: str
    serial_number: str
    version: str
    interfaces: list[Interface]
    lldp_neighbors: list[LldpNeighbor]
    stack: list[dict]
    vlans: list[dict]
    prefixes: list[dict] | None
    routes: list[dict] | None


class DiscoveryResponse(TypedDict):
    ip: str
    data: DiscoveryData
    snmp_reachable: bool
    icmp_reachable: bool
    ssh_reachable: bool
    sysObjectID: str | None
