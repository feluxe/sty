"""

"""


def sgr(num):
    return '\033[' + str(num) + 'm'


def eightbit_fg(num):
    return '\033[38;5;' + str(num) + 'm'


def eightbit_bg(num):
    return '\033[48;5;' + str(num) + 'm'


def rgb_fg(rgb: tuple):
    r = str(rgb[0])
    g = str(rgb[1])
    b = str(rgb[2])
    return '\x1b[38;2;' + r + ';' + g + ';' + b + 'm'


def rgb_bg(rgb: tuple):
    r = str(rgb[0])
    g = str(rgb[1])
    b = str(rgb[2])
    return '\x1b[48;2;' + r + ';' + g + ';' + b + 'm'
