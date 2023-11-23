"""
A selection of render functions.

These functions generate the escape-sequences that trigger certain colors/effects in
the terminals.
"""


def sgr(num: int) -> str:
    """
    Create a SGR escape sequence.
    """
    return "\033[" + str(num) + "m"


def eightbit_fg(num: int) -> str:
    """
    Create a 8bit (256-color) foreground escape sequence.
    """
    return "\033[38;5;" + str(num) + "m"


def eightbit_bg(num: int) -> str:
    """
    Create a 8bit (256-color) background escape sequence.
    """
    return "\033[48;5;" + str(num) + "m"


def rgb_fg(r: int, g: int, b: int) -> str:
    """
    Create a 24bit (true color) foreground escape sequence.
    """
    return "\x1b[38;2;" + str(r) + ";" + str(g) + ";" + str(b) + "m"


def rgb_bg(r: int, g: int, b: int) -> str:
    """
    Create a 24bit (true color) background escape sequence.
    """
    return "\x1b[48;2;" + str(r) + ";" + str(g) + ";" + str(b) + "m"
