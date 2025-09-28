from typing import TypedDict


class ApTableEntry(TypedDict):
    name: str
    mac_address: str
    serial_number: str
    management_ip: str
    group_name: str | None
    device_type: str
    manufacturer: str
    wlc_ip: str | None
    os_version: str | None
