"""
"""
from sty.render import sgr, eightbit_fg, eightbit_bg, rgb_fg, rgb_bg


def is_args_rgb(*args):
    return len(args) > 1


def is_args_eightbit(*args):
    if args:
        if args[0] is 0:
            return True
        if isinstance(args[0], int):
            return True
    return False


class Base(object):

    def default_call(self, *args):
        if args and isinstance(args[0], dict):
            for kv in args[0].items():
                setattr(self, kv[0], kv[1])

        if len(args) == 0:
            return self

        elif isinstance(args[0], str):
            if hasattr(self, args[0]):
                return getattr(self, args[0])
            else:
                return args[0]
        else:
            return ''


class EfBase(Base):
    """
    Class to handle Effects. (italic, bold, blink, etc.)
    """

    def __call__(self, *args):
        return self.default_call(*args)

    b = sgr(1)
    bold = sgr(1)
    faint = sgr(2)
    i = sgr(3)
    italic = sgr(3)
    u = sgr(4)
    underline = sgr(4)
    blink_slow = sgr(5)
    blink_fast = sgr(6)
    reverse = sgr(7)
    conceal = sgr(8)
    crossed = sgr(9)


class RsBase(Base):
    """
    Class to handles Resets.
    """

    def __call__(self, *args):
        return self.default_call(*args)

    all = sgr(0)
    fg = sgr(39)
    bg = sgr(49)
    b = sgr(21)
    bold = sgr(21)
    faint = sgr(22)
    i = sgr(23)
    italic = sgr(23)
    u = sgr(24)
    underline = sgr(24)
    blink = sgr(25)
    conceal = sgr(28)
    strike = sgr(29)


class FgBase(Base):
    """
    Class to handle Foregrounds colors.
    """

    def __call__(self, *args):
        if is_args_rgb(*args):
            return rgb_fg(*args)

        if is_args_eightbit(*args):
            return eightbit_fg(args[0])

        return self.default_call(*args)

    # Classic terminal foreground color preset.
    # These are well supported.
    black = sgr(30)
    red = sgr(31)
    green = sgr(32)
    yellow = sgr(33)
    blue = sgr(34)
    magenta = sgr(35)
    cyan = sgr(36)
    white = sgr(37)

    # These are less supported:
    li_black = sgr(90)
    li_red = sgr(91)
    li_green = sgr(92)
    li_yellow = sgr(93)
    li_blue = sgr(94)
    li_magenta = sgr(95)
    li_cyan = sgr(96)
    li_white = sgr(97)


class BgBase(Base):
    """
    Class to handle Background colors.
    """

    def __call__(self, *args):
        if is_args_rgb(*args):
            return rgb_bg(*args)

        if is_args_eightbit(*args):
            return eightbit_bg(args[0])

        return self.default_call(*args)

    # Classic terminal foreground color preset.
    # These are well supported.
    black = sgr(40)
    red = sgr(41)
    green = sgr(42)
    yellow = sgr(43)
    blue = sgr(44)
    magenta = sgr(45)
    cyan = sgr(46)
    white = sgr(47)

    # These are less supported:
    li_black = sgr(100)
    li_red = sgr(101)
    li_green = sgr(102)
    li_yellow = sgr(103)
    li_blue = sgr(104)
    li_magenta = sgr(105)
    li_cyan = sgr(106)
    li_white = sgr(107)


ef = EfBase()
fg = FgBase()
bg = BgBase()
rs = RsBase()
