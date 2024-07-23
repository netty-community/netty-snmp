from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from netty_snmp._types import DeviceType

PALOALTO_DEVICE_TYPES: dict[str, "DeviceType"] = {
    ".1.3.6.1.4.1.25461.2.3.1": {"manufacturer": "Palo Alto", "platform": "paloalto_panos", "model": "PA-4050"},
    ".1.3.6.1.4.1.25461.2.3.11": {"manufacturer": "Palo Alto", "platform": "paloalto_panos", "model": "PA-5020"},
    ".1.3.6.1.4.1.25461.2.3.12": {"manufacturer": "Palo Alto", "platform": "paloalto_panos", "model": "PA-200"},
    ".1.3.6.1.4.1.25461.2.3.17": {"manufacturer": "Palo Alto", "platform": "paloalto_panos", "model": "PA-3050"},
    ".1.3.6.1.4.1.25461.2.3.18": {"manufacturer": "Palo Alto", "platform": "paloalto_panos", "model": "PA-3020"},
    ".1.3.6.1.4.1.25461.2.3.19": {"manufacturer": "Palo Alto", "platform": "paloalto_panos", "model": "PA-3060"},
    ".1.3.6.1.4.1.25461.2.3.2": {"manufacturer": "Palo Alto", "platform": "paloalto_panos", "model": "PA-4020"},
    ".1.3.6.1.4.1.25461.2.3.21": {"manufacturer": "Palo Alto", "platform": "paloalto_panos", "model": "PA-3250"},
    ".1.3.6.1.4.1.25461.2.3.22": {"manufacturer": "Palo Alto", "platform": "paloalto_panos", "model": "PA-5260"},
    ".1.3.6.1.4.1.25461.2.3.23": {"manufacturer": "Palo Alto", "platform": "paloalto_panos", "model": "PA-5250"},
    ".1.3.6.1.4.1.25461.2.3.24": {"manufacturer": "Palo Alto", "platform": "paloalto_panos", "model": "PA-5220"},
    ".1.3.6.1.4.1.25461.2.3.29": {"manufacturer": "Palo Alto", "platform": "paloalto_panos", "model": "PA-VM"},
    ".1.3.6.1.4.1.25461.2.3.3": {"manufacturer": "Palo Alto", "platform": "paloalto_panos", "model": "PA-2050"},
    ".1.3.6.1.4.1.25461.2.3.30": {"manufacturer": "Palo Alto", "platform": "paloalto_panos", "model": "M-100"},
    ".1.3.6.1.4.1.25461.2.3.31": {"manufacturer": "Palo Alto", "platform": "paloalto_panos", "model": "PA-7050"},
    ".1.3.6.1.4.1.25461.2.3.32": {
        "manufacturer": "Palo Alto",
        "platform": "paloalto_panos",
        "model": "PALO ALTO GP-100",
    },
    ".1.3.6.1.4.1.25461.2.3.33": {"manufacturer": "Palo Alto", "platform": "paloalto_panos", "model": "WF-500"},
    ".1.3.6.1.4.1.25461.2.3.34": {"manufacturer": "Palo Alto", "platform": "paloalto_panos", "model": "PA-7080"},
    ".1.3.6.1.4.1.25461.2.3.35": {"manufacturer": "Palo Alto", "platform": "paloalto_panos", "model": "M-500"},
    ".1.3.6.1.4.1.25461.2.3.36": {"manufacturer": "Palo Alto", "platform": "paloalto_panos", "model": "PA-820"},
    ".1.3.6.1.4.1.25461.2.3.37": {"manufacturer": "Palo Alto", "platform": "paloalto_panos", "model": "PA-850"},
    ".1.3.6.1.4.1.25461.2.3.38": {"manufacturer": "Palo Alto", "platform": "paloalto_panos", "model": "PA-220"},
    ".1.3.6.1.4.1.25461.2.3.39": {"manufacturer": "Palo Alto", "platform": "paloalto_panos", "model": "M-600"},
    ".1.3.6.1.4.1.25461.2.3.4": {"manufacturer": "Palo Alto", "platform": "paloalto_panos", "model": "PA-2020"},
    ".1.3.6.1.4.1.25461.2.3.40": {"manufacturer": "Palo Alto", "platform": "paloalto_panos", "model": "M-200"},
    ".1.3.6.1.4.1.25461.2.3.41": {"manufacturer": "Palo Alto", "platform": "paloalto_panos", "model": "PA-220R"},
    ".1.3.6.1.4.1.25461.2.3.42": {"manufacturer": "Palo Alto", "platform": "paloalto_panos", "model": "PA-5280"},
    ".1.3.6.1.4.1.25461.2.3.43": {"manufacturer": "Palo Alto", "platform": "paloalto_panos", "model": "PA-3220"},
    ".1.3.6.1.4.1.25461.2.3.44": {"manufacturer": "Palo Alto", "platform": "paloalto_panos", "model": "PA-3260"},
    ".1.3.6.1.4.1.25461.2.3.5": {"manufacturer": "Palo Alto", "platform": "paloalto_panos", "model": "PA-4060"},
    ".1.3.6.1.4.1.25461.2.3.6": {"manufacturer": "Palo Alto", "platform": "paloalto_panos", "model": "PA-500"},
    ".1.3.6.1.4.1.25461.2.3.7": {"manufacturer": "Palo Alto", "platform": "paloalto_panos", "model": "PANORAMA"},
    ".1.3.6.1.4.1.25461.2.3.8": {"manufacturer": "Palo Alto", "platform": "paloalto_panos", "model": "PA-5060"},
    ".1.3.6.1.4.1.25461.2.3.9": {"manufacturer": "Palo Alto", "platform": "paloalto_panos", "model": "PA-5050"},
}
