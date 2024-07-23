from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from netty_snmp._types import DeviceType


TP_LINK_DEVICE_TYPES: dict[str, "DeviceType"] = {
    "1.3.6.1.4.1.11863.1.1.35": {"manufacturer": "TP-Link", "platform": "tplink_jetstream", "model": "T1500-28PCT"},
    "1.3.6.1.4.1.11863.3.2.10": {"manufacturer": "TP-Link", "platform": "tplink_jetstream", "model": "EAP245"},
    "1.3.6.1.4.1.11863.5.29": {"manufacturer": "TP-Link", "platform": "tplink_jetstream", "model": "T1600G-52TS"},
}
