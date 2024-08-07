from enum import StrEnum

from netty_snmp._types import DeviceType
from netty_snmp.device_type.manufactures.a10 import A10_DEVICE_TYPES
from netty_snmp.device_type.manufactures.arista import ARISTA_DEVICE_TYPES
from netty_snmp.device_type.manufactures.aruba import ARUBA_DEVICE_TYPES
from netty_snmp.device_type.manufactures.cisco import CISCO_DEVICE_TYPES
from netty_snmp.device_type.manufactures.extreme import EXTREME_DEVICE_TYPES
from netty_snmp.device_type.manufactures.fortinet import FORTINET_DEVICE_TYPES
from netty_snmp.device_type.manufactures.h3c import H3C_DEVICE_TYPES
from netty_snmp.device_type.manufactures.huawei import HUAWEI_DEVICE_TYPES
from netty_snmp.device_type.manufactures.juniper import JUNIPER_DEVICE_TYPES
from netty_snmp.device_type.manufactures.mikrotik import MIKROTIK_DEVICE_TYPES
from netty_snmp.device_type.manufactures.netgear import NETGEAR_DEVICE_TYPES
from netty_snmp.device_type.manufactures.paloalto import PALOALTO_DEVICE_TYPES
from netty_snmp.device_type.manufactures.ruckus import RUCKUS_DEVICE_TYPES
from netty_snmp.device_type.manufactures.ruijie import RUIJIE_DEVICE_TYPES
from netty_snmp.device_type.manufactures.tp_link import TP_LINK_DEVICE_TYPES
from netty_snmp.device_type.manufactures.zte import ZTE_DEVICE_TYPES
from netty_snmp.factory.consts import UNKNOWN_MODEL, UNKNOWN_PLATFORM


class Manufacturer(StrEnum):
    """default use iana registered enterprise organization name, without suffix and to camel case"""

    Cisco = "Cisco"
    Huawei = "Huawei"
    Aruba = "Aruba"
    Arista = "Arista"
    RuiJie = "Ruijie"
    H3C = "H3C"
    PaloAlto = "PALO ALTO"
    FortiNet = "Fortinet."
    Juniper = "Juniper."
    Netgear = "Netgear"
    TPLink = "TP-Link"
    Ruckus = "Ruckus"
    CheckPoint = "Check Point"
    Sangfor = "Sangfor"
    ZTE = "ZTE"
    A10 = "A10"
    Extreme = "Extreme"
    MikroTik = "MikroTik"


class Platform(StrEnum):
    CiscoIOS = "cisco_ios"
    CiscoIOSXE = "cisco_xe"
    CiscoIOSXR = "cisco_xr"
    CiscoNexusOS = "cisco_nxos"
    CiscoASA = "cisco_asa"
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
    Netgear = "netgear_prosafe"
    TPLink = "tplink_jetstream"
    Ruckus = "ruckus_fastiron"
    Sangfor = "Unknown"
    ZTE = "zte_zxros"
    A10 = "a10"
    Extreme = "extreme"
    MikroTikRouterOS = "mikrotik_routers"
    MikroTikSwitchOS = "mikrotik_switchos"


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
    "4562": Manufacturer.Netgear,
    "11863": Manufacturer.TPLink,
    "25053": Manufacturer.Ruckus,
    "2620": Manufacturer.CheckPoint,
    "30547": Manufacturer.Sangfor,
    "3902": Manufacturer.ZTE,
    "22610": Manufacturer.A10,
    "1916": Manufacturer.Extreme,
    "14988": Manufacturer.MikroTik,
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
    Manufacturer.A10: A10_DEVICE_TYPES,
    Manufacturer.Ruckus: RUCKUS_DEVICE_TYPES,
    Manufacturer.TPLink: TP_LINK_DEVICE_TYPES,
    Manufacturer.Netgear: NETGEAR_DEVICE_TYPES,
    Manufacturer.ZTE: ZTE_DEVICE_TYPES,
    Manufacturer.MikroTik: MIKROTIK_DEVICE_TYPES,
    Manufacturer.Extreme: EXTREME_DEVICE_TYPES,
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
    Manufacturer.Netgear: Platform.Netgear,
    Manufacturer.TPLink: Platform.TPLink,
    Manufacturer.Ruckus: Platform.Ruckus,
}


def _forecast_platform(device_type: DeviceType) -> Platform:
    if device_type.get("platform"):
        return device_type["platform"]  # type: ignore  # noqa: PGH003
    # Optimization: add other platforms forecasting according to model name and vendor
    if device_type["manufacturer"] == Manufacturer.Cisco:
        return _forecast_cisco_platform(device_type)
    if device_type["manufacturer"] == Manufacturer.Huawei:
        return _forecast_huawei_platform(device_type)
    return ManufacturerDefaultPlatform[device_type["manufacturer"]]  # type: ignore  # noqa: PGH003


def _forecast_cisco_platform(device_type: DeviceType) -> Platform:
    if device_type["model"].startswith(("C9", "C38")):
        return Platform.CiscoIOSXE
    if device_type["model"].startswith("N"):
        return Platform.CiscoNexusOS
    if device_type["model"].lower().startswith("isr"):
        return Platform.CiscoIOSXR
    if device_type["model"].lower().startswith("asa"):
        return Platform.CiscoASA
    return Platform.CiscoIOS


def _forecast_huawei_platform(device_type: DeviceType) -> Platform:
    if device_type["model"].startswith("CE") or device_type["model"].startswith("FM"):
        return Platform.HuaweiVRPV8
    return Platform.HuaweiVRP


def _get_manufacturer_platform(device_type: DeviceType) -> DeviceType:
    if not device_type.get("platform"):
        device_type["platform"] = _forecast_platform(device_type)
    return device_type


def get_device_type(sys_object_id: str) -> DeviceType | None:
    private_enterprise_id = sys_object_id.split(".1.3.6.1.4.1.")[1].split(".")[0]
    if private_enterprise_id not in EnterpriseIdManufacturer:
        return None

    device_type = ManufacturerDeviceTypes[EnterpriseIdManufacturer[private_enterprise_id]].get(sys_object_id)
    if not device_type:
        device_type = DeviceType(
            manufacturer=EnterpriseIdManufacturer[private_enterprise_id],
            model=UNKNOWN_MODEL,
            platform=UNKNOWN_PLATFORM,
        )
    return _get_manufacturer_platform(device_type)


def strings_to_dict(strings: str, manufacturer: Manufacturer, platform: Platform) -> dict:
    # basic sysObjectIds data source:
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
