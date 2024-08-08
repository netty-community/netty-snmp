import re
from typing import overload

MAC_ADDRESS_LENGTH = 12


@overload
def mac_address_validator(mac: None, strict: bool = False) -> None: ...


@overload
def mac_address_validator(mac: str, strict: bool = False) -> str: ...


@overload
def mac_address_validator(mac: str, strict: bool = True) -> str | None: ...


def mac_address_validator(mac: str | None, strict: bool = False) -> str | None:
    """
    Validates the given MAC address. if given MAC address is not valid, it will be returned as it is.

    Args:
        mac (str): The MAC address to be validated.

    Returns:
        str: The validated MAC address in colon-separated format.
    """
    if mac is None:
        return mac
    _mac_address_re = r"^[0-9a-fA-F]{12}$"
    input_mac = re.sub(r"[^0-9a-fA-F]", "", mac)
    if len(input_mac) != MAC_ADDRESS_LENGTH:
        if not strict:
            return mac
        return None
    if re.match(_mac_address_re, input_mac):
        return ":".join(input_mac[i : i + 2] for i in range(0, len(input_mac), 2)).lower()
    return mac
