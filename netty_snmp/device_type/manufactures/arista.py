from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from netty_snmp._types import DeviceType

ARISTA_DEVICE_TYPES: dict[str, "DeviceType"] = {
    ".1.3.6.1.4.1.30065.1.2546.720.858.48.207.2": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "720XP-48ZC2",
    },
    ".1.3.6.1.4.1.30065.1.2546.720.858.48.2600.6": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "720XP-48Y6",
    },
    ".1.3.6.1.4.1.30065.1.2759": {"manufacturer": "Arista", "platform": "arista_eos", "model": "VEOS"},
    ".1.3.6.1.4.1.30065.1.3011.7010.427.48": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "DCS-7010T-48",
    },
    ".1.3.6.1.4.1.30065.1.3011.7010.427.48.2957": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "7010T-48-DC",
    },
    ".1.3.6.1.4.1.30065.1.3011.7020.1964.48": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "7020TR-48",
    },
    ".1.3.6.1.4.1.30065.1.3011.7020.312.48": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "7020TRA-48",
    },
    ".1.3.6.1.4.1.30065.1.3011.7020.3735.24.2878.2": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "7020SR-24C2",
    },
    ".1.3.6.1.4.1.30065.1.3011.7048.427.3648": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "DCS-7048T-A",
    },
    ".1.3.6.1.4.1.30065.1.3011.7048.427.4.3282": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "DCS-7048T-4S",
    },
    ".1.3.6.1.4.1.30065.1.3011.7050.1958.128": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "7050TX-128",
    },
    ".1.3.6.1.4.1.30065.1.3011.7050.1958.128.761": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "7050TX-128-SSD",
    },
    ".1.3.6.1.4.1.30065.1.3011.7050.1958.2.128": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "7050TX2-128",
    },
    ".1.3.6.1.4.1.30065.1.3011.7050.1958.2.128.761": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "7050TX2-128-SSD",
    },
    ".1.3.6.1.4.1.30065.1.3011.7050.1958.48": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "7050TX-48",
    },
    ".1.3.6.1.4.1.30065.1.3011.7050.1958.48.761": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "7050TX-48-SSD",
    },
    ".1.3.6.1.4.1.30065.1.3011.7050.1958.64": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "DCS-7050TX-64",
    },
    ".1.3.6.1.4.1.30065.1.3011.7050.1958.64.761": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "7050TX-64-SSD",
    },
    ".1.3.6.1.4.1.30065.1.3011.7050.1958.72": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "7050TX-72",
    },
    ".1.3.6.1.4.1.30065.1.3011.7050.1958.72.2512": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "DCS-7050TX-72Q",
    },
    ".1.3.6.1.4.1.30065.1.3011.7050.1958.72.2512.761": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "7050TX-72-Q-SSD",
    },
    ".1.3.6.1.4.1.30065.1.3011.7050.1958.72.761": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "7050TX-72-SSD",
    },
    ".1.3.6.1.4.1.30065.1.3011.7050.1958.96": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "7050TX-96",
    },
    ".1.3.6.1.4.1.30065.1.3011.7050.1958.96.761": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "7050TX-96-SSD",
    },
    ".1.3.6.1.4.1.30065.1.3011.7050.2512.16": {"manufacturer": "Arista", "platform": "arista_eos", "model": "7050Q-16"},
    ".1.3.6.1.4.1.30065.1.3011.7050.2512.16.761": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "7050Q-16-SSD",
    },
    ".1.3.6.1.4.1.30065.1.3011.7050.2733.3.32.3282": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "DCS-7050CX3-32S",
    },
    ".1.3.6.1.4.1.30065.1.3011.7050.3095.2.32.3282": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "DCS-7050QX2-32S",
    },
    ".1.3.6.1.4.1.30065.1.3011.7050.3095.2.32.3282.761": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "7050QX-232-S-SSD",
    },
    ".1.3.6.1.4.1.30065.1.3011.7050.3095.32": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "7050QX-32",
    },
    ".1.3.6.1.4.1.30065.1.3011.7050.3095.32.2745.761": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "7050QX-32-CL-SSD",
    },
    ".1.3.6.1.4.1.30065.1.3011.7050.3095.32.3282": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "DCS-7050QX-32S",
    },
    ".1.3.6.1.4.1.30065.1.3011.7050.3095.32.3282.761": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "7050QX-32-S-SSD",
    },
    ".1.3.6.1.4.1.30065.1.3011.7050.3095.32.761": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "7050QX-32-SSD",
    },
    ".1.3.6.1.4.1.30065.1.3011.7050.3282": {"manufacturer": "Arista", "platform": "arista_eos", "model": "DCS 7148S-F"},
    ".1.3.6.1.4.1.30065.1.3011.7050.3282.52": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "DCS7050S52",
    },
    ".1.3.6.1.4.1.30065.1.3011.7050.3282.52.761": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "7050S-52-SSD",
    },
    ".1.3.6.1.4.1.30065.1.3011.7050.3282.64": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "DCS-7050S-64",
    },
    ".1.3.6.1.4.1.30065.1.3011.7050.3282.64.761": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "7050S-64-SSD",
    },
    ".1.3.6.1.4.1.30065.1.3011.7050.3741.128": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "DCS-7050SX-128",
    },
    ".1.3.6.1.4.1.30065.1.3011.7050.3741.128.761": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "7050SX-128-SSD",
    },
    ".1.3.6.1.4.1.30065.1.3011.7050.3741.2.128": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "7050SX2-128",
    },
    ".1.3.6.1.4.1.30065.1.3011.7050.3741.2.128.761": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "7050SX2-128-SSD",
    },
    ".1.3.6.1.4.1.30065.1.3011.7050.3741.2.72.2512": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "7050SX2-72Q",
    },
    ".1.3.6.1.4.1.30065.1.3011.7050.3741.2.72.2512.761": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "7050SX2-72Q-SSD",
    },
    ".1.3.6.1.4.1.30065.1.3011.7050.3741.3.48.1654.12": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "DCS-7050SX3-48YC12",
    },
    ".1.3.6.1.4.1.30065.1.3011.7050.3741.3.48.1654.8": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "7050SX3-48YC8",
    },
    ".1.3.6.1.4.1.30065.1.3011.7050.3741.3.96.1654.8": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "7050SX3-96YC8",
    },
    ".1.3.6.1.4.1.30065.1.3011.7050.3741.64": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "DCS-7050SX-64",
    },
    ".1.3.6.1.4.1.30065.1.3011.7050.3741.64.761": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "7050SX-64-SSD",
    },
    ".1.3.6.1.4.1.30065.1.3011.7050.3741.72": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "7050SX-72",
    },
    ".1.3.6.1.4.1.30065.1.3011.7050.3741.72.2512": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "DCS-7050SX-72Q",
    },
    ".1.3.6.1.4.1.30065.1.3011.7050.3741.72.2512.761": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "7050SX-72-Q-SSD",
    },
    ".1.3.6.1.4.1.30065.1.3011.7050.3741.72.761": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "7050SX-72-SSD",
    },
    ".1.3.6.1.4.1.30065.1.3011.7050.3741.96": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "7050SX-96",
    },
    ".1.3.6.1.4.1.30065.1.3011.7050.3741.96.761": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "7050SX-96-SSD",
    },
    ".1.3.6.1.4.1.30065.1.3011.7050.427.36": {"manufacturer": "Arista", "platform": "arista_eos", "model": "7050T-36"},
    ".1.3.6.1.4.1.30065.1.3011.7050.427.52": {"manufacturer": "Arista", "platform": "arista_eos", "model": "7050T-52"},
    ".1.3.6.1.4.1.30065.1.3011.7050.427.52.761": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "7050T-52-SSD",
    },
    ".1.3.6.1.4.1.30065.1.3011.7050.427.64": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "DCS-7050T-64",
    },
    ".1.3.6.1.4.1.30065.1.3011.7050.427.64.761": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "7050T-64-SSD",
    },
    ".1.3.6.1.4.1.30065.1.3011.7060.2733.2.32.3282": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "DCS-7060CX2-32S",
    },
    ".1.3.6.1.4.1.30065.1.3011.7060.2733.32.3282": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "DCS-7060CX-32S",
    },
    ".1.3.6.1.4.1.30065.1.3011.7060.2733.32.3282.761": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "7060CX-32S-SSD",
    },
    ".1.3.6.1.4.1.30065.1.3011.7060.3741.2.48.1654.6": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "DCS-7060SX2-48YC6",
    },
    ".1.3.6.1.4.1.30065.1.3011.7120.427.4.3282": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "DCS7120T4S",
    },
    ".1.3.6.1.4.1.30065.1.3011.7124.2312": {"manufacturer": "Arista", "platform": "arista_eos", "model": "7124FX"},
    ".1.3.6.1.4.1.30065.1.3011.7124.2312.2745": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "7124FX-CL",
    },
    ".1.3.6.1.4.1.30065.1.3011.7124.3282": {"manufacturer": "Arista", "platform": "arista_eos", "model": "DCS-7124S"},
    ".1.3.6.1.4.1.30065.1.3011.7124.3741": {"manufacturer": "Arista", "platform": "arista_eos", "model": "DCS-7124SX"},
    ".1.3.6.1.4.1.30065.1.3011.7124.3741.3282": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "DCS-7124SX-S",
    },
    ".1.3.6.1.4.1.30065.1.3011.7124.3741.761": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "7124SX-SSD",
    },
    ".1.3.6.1.4.1.30065.1.3011.7140.427.8.3282": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "DCS7140T8S",
    },
    ".1.3.6.1.4.1.30065.1.3011.7148.3282": {"manufacturer": "Arista", "platform": "arista_eos", "model": "DCS7148S"},
    ".1.3.6.1.4.1.30065.1.3011.7148.3741": {"manufacturer": "Arista", "platform": "arista_eos", "model": "DCS-7148SX"},
    ".1.3.6.1.4.1.30065.1.3011.7150.3282.24": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "DCS-7150S-24",
    },
    ".1.3.6.1.4.1.30065.1.3011.7150.3282.24.2745": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "DCS-7150S-24-CL",
    },
    ".1.3.6.1.4.1.30065.1.3011.7150.3282.24.2745.761": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "7150S-24-CL-SSD",
    },
    ".1.3.6.1.4.1.30065.1.3011.7150.3282.52.2745": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "DCS-7150S-52-CL",
    },
    ".1.3.6.1.4.1.30065.1.3011.7150.3282.52.2745.761": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "7150S-52-CL-SSD",
    },
    ".1.3.6.1.4.1.30065.1.3011.7150.3282.64.2745": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "DCS-7150S-64-CL",
    },
    ".1.3.6.1.4.1.30065.1.3011.7150.3282.64.2745.761": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "DCS-7150S-64-CL-SSD",
    },
    ".1.3.6.1.4.1.30065.1.3011.7160.32.2726": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "7160-32CQ",
    },
    ".1.3.6.1.4.1.30065.1.3011.7160.32.2726.761": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "7160-32CQ-SSD",
    },
    ".1.3.6.1.4.1.30065.1.3011.7160.48.1654.6": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "7160-48YC6",
    },
    ".1.3.6.1.4.1.30065.1.3011.7160.48.1654.6.761": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "7160-48YC6-SSD",
    },
    ".1.3.6.1.4.1.30065.1.3011.7160.48.1981.6": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "7160-48TC6",
    },
    ".1.3.6.1.4.1.30065.1.3011.7160.48.1981.6.761": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "7160-48TC6-SSD",
    },
    ".1.3.6.1.4.1.30065.1.3011.7250.3095.64": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "DCS-7250QX-64",
    },
    ".1.3.6.1.4.1.30065.1.3011.7250.3095.64.761": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "7250QX-64-SSD",
    },
    ".1.3.6.1.4.1.30065.1.3011.7250.3095.64.972": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "7250QX-64M",
    },
    ".1.3.6.1.4.1.30065.1.3011.7260.2733.3.64": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "7260CX3-64",
    },
    ".1.3.6.1.4.1.30065.1.3011.7260.2733.64": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "7260CX-64",
    },
    ".1.3.6.1.4.1.30065.1.3011.7260.2733.64.761": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "7260CX-64-SSD",
    },
    ".1.3.6.1.4.1.30065.1.3011.7260.3095.64": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "7260QX-64",
    },
    ".1.3.6.1.4.1.30065.1.3011.7260.3095.64.761": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "7260QX-64-SSD",
    },
    ".1.3.6.1.4.1.30065.1.3011.7280.1347.48.2878.6": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "7280SRA-48C6",
    },
    ".1.3.6.1.4.1.30065.1.3011.7280.1347.48.2878.6.972": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "7280SRA-48-C6M",
    },
    ".1.3.6.1.4.1.30065.1.3011.7280.1964.48.2878.6": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "7280TR-48-C6",
    },
    ".1.3.6.1.4.1.30065.1.3011.7280.1964.48.2878.6.972": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "7280TR-48-C6M",
    },
    ".1.3.6.1.4.1.30065.1.3011.7280.2655.2878.36.3282": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "7280QRA-C36S",
    },
    ".1.3.6.1.4.1.30065.1.3011.7280.2655.2878.36.3282.972": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "7280QRA-C36S-M",
    },
    ".1.3.6.1.4.1.30065.1.3011.7280.2655.2878.72": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "7280QRA-C72",
    },
    ".1.3.6.1.4.1.30065.1.3011.7280.2655.2878.72.972": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "7280QRA-C72M",
    },
    ".1.3.6.1.4.1.30065.1.3011.7280.2727.2.3648.30": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "7280CR2A-30",
    },
    ".1.3.6.1.4.1.30065.1.3011.7280.2727.3.32.1605.4": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "7280CR3-32D4",
    },
    ".1.3.6.1.4.1.30065.1.3011.7280.2727.48": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "7280CR-48",
    },
    ".1.3.6.1.4.1.30065.1.3011.7280.2727.48.761": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "7280CR-48-SSD",
    },
    ".1.3.6.1.4.1.30065.1.3011.7280.3101.2878.36": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "7280QR-C36",
    },
    ".1.3.6.1.4.1.30065.1.3011.7280.3101.2878.36.3282": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "7280QR-C36S",
    },
    ".1.3.6.1.4.1.30065.1.3011.7280.3101.2878.36.3282.972": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "7280QR-C36SM",
    },
    ".1.3.6.1.4.1.30065.1.3011.7280.3101.2878.36.972": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "7280QR-C36M",
    },
    ".1.3.6.1.4.1.30065.1.3011.7280.3101.2878.72": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "DCS-7280QR-C72",
    },
    ".1.3.6.1.4.1.30065.1.3011.7280.3101.2878.72.972": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "7280QR-C72M",
    },
    ".1.3.6.1.4.1.30065.1.3011.7280.312.48.2878.6": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "7280TRA-48C6",
    },
    ".1.3.6.1.4.1.30065.1.3011.7280.312.48.2878.6.972": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "7280TRA-48-C6M",
    },
    ".1.3.6.1.4.1.30065.1.3011.7280.3714.64": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "DCS-7280SE-64",
    },
    ".1.3.6.1.4.1.30065.1.3011.7280.3714.68": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "7280SE-68",
    },
    ".1.3.6.1.4.1.30065.1.3011.7280.3714.72": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "7280SE-72",
    },
    ".1.3.6.1.4.1.30065.1.3011.7280.3735.2.48.1654.6": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "7280SR2-48YC6",
    },
    ".1.3.6.1.4.1.30065.1.3011.7280.3735.3.48.1654.8": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "7280SR3-48YC8",
    },
    ".1.3.6.1.4.1.30065.1.3011.7280.3735.48.2878.6": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "7280SR-48-C6",
    },
    ".1.3.6.1.4.1.30065.1.3011.7280.3735.48.2878.6.972": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "7280SR-48-C6M",
    },
    ".1.3.6.1.4.1.30065.1.3011.7280.3977.48.2878.6": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "7280SRAM-48C6",
    },
    ".1.3.6.1.4.1.30065.1.3011.7304": {"manufacturer": "Arista", "platform": "arista_eos", "model": "7304"},
    ".1.3.6.1.4.1.30065.1.3011.7308": {"manufacturer": "Arista", "platform": "arista_eos", "model": "7308"},
    ".1.3.6.1.4.1.30065.1.3011.7316": {"manufacturer": "Arista", "platform": "arista_eos", "model": "7316"},
    ".1.3.6.1.4.1.30065.1.3011.7504": {"manufacturer": "Arista", "platform": "arista_eos", "model": "DCS-7504"},
    ".1.3.6.1.4.1.30065.1.3011.7504.1359": {"manufacturer": "Arista", "platform": "arista_eos", "model": "7504N"},
    ".1.3.6.1.4.1.30065.1.3011.7508": {"manufacturer": "Arista", "platform": "arista_eos", "model": "DCS-7508"},
    ".1.3.6.1.4.1.30065.1.3011.7508.1359": {"manufacturer": "Arista", "platform": "arista_eos", "model": "7508N"},
    ".1.3.6.1.4.1.30065.1.3011.7512.1359": {"manufacturer": "Arista", "platform": "arista_eos", "model": "7512N"},
    ".1.3.6.1.4.1.30065.1.2546.720.858.24.213.4": {
        "manufacturer": "Arista",
        "platform": "arista_eos",
        "model": "CCS-720XP-24ZY4",
    },
}
