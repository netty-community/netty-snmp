from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from netty_snmp._types import DeviceType

ARUBA_DEVICE_TYPES: dict[str, "DeviceType"] = {
    ".1.3.6.1.4.1.14823.1.1.1": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "5000"},
    ".1.3.6.1.4.1.14823.1.1.10": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "200"},
    ".1.3.6.1.4.1.14823.1.1.11": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "2424"},
    ".1.3.6.1.4.1.14823.1.1.12": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "ARUBA 6000-SC3"},
    ".1.3.6.1.4.1.14823.1.1.13": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "3200"},
    ".1.3.6.1.4.1.14823.1.1.14": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "3200-8"},
    ".1.3.6.1.4.1.14823.1.1.15": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "3400"},
    ".1.3.6.1.4.1.14823.1.1.16": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "3400-32"},
    ".1.3.6.1.4.1.14823.1.1.17": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "3600"},
    ".1.3.6.1.4.1.14823.1.1.18": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "3600-64"},
    ".1.3.6.1.4.1.14823.1.1.19": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "650-US"},
    ".1.3.6.1.4.1.14823.1.1.2": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "2400"},
    ".1.3.6.1.4.1.14823.1.1.20": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "651"},
    ".1.3.6.1.4.1.14823.1.1.23": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "620"},
    ".1.3.6.1.4.1.14823.1.1.24": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "ARUBA S3500-24P"},
    ".1.3.6.1.4.1.14823.1.1.25": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "ARUBA S3500-24T"},
    ".1.3.6.1.4.1.14823.1.1.26": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "S3500-48P"},
    ".1.3.6.1.4.1.14823.1.1.27": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "ARUBA S3500-48T"},
    ".1.3.6.1.4.1.14823.1.1.28": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "ARUBA S2500-24P"},
    ".1.3.6.1.4.1.14823.1.1.29": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "ARUBA S2500-24T"},
    ".1.3.6.1.4.1.14823.1.1.3": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "800"},
    ".1.3.6.1.4.1.14823.1.1.30": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "ARUBA S2500-48P"},
    ".1.3.6.1.4.1.14823.1.1.31": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "ARUBA S2500-48T"},
    ".1.3.6.1.4.1.14823.1.1.32": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "7210"},
    ".1.3.6.1.4.1.14823.1.1.33": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "7220"},
    ".1.3.6.1.4.1.14823.1.1.34": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "7240"},
    ".1.3.6.1.4.1.14823.1.1.35": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "ARUBA S3500-24F"},
    ".1.3.6.1.4.1.14823.1.1.36": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "ARUBA S1500-48P"},
    ".1.3.6.1.4.1.14823.1.1.37": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "ARUBA S1500-24P"},
    ".1.3.6.1.4.1.14823.1.1.38": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "S1500-12P"},
    ".1.3.6.1.4.1.14823.1.1.39": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "7005"},
    ".1.3.6.1.4.1.14823.1.1.4": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "6000"},
    ".1.3.6.1.4.1.14823.1.1.40": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "7010-US"},
    ".1.3.6.1.4.1.14823.1.1.41": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "7030"},
    ".1.3.6.1.4.1.14823.1.1.42": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "7205"},
    ".1.3.6.1.4.1.14823.1.1.43": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "ARUBA A7024"},
    ".1.3.6.1.4.1.14823.1.1.44": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "ARUBA A7105"},
    ".1.3.6.1.4.1.14823.1.1.45": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "ARUBA A9900"},
    ".1.3.6.1.4.1.14823.1.1.46": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "ARUBA A9980"},
    ".1.3.6.1.4.1.14823.1.1.47": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "7240XM"},
    ".1.3.6.1.4.1.14823.1.1.48": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "7008"},
    ".1.3.6.1.4.1.14823.1.1.5": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "2450"},
    ".1.3.6.1.4.1.14823.1.1.50": {
        "manufacturer": "Aruba",
        "platform": "aruba_os",
        "model": "MOBILITY MASTER VIRTUAL APPLIANCE",
    },
    ".1.3.6.1.4.1.14823.1.1.52": {
        "manufacturer": "Aruba",
        "platform": "aruba_os",
        "model": "MOBILITY CONTROLLER VIRTUAL APPLIANCE",
    },
    ".1.3.6.1.4.1.14823.1.1.54": {
        "manufacturer": "Aruba",
        "platform": "aruba_os",
        "model": "MOBILITY MASTER VIRTUAL APPLIANCE",
    },
    ".1.3.6.1.4.1.14823.1.1.55": {
        "manufacturer": "Aruba",
        "platform": "aruba_os",
        "model": "MOBILITY MASTER VIRTUAL APPLIANCE",
    },
    ".1.3.6.1.4.1.14823.1.1.6": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "850"},
    ".1.3.6.1.4.1.14823.1.1.7": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "2400E"},
    ".1.3.6.1.4.1.14823.1.1.8": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "800E"},
    ".1.3.6.1.4.1.14823.1.1.9": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "804"},
    ".1.3.6.1.4.1.14823.1.1.99": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "2400-F"},
    ".1.3.6.1.4.1.14823.1.1.9999": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "6000"},
    ".1.3.6.1.4.1.14823.1.2.1": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "ARUBA A50"},
    ".1.3.6.1.4.1.14823.1.2.10": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "ARUBA AP-80M"},
    ".1.3.6.1.4.1.14823.1.2.102": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "AP-535"},
    ".1.3.6.1.4.1.14823.1.2.107": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "IAP-515"},
    ".1.3.6.1.4.1.14823.1.2.11": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "ARUBA AP-WG102"},
    ".1.3.6.1.4.1.14823.1.2.111": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "AP-505"},
    ".1.3.6.1.4.1.14823.1.2.114": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "AP-575"},
    ".1.3.6.1.4.1.14823.1.2.115": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "AP-577"},
    ".1.3.6.1.4.1.14823.1.2.12": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "ARUBA AP-40"},
    ".1.3.6.1.4.1.14823.1.2.13": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "ARUBA AP-41"},
    ".1.3.6.1.4.1.14823.1.2.14": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "ARUBA AP-65"},
    ".1.3.6.1.4.1.14823.1.2.15": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "ARUBA AP-MW1700"},
    ".1.3.6.1.4.1.14823.1.2.16": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "ARUBA AP-DUOWJ"},
    ".1.3.6.1.4.1.14823.1.2.17": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "ARUBA AP-DUO"},
    ".1.3.6.1.4.1.14823.1.2.18": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "ARUBA AP-80MB"},
    ".1.3.6.1.4.1.14823.1.2.19": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "ARUBA AP-80SB"},
    ".1.3.6.1.4.1.14823.1.2.2": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "ARUBA A52"},
    ".1.3.6.1.4.1.14823.1.2.20": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "ARUBA AP-85"},
    ".1.3.6.1.4.1.14823.1.2.21": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "ARUBA AP-124"},
    ".1.3.6.1.4.1.14823.1.2.22": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "ARUBA AP-125"},
    ".1.3.6.1.4.1.14823.1.2.23": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "ARUBA AP-120"},
    ".1.3.6.1.4.1.14823.1.2.24": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "ARUBA AP-121"},
    ".1.3.6.1.4.1.14823.1.2.25": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "ARUBA AP-1250"},
    ".1.3.6.1.4.1.14823.1.2.26": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "ARUBA AP-120ABG"},
    ".1.3.6.1.4.1.14823.1.2.27": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "ARUBA AP-121ABG"},
    ".1.3.6.1.4.1.14823.1.2.28": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "ARUBA AP-124ABG"},
    ".1.3.6.1.4.1.14823.1.2.29": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "ARUBA AP-125ABG"},
    ".1.3.6.1.4.1.14823.1.2.3": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "ARUBA AP-60"},
    ".1.3.6.1.4.1.14823.1.2.30": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "ARUBA RAP-5WN"},
    ".1.3.6.1.4.1.14823.1.2.31": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "ARUBA RAP-5"},
    ".1.3.6.1.4.1.14823.1.2.32": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "ARUBA RAP-2WG"},
    ".1.3.6.1.4.1.14823.1.2.33": {
        "manufacturer": "Aruba",
        "platform": "aruba_os",
        "model": "ARUBA RESERVED4 ACCESS POINT",
    },
    ".1.3.6.1.4.1.14823.1.2.34": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "IAP-105"},
    ".1.3.6.1.4.1.14823.1.2.35": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "ARUBA AP-65WB"},
    ".1.3.6.1.4.1.14823.1.2.36": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "ARUBA AP-651"},
    ".1.3.6.1.4.1.14823.1.2.37": {
        "manufacturer": "Aruba",
        "platform": "aruba_os",
        "model": "ARUBA RESERVED6 ACCESS POINT",
    },
    ".1.3.6.1.4.1.14823.1.2.38": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "ARUBA AP-60P"},
    ".1.3.6.1.4.1.14823.1.2.39": {
        "manufacturer": "Aruba",
        "platform": "aruba_os",
        "model": "ARUBA RESERVED7 ACCESS POINT",
    },
    ".1.3.6.1.4.1.14823.1.2.4": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "ARUBA AP-61"},
    ".1.3.6.1.4.1.14823.1.2.40": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "ARUBA IAP-92"},
    ".1.3.6.1.4.1.14823.1.2.41": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "ARUBA IAP-93"},
    ".1.3.6.1.4.1.14823.1.2.42": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "ARUBA AP-68"},
    ".1.3.6.1.4.1.14823.1.2.43": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "ARUBA AP-68P"},
    ".1.3.6.1.4.1.14823.1.2.44": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "ARUBA AP-175P"},
    ".1.3.6.1.4.1.14823.1.2.45": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "ARUBA AP-175AC"},
    ".1.3.6.1.4.1.14823.1.2.46": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "ARUBA AP-175DC"},
    ".1.3.6.1.4.1.14823.1.2.47": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "IAP-134"},
    ".1.3.6.1.4.1.14823.1.2.48": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "IAP-135"},
    ".1.3.6.1.4.1.14823.1.2.49": {
        "manufacturer": "Aruba",
        "platform": "aruba_os",
        "model": "ARUBA RESERVED8 ACCESS POINT",
    },
    ".1.3.6.1.4.1.14823.1.2.5": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "ARUBA AP-70"},
    ".1.3.6.1.4.1.14823.1.2.50": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "ARUBA AP-93H"},
    ".1.3.6.1.4.1.14823.1.2.51": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "ARUBA RAP-3WN"},
    ".1.3.6.1.4.1.14823.1.2.52": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "ARUBA RAP-3WNP"},
    ".1.3.6.1.4.1.14823.1.2.53": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "IAP-104"},
    ".1.3.6.1.4.1.14823.1.2.54": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "ARUBA RAP-155"},
    ".1.3.6.1.4.1.14823.1.2.55": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "ARUBA RAP-155P"},
    ".1.3.6.1.4.1.14823.1.2.56": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "ARUBA RAP-108"},
    ".1.3.6.1.4.1.14823.1.2.57": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "ARUBA RAP-109"},
    ".1.3.6.1.4.1.14823.1.2.58": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "IAP-224"},
    ".1.3.6.1.4.1.14823.1.2.59": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "IAP-225"},
    ".1.3.6.1.4.1.14823.1.2.6": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "ARUBA AP-61-WJ"},
    ".1.3.6.1.4.1.14823.1.2.60": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "IAP-114"},
    ".1.3.6.1.4.1.14823.1.2.61": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "IAP-115"},
    ".1.3.6.1.4.1.14823.1.2.62": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "ARUBA RAP-109L"},
    ".1.3.6.1.4.1.14823.1.2.63": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "IAP-274"},
    ".1.3.6.1.4.1.14823.1.2.64": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "IAP-275"},
    ".1.3.6.1.4.1.14823.1.2.65": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "ARUBA AP-214A"},
    ".1.3.6.1.4.1.14823.1.2.66": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "ARUBA AP-215A"},
    ".1.3.6.1.4.1.14823.1.2.67": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "IAP-204"},
    ".1.3.6.1.4.1.14823.1.2.68": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "IAP-205"},
    ".1.3.6.1.4.1.14823.1.2.69": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "IAP-103"},
    ".1.3.6.1.4.1.14823.1.2.7": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "ARUBA A2E"},
    ".1.3.6.1.4.1.14823.1.2.70": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "ARUBA AP-103H"},
    ".1.3.6.1.4.1.14823.1.2.71": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "IAP VIRTUAL CONTROLLER"},
    ".1.3.6.1.4.1.14823.1.2.72": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "ARUBA AP-277"},
    ".1.3.6.1.4.1.14823.1.2.73": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "IAP-214"},
    ".1.3.6.1.4.1.14823.1.2.74": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "IAP-215"},
    ".1.3.6.1.4.1.14823.1.2.75": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "IAP-228"},
    ".1.3.6.1.4.1.14823.1.2.76": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "IAP-205H"},
    ".1.3.6.1.4.1.14823.1.2.77": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "IAP-324"},
    ".1.3.6.1.4.1.14823.1.2.78": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "IAP-325"},
    ".1.3.6.1.4.1.14823.1.2.79": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "IAP-334"},
    ".1.3.6.1.4.1.14823.1.2.8": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "ARUBA AP-1200"},
    ".1.3.6.1.4.1.14823.1.2.80": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "IAP-335"},
    ".1.3.6.1.4.1.14823.1.2.81": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "IAP-314"},
    ".1.3.6.1.4.1.14823.1.2.82": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "IAP-315"},
    ".1.3.6.1.4.1.14823.1.2.84": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "IAP-207"},
    ".1.3.6.1.4.1.14823.1.2.85": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "IAP-304"},
    ".1.3.6.1.4.1.14823.1.2.86": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "IAP-305"},
    ".1.3.6.1.4.1.14823.1.2.87": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "IAP-303H"},
    ".1.3.6.1.4.1.14823.1.2.88": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "IAP-365"},
    ".1.3.6.1.4.1.14823.1.2.9": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "ARUBA AP-80S"},
    ".1.3.6.1.4.1.14823.1.2.9999": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "ARUBA AP-UNDEFINED"},
    ".1.3.6.1.4.1.14823.1.3.1": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "ZMASTER"},
    ".1.3.6.1.4.1.14823.1.6.1": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "C2000"},
    ".1.3.6.1.4.1.14823.1.1.59": {"manufacturer": "Aruba", "platform": "aruba_os", "model": "Aruba9240"},
}
