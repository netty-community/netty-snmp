# Network Device information Discovery via SNMP

Netty_snmp is a flexible,powerful,high performance tool for network device information collection.
It will recognize network device's manufacture and platform(netmiko driver) automatically through
SNMP `SysObjectId` and collect a lot of network basic information with friendly output format and
exceptions traceback.
> Inspirations of SNMP and why not command line tools(CLI)
CLI output is un-structure data, we need use regex/textfsm liked tools to extract the information
from network device output. It's very painful to maintain the string-based regex code and very hard to
extend. SNMP is fast, stable to get and all data is structured which is easy to handle by code, also it's
much easier to maintain the codebase, some of items is generic for all network manufacturers, such
as interface, hostname, lldp neighbors. One time coding and support all vendors, fancy, right?
So, personally use snmp to collect basic information of network device is a better choice than CLI.


## Installation Guide
> soon coming

## Examples
1. scanning a prefix via SNMPv2 and discovery all network device items
```python
from netty_snmp import DispatchSnmpFactory, consts

dis = DispatchSnmpFactory(
    prefix="192.168.0.0/24",
    port=161,
    version=consts.SnmpVersion.v2c, # via snmp v2c
    community="public",
    max_workers=16, # concurrency for collection task, run in 16 threads
)
print(dis.discovery())
```
2. scanning a ip address via SNMPv2 and discovery partial items, in this example: only hostname and interfaces will be collected.
```python
dis = DispatchSnmpFactory(
    prefix="192.168.0.0/32",
    port=161,
    version=consts.SnmpVersion.v2c, # via snmp v2c
    community="public",
    max_workers=16, # concurrency for collection task, run in 16 threads
)
print(dis.discovery(["hostname", "interfaces"]))

3. scanning via SNMPv3
```python
DispatchSnmpFactory(
    prefix="192.168.0.0/24",
    port=161,
    version=consts.SnmpVersion.v3,
    v3_params=SnmpV3Params(
        security_username="admin",
        security_level="authNoPriv",
        auth_protocol="md5",
        auth_password="admin",
        context_engine_id="0000000000000000",
        privacy_protocol="des",
        privacy_password="admin",
    ),
    max_workers=16,
)
print(dis.discovery())
```
---
## Main Support Items
- **Hostname**: the hostname of network device
- **System Description**: the textual information of the system: include model name, software version, hardware version and etc.
- **Uptime**: network device uptime
- **ChassisID**: the mac address of chassis, the unique identifier of chassis
- **Interfaces**: interface full information
  - Interface Index
  - Interface Name
  - Interface Description
  - Interface Mtu
  - Interface Speed: physical speed
  - Interface High Speed: negotiation speed
  - Interface Type
  - Interface Mac Address
  - Interface Admin status
  - Interface Operational Status
  - Interface IP Addresses: (L3 Interface)
  - Interface Port Mode: access/trunk/hybrid ...
- **LLDP Neighbors**: lldp information will local and remote connection info
  - Local Chassis Id: the unique identifier mac address of chassis
  - Local Hostname: the hostname of local device
  - Local Interface Name
  - Local Interface Description
  - Remote Chassis Id: the unique identifier mac address of lldp neighbor chassis
  - Remote Hostname: the hostname of lldp neighbor
  - Remote Interface Name: the interface name of lldp neighbor
  - Remote interface Description: the interface description of lldp neighbor

- **Entities**
  - Entity Physical Description: the mode information of entity
  - Entity Physical Name: the name of entity
  - Entity Software revision: software version
  - Entity Serial Number: the serial number of entity
---
> waiting for implement
- **VLANS**
- **StackWise**
- **Prefixes**
- **ARP Table**
- **Mac Address Table**
- **Routing table**

---
## Main support manufactures
### well tested
- Cisco
- Huawei
- Aruba
### basic tested
- H3C
- Ruijie
- Arista
- Fortinet
- PaloAlto
- Juniper


## Development Guide
1. install [rye](https://rye.astral.sh/guide/installation/) for python project management
2. execute `rye sync` to install dependencies
3. execute `pre-commit install` for lint and pytest hooks
4. perform you code changes and execute `pre-commit` to do static code check and unit test.
5. push changes to the codebase.
