from ipaddress import IPv4Network, IPv6Network
from typing import Literal, NamedTuple, TypedDict

type IPvANyNetwork = IPv4Network | IPv6Network

type DiscoveryItem = Literal[
    "hostname",
    "sys_descr",
    "chassis_id",
    "uptime",
    "interfaces",
    "lldp_neighbors",
    "stack",
    "vlans",
    "prefixes",
    "routes",
    "entities",
    "mac_address_table",
    "arp_table",
]

type DispatchItem = Literal[
    "sys_object_id",
    "hostname",
    "sys_descr",
    "chassis_id",
    "uptime",
    "interfaces",
    "lldp_neighbors",
    "stack",
    "vlans",
    "prefixes",
    "routes",
    "entities",
    "mac_address_table",
    "arp_table",
]


class DeviceType(TypedDict):
    platform: str
    manufacturer: str
    model: str


class SnmpDiscovery(NamedTuple):
    name: str
    oid: str
    snmp_index: str
    snmp_value: str | float | int


class SnmpItem(NamedTuple):
    name: str
    oid: str
    value_type: Literal["str", "int", "float"]
    description: str | None = None
    value_mapping: dict[int, str] | None = None
    to_hex: bool = False

    def get_value_type(self) -> str | int | float:
        type_mapping = {"str": str, "int": int, "float": float}
        return type_mapping[self.value_type]


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
    local_hostname: str
    local_if_name: str
    local_if_descr: str
    remote_chassis_id: str
    remote_hostname_id: str
    remote_if_name: str
    remote_if_descr: str


class Entity(TypedDict):
    ent_physical_class: int
    ent_physical_descr: str
    ent_physical_name: str
    ent_physical_firmware_rev: str
    ent_physical_hardware_rev: str
    ent_physical_serial_num: str


class DiscoveryException(TypedDict):
    item: DispatchItem
    exception: str


class SnmpDiscoveryData(TypedDict, total=False):
    hostname: str
    sys_descr: str
    uptime: str
    chassis_id: str
    interfaces: list[Interface]
    lldp_neighbors: list[LldpNeighbor]
    stack: list[dict]
    vlans: list[dict]
    prefixes: list[dict] | None
    routes: list[dict] | None
    exceptions: list[DiscoveryException]


class DiscoveryData(SnmpDiscoveryData):
    device_type: str
    manufacturer: str
    platform: str


class DiscoveryResponse(TypedDict):
    ip: str
    data: DiscoveryData | None
    snmp_reachable: bool
    icmp_reachable: bool
    ssh_reachable: bool
    sysObjectID: str | None
    exceptions: list[DiscoveryException] | None
