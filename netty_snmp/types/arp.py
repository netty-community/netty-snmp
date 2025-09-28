from typing import TypedDict


class ArpTableEntry(TypedDict):
    ip_address: str
    mac_address: str
    arp_type: str
    if_index: int
    vlan_id: int
    ip_network: str


def get_arp_type(value: int) -> str:
    types = {
        1: "other",
        2: "invalid",
        3: "dynamic",
        4: "static",
    }
    return types.get(value, "unknown")
