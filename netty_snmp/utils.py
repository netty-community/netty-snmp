import re

MAC_ADDRESS_LENGTH = 12


def mac_address_validator(mac: str) -> str:
    """
    Validates the given MAC address.

    Args:
        mac (str): The MAC address to be validated.

    Returns:
        str: The validated MAC address in colon-separated format.

    Raises:
        ValueError: If the MAC address is not in the correct format.
    """
    _mac_address_re = r"^[0-9a-fA-F]{12}$"
    input_mac = re.sub(r"[^0-9a-fA-F]", "", mac)
    if len(input_mac) != MAC_ADDRESS_LENGTH:
        raise ValueError("validation_error.bad_mac_format")
    if re.match(_mac_address_re, input_mac):
        return ":".join(input_mac[i : i + 2] for i in range(0, len(input_mac), 2)).lower()
    raise ValueError("validation_error.bad_mac_format")
