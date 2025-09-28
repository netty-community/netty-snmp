from typing import TypedDict


class MacAddressTableEntry(TypedDict):
    mac_address: str
    if_index: int
    ip_address: str
    vlan_id: int
