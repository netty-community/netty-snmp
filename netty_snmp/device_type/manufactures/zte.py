from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from netty_snmp._types import DeviceType

ZTE_DEVICE_TYPES: dict[str, "DeviceType"] = {
    "1.3.6.1.4.1.3902.1004.9806.2.1.1": {"manufacturer": "ZTE", "platform": "zte_zxros", "model": "ZXDSL9806H"},
    "1.3.6.1.4.1.3902.3.100.14": {"manufacturer": "ZTE", "platform": "zte_zxros", "model": "ZXR10"},
    "1.3.6.1.4.1.3902.3.100.173": {"manufacturer": "ZTE", "platform": "zte_zxros", "model": "ZXR10 2842"},
    "1.3.6.1.4.1.3902.3.100.20": {"manufacturer": "ZTE", "platform": "zte_zxros", "model": "ZXR10 5928"},
    "1.3.6.1.4.1.3902.3.100.23": {"manufacturer": "ZTE", "platform": "zte_zxros", "model": "ZXR10"},
    "1.3.6.1.4.1.3902.3.100.405": {"manufacturer": "ZTE", "platform": "zte_zxros", "model": "ZX10"},
    "1.3.6.1.4.1.3902.3.600.3.1.604": {"manufacturer": "ZTE", "platform": "zte_zxros", "model": "ZXR10 9900"},
    "1.3.6.1.4.1.3902.3.600.3.1.724": {"manufacturer": "ZTE", "platform": "zte_zxros", "model": "ZXR10 5960"},
}
