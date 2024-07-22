from enum import StrEnum

from netty_snmp._types import DeviceType
from netty_snmp.device_type.manufactures.arista import ARISTA_DEVICE_TYPES
from netty_snmp.device_type.manufactures.aruba import ARUBA_DEVICE_TYPES
from netty_snmp.device_type.manufactures.cisco import CISCO_DEVICE_TYPES
from netty_snmp.device_type.manufactures.fortinet import FORTINET_DEVICE_TYPES
from netty_snmp.device_type.manufactures.h3c import H3C_DEVICE_TYPES
from netty_snmp.device_type.manufactures.huawei import HUAWEI_DEVICE_TYPES
from netty_snmp.device_type.manufactures.juniper import JUNIPER_DEVICE_TYPES
from netty_snmp.device_type.manufactures.paloalto import PALOALTO_DEVICE_TYPES
from netty_snmp.device_type.manufactures.ruijie import RUIJIE_DEVICE_TYPES


class Manufacturer(StrEnum):
    Cisco = "Cisco"
    Huawei = "Huawei"
    Aruba = "Aruba"
    Arista = "Arista"
    RuiJie = "Ruijie"
    H3C = "H3C"
    PaloAlto = "Palo Alto"
    FortiNet = "FortiNet"
    Juniper = "Juniper"


class Platform(StrEnum):
    CiscoIOS = "cisco_ios"
    CiscoIOSXE = "cisco_xe"
    CiscoIOSXR = "cisco_xr"
    CiscoNexusOS = "cisco_nxos"
    Huawei = "huawei"
    HuaweiVRP = "huawei_vrp"
    HuaweiVRPV8 = "huawei_vrpv8"
    Aruba = "aruba_os"
    ArubaOSSwitch = "aruba_osswitch"
    Arista = "arista_eos"
    RuiJie = "ruijie_os"
    H3C = "hp_comware"
    FortiNet = "fortinet"
    PaloAlto = "paloalto_panos"
    Juniper = "juniper_junos"


EnterpriseIdManufacturer: dict[str, Manufacturer] = {
    "2011": Manufacturer.Huawei,
    "9": Manufacturer.Cisco,
    "14823": Manufacturer.Aruba,
    "30065": Manufacturer.Arista,
    "4881": Manufacturer.RuiJie,
    "61878": Manufacturer.H3C,
    "25461": Manufacturer.PaloAlto,
    "12356": Manufacturer.FortiNet,
    "2636": Manufacturer.Juniper,
}


ManufacturerDeviceTypes = {
    Manufacturer.Cisco: CISCO_DEVICE_TYPES,
    Manufacturer.Huawei: HUAWEI_DEVICE_TYPES,
    Manufacturer.Aruba: ARUBA_DEVICE_TYPES,
    Manufacturer.Arista: ARISTA_DEVICE_TYPES,
    Manufacturer.RuiJie: RUIJIE_DEVICE_TYPES,
    Manufacturer.H3C: H3C_DEVICE_TYPES,
    Manufacturer.PaloAlto: PALOALTO_DEVICE_TYPES,
    Manufacturer.FortiNet: FORTINET_DEVICE_TYPES,
    Manufacturer.Juniper: JUNIPER_DEVICE_TYPES,
}

ManufacturerDefaultPlatform = {
    Manufacturer.Cisco: Platform.CiscoIOS,
    Manufacturer.Huawei: Platform.Huawei,
    Manufacturer.Aruba: Platform.Aruba,
    Manufacturer.Arista: Platform.Arista,
    Manufacturer.RuiJie: Platform.RuiJie,
    Manufacturer.H3C: Platform.H3C,
    Manufacturer.PaloAlto: Platform.PaloAlto,
    Manufacturer.FortiNet: Platform.FortiNet,
    Manufacturer.Juniper: Platform.Juniper,
}


def _forecast_platform(device_type: DeviceType) -> Platform:
    if device_type.get("platform"):
        return device_type["platform"]
    # Optimization: add other platforms forecasting according to model name and vendor
    if device_type["manufacturer"] == Manufacturer.Cisco:
        if device_type["model"].startswith("C9", "C38"):
            device_type["platform"] = Platform.CiscoIOSXE
        elif device_type["model"].startswith("N"):
            device_type["platform"] = Platform.CiscoNexusOS
        elif device_type["model"].lower().startswith("isr"):
            device_type["platform"] = Platform.CiscoIOSXR
        else:
            device_type["platform"] = Platform.CiscoIOS
    if device_type["manufacturer"] == Manufacturer.Huawei:
        if device_type["model"].startswith("CE") or device_type["model"].startswith("FM"):
            device_type["platform"] = Platform.HuaweiVRPV8
        else:
            device_type["platform"] = Platform.HuaweiVRP
    device_type["platform"] = ManufacturerDefaultPlatform[device_type["manufacturer"]]

    return device_type["platform"]


def _get_manufacturer_platform(device_type: DeviceType) -> DeviceType:
    if not device_type.get("platform"):
        device_type["platform"] = _forecast_platform(device_type)
    return device_type


def get_device_type(sys_object_id: str) -> DeviceType | None:
    private_enterprise_id = sys_object_id.split(".")[0]
    if private_enterprise_id not in EnterpriseIdManufacturer:
        return None

    device_type = ManufacturerDeviceTypes[EnterpriseIdManufacturer[private_enterprise_id]].get(sys_object_id)
    return _get_manufacturer_platform(device_type)


def strings_to_dict(strings: str, manufacturer: Manufacturer, platform: Platform) -> dict:
    # basic sysbojectids data source:
    # 1. https://bestmonitoringtools.com/identify-devices-with-snmp-system-oid-sysobjectid-database/
    # 2.
    result = {}
    d1 = [line.split("\t") for line in strings.splitlines() if line]
    for x in d1:
        if len(x) < 3:  # noqa: PLR2004
            continue
        result[x[0]] = {
            "manufacturer": manufacturer,
            "platform": platform,
            "model": x[2],
        }
    return result
