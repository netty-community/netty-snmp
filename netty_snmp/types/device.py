from typing import TypedDict


class Entity(TypedDict):
    ent_physical_class: int
    ent_physical_descr: str
    ent_physical_name: str
    ent_physical_software_rev: str
    ent_physical_serial_num: str


class StackMember(TypedDict):
    id: int
    priority: int
    role: str
    mac_address: str
