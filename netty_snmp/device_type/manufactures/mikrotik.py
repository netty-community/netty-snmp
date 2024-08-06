from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from netty_snmp._types import DeviceType

MIKROTIK_DEVICE_TYPES: dict[str, "DeviceType"] = {
    "1.3.6.1.4.1.14988.1": {"manufacturer": "MikroTik", "platform": "mikrotik_switchos", "model": "RB1200"}
}
