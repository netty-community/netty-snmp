from enum import IntEnum

from netty_snmp._types import SnmpItem

SNMP_DEFAULT_PORT = 161
SNMP_DEFAULT_COMMUNITY = "public"
UNKNOWN_MANUFACTURER = "Unknown"
UNKNOWN_PLATFORM = "Unknown"
UNKNOWN_MODEL = "Unknown"


class SnmpVersion(IntEnum):
    v1 = 1
    v2c = 2
    v3 = 3


class StackRole(IntEnum):
    Master = 1
    Member = 2
    NotMember = 3
    StandBy = 4


INTERFACE_STATUS_MAPPING = {1: "up", 2: "down", 3: "testing"}

LLDP_CHASSIS_ID_SUBTYPE_MAPPING = {
    1: "Chassis Component",
    2: "Interface Alias",
    3: "Port Component",
    4: "MAC Address",
    5: "Network Address",
    6: "Interface Name",
    7: "Local",
}

LLDP_PORT_ID_SUBTYPE_MAPPING = {
    1: "Interface Alias",
    2: "Port Component",
    3: "MAC Address",
    4: "Network Address",
    5: "Interface Name",
    6: "Agent Circuit ID",
    7: "Local",
}

ENTITY_PHYSICAL_CLASS_MAPPING = {
    1: "Other",
    2: "Unknown",
    3: "Chassis",
    4: "Backplane",
    5: "Container",
    6: "PowerSupply",
    7: "Fan",
    8: "Sensor",
    9: "Module",
    10: "Port",
    11: "Stack",
    12: "CPU",
}

HW_STACK_RUN_MAPPING = {1: "enable", 2: "disable"}
HW_STACK_ROLE_MAPPING = {1: "master", 2: "backup", 3: "slave"}


# ---------- system ---------- #

sysObjectID = SnmpItem(
    name="sysDescr",
    oid="1.3.6.1.2.1.1.1.0",
    description="The textual description of the network management subsystem.",
    value_type="str",
    value_mapping=None,
)

sysObjectID = SnmpItem(
    name="sysObjectID",
    oid="1.3.6.1.2.1.1.2",
    description="The vendor's authoritative identification of the network management subsystem contained in the entity.",
    value_type="str",
    value_mapping=None,
)

sysUpTime = SnmpItem(
    name="sysUpTime",
    oid="1.3.6.1.2.1.1.3.0",
    description="The time that the network management subsystem is running.",
    value_type="int",
    value_mapping=None,
)

sysName = SnmpItem(
    name="sysName",
    oid="1.3.6.1.2.1.1.5.0",
    description="The name of the network management subsystem.",
    value_type="str",
    value_mapping=None,
)

# ---------- interface ------------- #
ifIndex = SnmpItem(
    name="ifIndex",
    oid="1.3.6.1.2.1.2.2.1.1",
    description="The ifIndex value for the interface.",
    value_type="int",
    value_mapping=None,
)

ifDescr = SnmpItem(
    name="ifDescr",
    oid="1.3.6.1.2.1.2.2.1.2",
    description="The ifDescr value for the interface.",
    value_type="str",
    value_mapping=None,
)

ifType = SnmpItem(
    name="ifType",
    oid="1.3.6.1.2.1.2.2.1.3",
    description="The ifType value for the interface.",
    value_type="int",
    value_mapping=None,
)

ifMtu = SnmpItem(
    name="ifMtu",
    oid="1.3.6.1.2.1.2.2.1.4",
    description="The ifMtu value for the interface.",
    value_type="int",
    value_mapping=None,
)

ifSpeed = SnmpItem(
    name="ifSpeed",
    oid="1.3.6.1.2.1.2.2.1.5",
    description="The ifSpeed value for the interface.",
    value_type="int",
    value_mapping=None,
)

ifPhysAddr = SnmpItem(
    name="ifPhysAddr",
    oid="1.3.6.1.2.1.2.2.1.6",
    description="The ifPhysAddr value for the interface.",
    value_type="str",
    value_mapping=None,
)

ifAdminStatus = SnmpItem(
    name="ifAdminStatus",
    oid="1.3.6.1.2.1.2.2.1.7",
    description="The ifAdminStatus value for the interface.",
    value_type="int",
    value_mapping={
        1: "up",
        2: "down",
        3: "testing",
    },
)

ifOperStatus = SnmpItem(
    name="ifOperStatus",
    oid="1.3.6.1.2.1.2.2.1.8",
    description="The ifOperStatus value for the interface.",
    value_type="int",
    value_mapping={
        1: "up",
        2: "down",
        3: "testing",
    },
)

ifLastChange = SnmpItem(
    name="ifLastChange",
    oid="1.3.6.1.2.1.2.2.1.9",
    description="The ifLastChange value for the interface.",
    value_type="int",
    value_mapping=None,
)

# ---------- lldp ---------- #

lldpLocChassisId = SnmpItem(
    name="lldpLocChassisId",
    oid="1.0.8802.1.1.2.1.3.2",
    description="The lldpLocChassisId value for the interface.",
    value_type="str",
    value_mapping=None,
    to_hex=True,
)

lldpLocalPortId = SnmpItem(
    name="lldpLocalPortId",
    oid="1.0.8802.1.1.2.1.3.7.1.3",
    description="The lldpLocalPortId value for the interface.",
    value_type="str",
    value_mapping=None,
    to_hex=True,
)

dot1dBasePortIfIndex = SnmpItem(
    name="dot1dBasePortIfIndex",
    oid="1.3.6.1.2.1.17.1.4.1.1",
    description="0	The value of the instance of the ifIndex object,",
    value_type="int",
    value_mapping=None,
)

lldpRemChassisIdSubtype = SnmpItem(
    name="lldpRemChassisIdSubtype",
    oid="1.0.8802.1.1.2.1.4.1.1.4",
    description="The lldpRemChassisIdSubtype value for the interface.",
    value_type="int",
    value_mapping=None,
)

lldpRemChassisId = SnmpItem(
    name="lldpRemChassisId",
    oid="1.0.8802.1.1.2.1.4.1.1.5",
    description="The lldpRemChassisId value for the interface.",
    value_type="str",
    value_mapping=None,
    to_hex=True,
)


lldpRemPortIdSubtype = SnmpItem(
    name="lldpRemPortIdSubtype",
    oid="1.0.8802.1.1.2.1.4.1.1.6",
    description="The lldpRemPortIdSubtype value for the interface.",
    value_type="int",
    value_mapping=None,
)

lldpRemPortId = SnmpItem(
    name="lldpRemPortId",
    oid="1.0.8802.1.1.2.1.4.1.1.7",
    description="The lldpRemPortId value for the interface.",
    value_type="str",
    value_mapping=None,
    to_hex=False,
)

lldpRemPortDesc = SnmpItem(
    name="lldpRemPortDesc",
    oid="1.0.8802.1.1.2.1.4.1.1.8",
    description="The lldpRemPortDesc value for the interface.",
    value_type="str",
    value_mapping=None,
)

lldpRemSysName = SnmpItem(
    name="lldpRemSysName",
    oid="1.0.8802.1.1.2.1.4.1.1.9",
    description="The lldpRemSysName value for the interface.",
    value_type="str",
    value_mapping=None,
)


# ---------- entity ---------- #

entPhysicalDescr = SnmpItem(
    name="entPhysicalDescr",
    oid="1.3.6.1.2.1.47.1.1.1.1.2",
    description="A textual description of physical entity.",
    value_type="str",
    value_mapping=None,
)

entPhysicalClass = SnmpItem(
    name="entPhysicalClass",
    oid="1.3.6.1.2.1.47.1.1.1.1.5",
    description="An indication of the general hardware type of the physical entity.",
    value_type="int",
    value_mapping=ENTITY_PHYSICAL_CLASS_MAPPING,
)
entPhysicalName = SnmpItem(
    name="entPhysicalName",
    oid="1.3.6.1.2.1.47.1.1.1.1.7",
    description="The textual name of the physical entity.",
    value_type="str",
    value_mapping=None,
)

entPhysicalHardwareRev = SnmpItem(
    name="entPhysicalHardwareRev",
    oid="1.3.6.1.2.1.47.1.1.1.1.8",
    description="The hardware revision of the physical entity.",
    value_type="str",
    value_mapping=None,
)
entPhysicalFirmwareRev = SnmpItem(
    name="entPhysicalFirmwareRev",
    oid="1.3.6.1.2.1.47.1.1.1.1.9",
    description="The firmware revision of the physical entity.",
    value_type="str",
    value_mapping=None,
)

entPhysicalSoftwareRev = SnmpItem(
    name="entPhysicalSoftwareRev",
    oid="1.3.6.1.2.1.47.1.1.1.1.10",
    description="The software revision of the physical entity.",
    value_type="str",
    value_mapping=None,
)

entPhysicalSerialNum = SnmpItem(
    name="entPhysicalSerialNum",
    oid="1.3.6.1.2.1.47.1.1.1.1.11",
    description="The serial number of the physical entity.",
    value_type="str",
    value_mapping=None,
)


#  -------- stack -------- #

#   # -------Huawei stack------- #

hwStackRun = SnmpItem(
    name="hwStackRun",
    oid="1.3.6.1.4.1.2011.5.25.183.1.1",
    description="The running status of the Huawei stack.",
    value_type="int",
    value_mapping=HW_STACK_RUN_MAPPING,
)
hwMemberCurrentStackId = SnmpItem(
    name="hwMemberCurrentStackId",
    oid="1.3.6.1.4.1.2011.5.25.183.1.20.1.1",
    description="The current stack ID of the Huawei stack member.",
    value_type="int",  # 0-8
    value_mapping=None,
)
hwMemberStackPriority = SnmpItem(
    name="hwMemberStackPriority",
    oid="1.3.6.1.4.1.2011.5.25.183.1.20.1.2",
    description="The priority of the Huawei stack member.",
    value_type="int",  # 1-255
    value_mapping=None,
)
hwMemberStackRole = SnmpItem(
    name="hwMemberStackRole",
    oid="1.3.6.1.4.1.2011.5.25.183.1.20.1.3",
    description="The role of the Huawei stack member.",
    value_type="int",  # 1-4
    value_mapping=HW_STACK_ROLE_MAPPING,
)
hwMemberStackMacAddress = SnmpItem(
    name="hwMemberStackMacAddress",
    oid="1.3.6.1.4.1.2011.5.25.183.1.20.1.4",
    description="The MAC address of the Huawei stack member.",
    value_type="str",
    value_mapping=None,
)
hwMemberStackDeviceType = SnmpItem(
    name="hwMemberStackDeviceType",
    oid="1.3.6.1.4.1.2011.5.25.183.1.20.1.5",
    description="The device type of the Huawei stack member.",
    value_type="str",
    value_mapping=None,
)

#   # -------Huawei CSS stack------- #

hwCssEnable = SnmpItem(
    name="hwCssEnable",
    oid="1.3.6.1.4.1.2011.5.25.183.1.1",
    description="The enable status of the Huawei CSS stack.",
    value_type="int",
    value_mapping=HW_STACK_RUN_MAPPING,
)

hwCssMemberFrameId = SnmpItem(
    name="hwCssMemberFrameId",
    oid="1.3.6.1.4.1.2011.5.25.183.3.2.1.1",
    description="The frame ID of the Huawei CSS stack member.",
    value_type="int",
    value_mapping=None,
)
hwCssMemberRole = SnmpItem(
    name="hwCssMemberRole",
    oid="1.3.6.1.4.1.2011.5.25.183.3.2.1.8",
    description="The role of the Huawei CSS stack member.",
    value_type="int",
    value_mapping=HW_STACK_ROLE_MAPPING,
)

hwCssMemberPriority = SnmpItem(
    name="hwCssMemberPriority",
    oid="1.3.6.1.4.1.2011.5.25.183.3.2.1.3",
    description="The priority of the Huawei CSS stack member.",
    value_type="int",
    value_mapping=None,
)
hwCssMemberConfigPriority = SnmpItem(
    name="hwCssMemberConfigPriority",
    oid="1.3.6.1.4.1.2011.5.25.183.3.2.1.4",
    description="The config priority of the Huawei CSS stack member.",
    value_type="int",
    value_mapping=None,
)

# -------- stack Cisco ------- #
cswSwitchRole = SnmpItem(
    name="cswSwitchRole",
    oid="1.3.6.1.4.1.9.9.500.1.2.1.1.3",
    description="The role of the Cisco switch.",
    value_type="int",
    value_mapping=HW_STACK_ROLE_MAPPING,
)

cswSwitchHwPriority = SnmpItem(
    name="cswSwitchHwPriority",
    oid="1.3.6.1.4.1.9.9.500.1.2.1.1.5",
    description="The hardware priority of the Cisco switch.",
    value_type="int",
    value_mapping=None,
)
cswSwitchState = SnmpItem(
    name="cswSwitchState",
    oid="1.3.6.1.4.1.9.9.500.1.2.1.1.6",
    description="The state of the Cisco switch.",
    value_type="int",
    value_mapping=HW_STACK_RUN_MAPPING,
)

cswSwitchMacAddress = SnmpItem(
    name="cswSwitchMacAddress",
    oid="1.3.6.1.4.1.9.9.500.1.2.1.1.7",
    description="The MAC address of the Cisco switch.",
    value_type="str",
    value_mapping=None,
)


panSysSwVersion = SnmpItem(
    name="panSysSwVersion",
    oid="1.3.6.1.4.1.25461.2.1.2.1.1",
    description="The version of the PAN-OS software.",
    value_type="str",
    value_mapping=None,
)
panSysSerialNumber = SnmpItem(
    name="panSysSerialNumber",
    oid="1.3.6.1.4.1.25461.2.1.2.1.3",
    description="The serial number of the PAN-OS.",
    value_type="str",
    value_mapping=None,
)

sysExtSwitchSWVersion = SnmpItem(
    name="sysExtSwitchSWVersion",
    oid="1.3.6.1.4.1.14823.2.2.1.2.1.19.1.4",
    description="The version of the external switch software.",
    value_type="str",
    value_mapping=None,
)

sysExtSwitchSetNo = SnmpItem(
    name="sysExtSwitchSetNo",
    oid="1.3.6.1.4.1.14823.2.2.1.2.1.19.1.7",
    description="The serial number of the external switch.",
    value_type="str",
    value_mapping=None,
)
