from typing import TypedDict


class Interface(TypedDict):
    if_index: int
    if_name: str
    if_descr: str
    if_type: int
    if_mtu: int
    if_speed: int
    if_high_speed: int
    if_phys_address: str
    if_admin_status: str
    if_oper_status: str
    if_ip_address: list[str]
    if_port_mode: str | None
