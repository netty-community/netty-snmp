from typing import TypedDict


class Vlan(TypedDict):
    vlan_id: int
    vlan_name: str
    if_index: int
    network: str | None
    gateway: str | None
