# Subject heading clean up

def sh_remove_state_suffix(text: str) -> str:
    return text.replace("Iowa (state)", "Iowa")


def sh_remove_seperator_spaces(text: str) -> str:
    return text.replace(" -- ", "--")


def sh_remove_trailing_semicolon(text: str) -> str:
    return text.replace(";<", "<")