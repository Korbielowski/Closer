def process_string(
    base_string: str, strings: list[str] | tuple[str, ...], sep: str = " "
) -> str:
    """Simple function for joining strings from models."""
    if base_string == "":
        return "Unspecified"
    for string in strings:
        if string != "":
            base_string += sep + string
    return base_string
