"""
These are the default registers that sty provides out of the box.
"""
from sty import renderfunc
from sty.primitive import Register, Style
from sty.rendertype import EightbitBg, EightbitFg, RgbBg, RgbFg, Sgr


class EfRegister(Register):
    """
    The default effect register.

    Instances from this class can be used to create effects like 'bold', 'dim',
    'italic', 'blink', etc.

    For example:

        print(f"{ef.bold}Bold Text{ef.rs}")
        print(f"{ef.italic}Italic Text{ef.rs}")
    """

    def __init__(self):
        super().__init__()

        self.renderfuncs[Sgr] = renderfunc.sgr

        self.b = Style(Sgr(1))
        self.bold = Style(Sgr(1))
        self.dim = Style(Sgr(2))
        self.i = Style(Sgr(3))
        self.italic = Style(Sgr(3))
        self.u = Style(Sgr(4))
        self.underl = Style(Sgr(4))
        self.blink = Style(Sgr(5))
        self.inverse = Style(Sgr(7))
        self.hidden = Style(Sgr(8))
        self.strike = Style(Sgr(9))

        # Reset all effects (Unfortunately there is no single Escape Sequence for this)
        self.rs = Style(Sgr(22), Sgr(23), Sgr(24), Sgr(25), Sgr(27), Sgr(28), Sgr(29))


class FgRegister(Register):
    """
    The default 'foreground register'.

    Instances from this class can be used to create colored text.

    For example:

        print(f"{fg.red}Red Text{fg.rs}")
        print(f"{fg.green}Green Text{fg.rs}")
    """

    def __init__(self):
        super().__init__()

        self.renderfuncs[Sgr] = renderfunc.sgr
        self.renderfuncs[EightbitFg] = renderfunc.eightbit_fg
        self.renderfuncs[RgbFg] = renderfunc.rgb_fg

        self.set_eightbit_call(EightbitFg)
        self.set_rgb_call(RgbFg)

        # Classic terminal foreground color preset.
        # These are well supported.
        self.black = Style(Sgr(30))
        self.red = Style(Sgr(31))
        self.green = Style(Sgr(32))
        self.yellow = Style(Sgr(33))
        self.blue = Style(Sgr(34))
        self.magenta = Style(Sgr(35))
        self.cyan = Style(Sgr(36))
        self.li_grey = Style(Sgr(37))

        self.rs = Style(Sgr(39))

        # These are less supported.
        self.da_grey = Style(Sgr(90))
        self.li_red = Style(Sgr(91))
        self.li_green = Style(Sgr(92))
        self.li_yellow = Style(Sgr(93))
        self.li_blue = Style(Sgr(94))
        self.li_magenta = Style(Sgr(95))
        self.li_cyan = Style(Sgr(96))
        self.white = Style(Sgr(97))

        # These are least supported.
        self.da_black = Style(EightbitFg(0))
        self.da_red = Style(EightbitFg(88))
        self.da_green = Style(EightbitFg(22))
        self.da_yellow = Style(EightbitFg(58))
        self.da_blue = Style(EightbitFg(18))
        self.da_magenta = Style(EightbitFg(89))
        self.da_cyan = Style(EightbitFg(23))
        self.grey = Style(EightbitFg(249))


class BgRegister(Register):
    """
    The default 'background register'.

    Instances from this class can be used to create text with colored backgrounds.

    For example:

        print(f"{bg.red}Text With Red Background{bg.rs}")
        print(f"{bg.green}Text With Green Background{bg.rs}")
    """

    def __init__(self):
        super().__init__()

        self.renderfuncs[Sgr] = renderfunc.sgr
        self.renderfuncs[EightbitBg] = renderfunc.eightbit_bg
        self.renderfuncs[RgbBg] = renderfunc.rgb_bg

        self.set_eightbit_call(EightbitBg)
        self.set_rgb_call(RgbBg)

        # Classic terminal background color preset.
        # These are well supported.
        self.black = Style(Sgr(40))
        self.red = Style(Sgr(41))
        self.green = Style(Sgr(42))
        self.yellow = Style(Sgr(43))
        self.blue = Style(Sgr(44))
        self.magenta = Style(Sgr(45))
        self.cyan = Style(Sgr(46))
        self.li_grey = Style(Sgr(47))

        self.rs = Style(Sgr(49))

        # These are less supported.
        self.da_grey = Style(Sgr(100))
        self.li_red = Style(Sgr(101))
        self.li_green = Style(Sgr(102))
        self.li_yellow = Style(Sgr(103))
        self.li_blue = Style(Sgr(104))
        self.li_magenta = Style(Sgr(105))
        self.li_cyan = Style(Sgr(106))
        self.white = Style(Sgr(107))

        # These are least supported.
        self.da_black = Style(EightbitBg(0))
        self.da_red = Style(EightbitBg(88))
        self.da_green = Style(EightbitBg(22))
        self.da_yellow = Style(EightbitBg(58))
        self.da_blue = Style(EightbitBg(18))
        self.da_magenta = Style(EightbitBg(89))
        self.da_cyan = Style(EightbitBg(23))
        self.grey = Style(EightbitBg(249))


class RsRegister(Register):
    """
    The default 'reset register'.

    Instances from this class can be used to reset single effects, foregrounds
    and backgrounds.

    For example:

        print(f"{ef.italic}Italic Text{rs.italic}")
        print(f"{ef.underl}Underlined Text{rs.underl}")
        print(f"{fg.red}{ef.italic}Red Italic Text{rs.all}")
    """

    def __init__(self):
        super().__init__()

        self.renderfuncs[Sgr] = renderfunc.sgr

        self.all = Style(Sgr(0))
        self.fg = Style(Sgr(39))
        self.bg = Style(Sgr(49))
        # Reset all effects (Unfortunately there is no single Escape Sequence for this)
        self.ef = Style(Sgr(22), Sgr(23), Sgr(24), Sgr(25), Sgr(27), Sgr(28), Sgr(29))

        self.bold_dim = Style(Sgr(22))
        self.dim_bold = Style(Sgr(22))
        self.i = Style(Sgr(23))
        self.italic = Style(Sgr(23))
        self.u = Style(Sgr(24))
        self.underl = Style(Sgr(24))
        self.blink = Style(Sgr(25))
        self.inverse = Style(Sgr(27))
        self.hidden = Style(Sgr(28))
        self.strike = Style(Sgr(29))


ef = EfRegister()
fg = FgRegister()
bg = BgRegister()
rs = RsRegister()
