# from sty.rendertype import EightbitFg

from .. import Example

print("\n\nCUSTOMIZING\n" + "=" * 80)

# ===== Start =====
Example("customizing the register-objects: assignment")
from sty import RgbFg, Sgr, Style, ef, fg, rs

fg.my_red = Style(RgbFg(255, 0, 0))

a = fg.my_red + "This text has red fg." + fg.rs

print(a)
# ===== End =====

# ===== Start =====
Example("customizing the register-objects: compose")
from sty import RgbFg, Sgr, Style, ef, fg, rs

fg.blue_bold = Style(RgbFg(0, 100, 200), Sgr(1))
fg.green_italic = Style(fg.green, ef.i)

a = fg.blue_bold + "This text has bold blue fg." + rs.all
b = fg.green_italic + "This text has italic green fg" + rs.all

print(a, b, sep="\n")
# ===== End =====

# ===== Start =====
Example("customizing the register-objects: render-func")
from sty import bg, fg, EightbitFg


def my_eightbit_bg_render_func(num: int) -> str:
    return "\033[48;5;" + str(num) + "m"


# Replace fg render-function with the above bg render-function:
fg.set_renderfunc(EightbitFg, my_eightbit_bg_render_func)

a = fg.da_green + "I have a green bg because my render-func was replaced" + bg.rs

print(a)
# ===== End =====

# ===== Start =====
Example("customizing the register-objects: calls")
from sty import EightbitBg, RgbBg, fg, renderfunc, rs

fg.set_renderfunc(EightbitBg, renderfunc.eightbit_bg)
fg.set_renderfunc(RgbBg, renderfunc.rgb_bg)

fg.set_eightbit_call(EightbitBg)
fg.set_rgb_call(RgbBg)

a = fg(201) + "I have a pink bg since fg was replaced with bg." + rs.all
b = fg(255, 10, 10) + "I have a red bg since fg was replaced with bg." + rs.all

print(a, b, sep="\n")
# ===== End =====

# ===== Start =====
Example("extending register-classes")
from sty import FgRegister, RgbFg, Sgr

# Extend the default foreground register-class.


class MyFgRegister(FgRegister):
    def __init__(self):

        super().__init__()

        # Add custom style attributes.

        self.purple = Style(Sgr(35))
        self.blue = Style(Sgr(34))
        self.orange = Style(RgbFg(255, 128, 0))
        # ...


# Create new register-object from extended register-class.

fg = MyFgRegister()

# Use your new register-object.

a = fg.purple + "I have purple foreground" + fg.rs
b = fg.blue + "I have blue foreground" + fg.rs
c = fg.orange + "I have orange foreground" + fg.rs
d = fg.green + "I have a green foreground" + fg.rs

print(a, b, c, d, sep="\n")
# ===== End =====

# ===== Start =====
Example("register-class from scratch")
from sty import EightbitFg, Register, RgbFg, Sgr, renderfunc


def my_eightbit_fg_render_func(num: int) -> str:
    return "\033[38;5;" + str(num) + "m"


def my_rgb_fg_render_func(r: int, g: int, b: int) -> str:
    return "\x1b[38;2;" + str(r) + ";" + str(g) + ";" + str(b) + "m"


class FgRegister(Register):
    def __init__(self):

        super().__init__()

        self.set_renderfunc(Sgr, renderfunc.sgr)
        self.set_renderfunc(EightbitFg, renderfunc.eightbit_fg)
        self.set_renderfunc(RgbFg, renderfunc.rgb_fg)

        self.set_eightbit_call(EightbitFg)
        self.set_rgb_call(RgbFg)

        self.red = Style(Sgr(31))
        self.green = Style(Sgr(32))
        self.rs = Style(Sgr(39))
        self.yellow = Style(RgbFg(250, 250, 70))
        # ...


# Create new register-object from register-class.

fg = FgRegister()

# Use your new register-object.

a = fg.yellow + "I have yellow foreground" + fg.rs
b = fg.red + "I have red foreground" + fg.rs
c = fg.green + "I have green foreground" + fg.rs

print(a, b, c, sep="\n")

# ===== End =====
