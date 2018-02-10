"""

"""


def sgr(num):
    return '\033[' + str(num) + 'm'


def eightbit_fg(num):
    return '\033[38;5;' + str(num) + 'm'


def eightbit_bg(num):
    return '\033[48;5;' + str(num) + 'm'


def rgb_fg(rgb: tuple):
    return f'\x1b[38;2;{str(rgb[0])};{str(rgb[1])};{str(rgb[2])}m'


def rgb_bg(rgb: tuple):
    return f'\x1b[48;2;{str(rgb[0])};{str(rgb[1])};{str(rgb[2])}m'


