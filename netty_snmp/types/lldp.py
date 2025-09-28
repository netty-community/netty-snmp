from typing import TypedDict


class LldpNeighbor(TypedDict):
    local_chassis_id: str
    local_hostname: str
    local_if_name: str
    local_if_descr: str
    remote_chassis_id: str
    remote_hostname_id: str
    remote_if_name: str
    remote_if_descr: str
