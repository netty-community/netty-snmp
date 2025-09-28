from ipaddress import IPv4Network, IPv6Network
from typing import Literal, NamedTuple, TypedDict

from netty_snmp.types.device import Entity, StackMember
from netty_snmp.types.interface import Interface
from netty_snmp.types.lldp import LldpNeighbor
from netty_snmp.types.mac_addr import MacAddressTableEntry
from netty_snmp.types.vlan import Vlan

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

type DispatchItem = Literal["sys_object_id"]


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

    def get_value_type(self) -> type[str] | type[int] | type[float] | type[bytes]:
        type_mapping = {"str": str, "int": int, "float": float, "bytes": bytes}
        return type_mapping[self.value_type]


class DiscoveryException(TypedDict):
    item: DispatchItem | DiscoveryItem
    exception: str


class SnmpDiscoveryData(TypedDict, total=False):
    hostname: str | None
    sys_descr: str | None
    uptime: str | None
    chassis_id: str | None
    interfaces: list[Interface]
    lldp_neighbors: list[LldpNeighbor]
    entities: list[Entity]
    stack: list[StackMember]
    vlans: list[Vlan]
    mac_address_table: list[MacAddressTableEntry]
    arp_table: list[MacAddressTableEntry]
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
    sys_object_id: str | None
    exceptions: list[DiscoveryException] | None
