"""
These are the default registers that sty provides out of the box.
"""
from . import renderfunc
from .primitive import Base
from .rendertype import *


class EfRegister(Base):

    rules: dict = {}

    b: str
    bold: str
    dim: str
    i: str
    italic: str
    u: str
    underl: str
    blink: str
    inverse: str
    hidden: str
    strike: str

    def __init__(self):

        self.set_renderfunc(Sgr, renderfunc.sgr)

        self.set_style('b', Sgr(1))
        self.set_style('bold', Sgr(1))
        self.set_style('dim', Sgr(2))
        self.set_style('i', Sgr(3))
        self.set_style('italic', Sgr(3))
        self.set_style('u', Sgr(4))
        self.set_style('underl', Sgr(4))
        self.set_style('blink', Sgr(5))
        self.set_style('inverse', Sgr(7))
        self.set_style('hidden', Sgr(8))
        self.set_style('strike', Sgr(9))


class FgRegister(Base):

    black: str
    red: str
    green: str
    yellow: str
    blue: str
    magenta: str
    cyan: str
    white: str

    rs: str

    li_black: str
    li_red: str
    li_green: str
    li_yellow: str
    li_blue: str
    li_magenta: str
    li_cyan: str
    li_white: str

    da_black: str
    da_red: str
    da_green: str
    da_yellow: str
    da_blue: str
    da_magenta: str
    da_cyan: str
    da_white: str

    def __init__(self):

        self.set_renderfunc(Sgr, renderfunc.sgr)
        self.set_renderfunc(EightbitFg, renderfunc.eightbit_fg)
        self.set_renderfunc(RgbFg, renderfunc.rgb_fg)

        self.set_eightbit_call(EightbitFg)
        self.set_rgb_call(RgbFg)

        # Classic terminal foreground color preset.
        # These are well supported.
        self.set_style('black', Sgr(30))
        self.set_style('red', Sgr(31))
        self.set_style('green', Sgr(32))
        self.set_style('yellow', Sgr(33))
        self.set_style('blue', Sgr(34))
        self.set_style('magenta', Sgr(35))
        self.set_style('cyan', Sgr(36))
        self.set_style('white', Sgr(37))

        self.set_style('rs', Sgr(39))

        # These are less good supported.
        self.set_style('li_black', Sgr(90))
        self.set_style('li_red', Sgr(91))
        self.set_style('li_green', Sgr(92))
        self.set_style('li_yellow', Sgr(93))
        self.set_style('li_blue', Sgr(94))
        self.set_style('li_magenta', Sgr(95))
        self.set_style('li_cyan', Sgr(96))
        self.set_style('li_white', Sgr(97))

        # These are less supported.
        self.set_style('da_black', EightbitFg(0))
        self.set_style('da_red', EightbitFg(88))
        self.set_style('da_green', EightbitFg(22))
        self.set_style('da_yellow', EightbitFg(58))
        self.set_style('da_blue', EightbitFg(18))
        self.set_style('da_magenta', EightbitFg(89))
        self.set_style('da_cyan', EightbitFg(23))
        self.set_style('da_white', EightbitFg(249))


class BgRegister(Base):

    black: str
    red: str
    green: str
    yellow: str
    blue: str
    magenta: str
    cyan: str
    white: str

    rs: str

    li_black: str
    li_red: str
    li_green: str
    li_yellow: str
    li_blue: str
    li_magenta: str
    li_cyan: str
    li_white: str

    da_black: str
    da_red: str
    da_green: str
    da_yellow: str
    da_blue: str
    da_magenta: str
    da_cyan: str
    da_white: str

    def __init__(self):

        self.set_renderfunc(Sgr, renderfunc.sgr)
        self.set_renderfunc(EightbitBg, renderfunc.eightbit_bg)
        self.set_renderfunc(RgbBg, renderfunc.rgb_bg)

        self.set_eightbit_call(EightbitBg)
        self.set_rgb_call(RgbBg)

        # Classic terminal background color preset.
        # These are well supported.
        self.set_style('black', Sgr(40))
        self.set_style('red', Sgr(41))
        self.set_style('green', Sgr(42))
        self.set_style('yellow', Sgr(43))
        self.set_style('blue', Sgr(44))
        self.set_style('magenta', Sgr(45))
        self.set_style('cyan', Sgr(46))
        self.set_style('white', Sgr(47))

        self.set_style('rs', Sgr(49))

        # These are less good supported.
        self.set_style('li_black', Sgr(100))
        self.set_style('li_red', Sgr(101))
        self.set_style('li_green', Sgr(102))
        self.set_style('li_yellow', Sgr(103))
        self.set_style('li_blue', Sgr(104))
        self.set_style('li_magenta', Sgr(105))
        self.set_style('li_cyan', Sgr(106))
        self.set_style('li_white', Sgr(107))

        # These are less supported.
        self.set_style('da_black', EightbitBg(0))
        self.set_style('da_red', EightbitBg(88))
        self.set_style('da_green', EightbitBg(22))
        self.set_style('da_yellow', EightbitBg(58))
        self.set_style('da_blue', EightbitBg(18))
        self.set_style('da_magenta', EightbitBg(89))
        self.set_style('da_cyan', EightbitBg(23))
        self.set_style('da_white', EightbitBg(249))


class RsRegister(Base):

    all: str
    fg: str
    bg: str
    bold_dim: str
    dim_bold: str
    i: str
    italic: str
    u: str
    underl: str
    blink: str
    inverse: str
    hidden: str
    strike: str

    def __init__(self):

        self.set_renderfunc(Sgr, renderfunc.sgr)

        self.set_style('all', Sgr(0))
        self.set_style('fg', Sgr(39))
        self.set_style('bg', Sgr(49))

        self.set_style('bold_dim', Sgr(22))
        self.set_style('dim_bold', Sgr(22))
        self.set_style('i', Sgr(23))
        self.set_style('italic', Sgr(23))
        self.set_style('u', Sgr(24))
        self.set_style('underl', Sgr(24))
        self.set_style('blink', Sgr(25))
        self.set_style('inverse', Sgr(27))
        self.set_style('hidden', Sgr(28))
        self.set_style('strike', Sgr(29))


ef = EfRegister()
fg = FgRegister()
bg = BgRegister()
rs = RsRegister()
