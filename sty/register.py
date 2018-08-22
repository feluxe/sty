"""
These are the default registers that sty provides out of the box.
"""

from sty import renderfunc, primitive, Rule
from enum import Enum


class Render:
    sgr = 'sgr'
    eightbit_fg = 'eightbit_fg'
    eightbit_bg = 'eightbit_bg'
    rgb_fg = 'rgb_fg'
    rgb_bg = 'rgb_bg'


class EfRegister(primitive.Base):

    def __init__(self):
        self.set_renderer(Render.sgr, renderfunc.sgr)

    b = Rule(Render.sgr, 1)
    bold = Rule(Render.sgr, 1)
    dim = Rule(Render.sgr, 2)
    i = Rule(Render.sgr, 3)
    italic = Rule(Render.sgr, 3)
    u = Rule(Render.sgr, 4)
    underl = Rule(Render.sgr, 4)
    blink = Rule(Render.sgr, 5)
    inverse = Rule(Render.sgr, 7)
    hidden = Rule(Render.sgr, 8)
    strike = Rule(Render.sgr, 9)


class FgRegister(primitive.Base):

    def __init__(self):
        self.set_renderer(Render.sgr, renderfunc.sgr)
        self.set_renderer(Render.eightbit_fg, renderfunc.eightbit_fg)
        self.set_renderer(Render.rgb_fg, renderfunc.rgb_fg)

    eightbit_call = Rule(Render.eightbit_fg)
    rgb_call = Rule(Render.rgb_fg)

    # Classic terminal foreground color preset.
    # These are well supported.
    black = Rule(Render.sgr, 30)
    red = Rule(Render.sgr, 31)
    green = Rule(Render.sgr, 32)
    yellow = Rule(Render.sgr, 33)
    blue = Rule(Render.sgr, 34)
    magenta = Rule(Render.sgr, 35)
    cyan = Rule(Render.sgr, 36)
    white = Rule(Render.sgr, 37)

    rs = Rule(Render.sgr, 39)

    # These are less good supported:
    li_black = Rule(Render.sgr, 90)
    li_red = Rule(Render.sgr, 91)
    li_green = Rule(Render.sgr, 92)
    li_yellow = Rule(Render.sgr, 93)
    li_blue = Rule(Render.sgr, 94)
    li_magenta = Rule(Render.sgr, 95)
    li_cyan = Rule(Render.sgr, 96)
    li_white = Rule(Render.sgr, 97)

    # These are less supported:
    da_black = Rule(Render.eightbit_fg, 0)
    da_red = Rule(Render.eightbit_fg, 88)
    da_green = Rule(Render.eightbit_fg, 22)
    da_yellow = Rule(Render.eightbit_fg, 58)
    da_blue = Rule(Render.eightbit_fg, 18)
    da_magenta = Rule(Render.eightbit_fg, 89)
    da_cyan = Rule(Render.eightbit_fg, 23)
    da_white = Rule(Render.eightbit_fg, 249)


class BgRegister(primitive.Base):

    def __init__(self):
        self.set_renderer(Render.sgr, renderfunc.sgr)
        self.set_renderer(Render.eightbit_bg, renderfunc.eightbit_bg)
        self.set_renderer(Render.rgb_bg, renderfunc.rgb_bg)

    eightbit_call = Rule(Render.eightbit_bg)
    rgb_call = Rule(Render.rgb_bg)

    # Classic terminal background color preset.
    # These are well supported.
    black = Rule(Render.sgr, 40)
    red = Rule(Render.sgr, 41)
    green = Rule(Render.sgr, 42)
    yellow = Rule(Render.sgr, 43)
    blue = Rule(Render.sgr, 44)
    magenta = Rule(Render.sgr, 45)
    cyan = Rule(Render.sgr, 46)
    white = Rule(Render.sgr, 47)

    rs = Rule(Render.sgr, 49)

    # These are less good supported:
    li_black = Rule(Render.sgr, 100)
    li_red = Rule(Render.sgr, 101)
    li_green = Rule(Render.sgr, 102)
    li_yellow = Rule(Render.sgr, 103)
    li_blue = Rule(Render.sgr, 104)
    li_magenta = Rule(Render.sgr, 105)
    li_cyan = Rule(Render.sgr, 106)
    li_white = Rule(Render.sgr, 107)

    # These are less supported:
    da_black = Rule(Render.eightbit_bg, 0)
    da_red = Rule(Render.eightbit_bg, 88)
    da_green = Rule(Render.eightbit_bg, 22)
    da_yellow = Rule(Render.eightbit_bg, 58)
    da_blue = Rule(Render.eightbit_bg, 18)
    da_magenta = Rule(Render.eightbit_bg, 89)
    da_cyan = Rule(Render.eightbit_bg, 23)
    da_white = Rule(Render.eightbit_bg, 249)


class RsRegister(primitive.Base):

    def __init__(self):
        self.set_renderer(Render.sgr, renderfunc.sgr)

    all = Rule(Render.sgr, 0)
    fg = Rule(Render.sgr, 39)
    bg = Rule(Render.sgr, 49)

    # Deprecated:
    # b = Rule(Render.sgr, 21)
    # bold = Rule(Render.sgr, 21)

    bold_dim = Rule(Render.sgr, 22)
    dim_bold = Rule(Render.sgr, 22)
    i = Rule(Render.sgr, 23)
    italic = Rule(Render.sgr, 23)
    u = Rule(Render.sgr, 24)
    underl = Rule(Render.sgr, 24)
    blink = Rule(Render.sgr, 25)
    inverse = Rule(Render.sgr, 27)
    hidden = Rule(Render.sgr, 28)
    strike = Rule(Render.sgr, 29)


ef = EfRegister()
fg = FgRegister()
bg = BgRegister()
rs = RsRegister()
