from .. import Example
from sty.rendertype import *

print("\n\nCUSTOMIZING\n" + "=" * 80)

# ===== Start =====
Example("customizing the register-objects: set_style")
from sty import fg, RgbFg

fg.set_style('my_red', RgbFg(255, 0, 0))

a = fg.my_red + 'This text has red fg.' + fg.rs

print(a)
# ===== End =====

# ===== Start =====
Example("customizing the register-objects: render_types")
from sty import fg, Sgr, RgbFg, EightbitFg

fg.set_style('my_sgr_red', Sgr(31))
fg.set_style('my_eightbit_red', EightbitFg(196))
fg.set_style('my_rgb_red', RgbFg(255, 0, 0))

a = fg.my_sgr_red + 'This text has a red fg.' + fg.rs
b = fg.my_eightbit_red + 'This text has a red fg.' + fg.rs
c = fg.my_rgb_red + 'This text has a red fg.' + fg.rs

print(a, b, c, sep='\n')
# ===== End =====

# ===== Start =====
Example("customizing the register-objects: get_style")
from sty import ef, fg, rs

# Make fg.green_i render a green and itelic foreground.
fg.set_style('green_i', fg.get_style('green'), ef.get_style('italic'))

# Make rs.green_i reset green and itelic foregrounds.
rs.set_style('green_i', rs.get_style('fg'), rs.get_style('italic'))

a = fg.green_i + 'This text has a green italic fg.' + rs.green_i

print(a, sep='\n')
# ===== End =====

# ===== End =====

# ===== Start =====
Example("customizing the register-objects: render-func")
from sty import fg, bg


def my_eightbit_bg_render_func(num: int) -> str:
    return '\033[48;5;' + str(num) + 'm'


# Replace fg render-function with the above bg render-function:
fg.set_renderfunc(EightbitFg, my_eightbit_bg_render_func)

a = fg.da_green + "I have a green bg because my render-func was replaced" + bg.rs

print(a)
# ===== End =====

# ===== Start =====
Example("customizing the register-objects: calls")
from sty import fg, rs, renderfunc, EightbitBg, RgbBg

fg.set_renderfunc(EightbitBg, renderfunc.eightbit_bg)
fg.set_renderfunc(RgbBg, renderfunc.rgb_bg)

fg.set_eightbit_call(EightbitBg)
fg.set_rgb_call(RgbBg)

a = fg(201) + 'I have a pink bg since fg was replaced with bg.' + rs.all
b = fg(255, 10, 10) + 'I have a red bg since fg was replaced with bg.' + rs.all

print(a, b, sep="\n")
# ===== End =====

# ===== Start =====
Example("extending register-classes")
from sty import FgRegister, Sgr, RgbFg

# Extend the default foreground register-class.


class MyFgRegister(FgRegister):

    # Add this for better editor support.

    purple: str
    blue: str
    orange: str

    # ...

    def __init__(self):

        super().__init__()

        # Add custom style attributes.

        self.set_style('purple', Sgr(35))
        self.set_style('blue', Sgr(34))
        self.set_style('orange', RgbFg(255, 128, 0))
        # ...


# Create new register-object from extended register-class.

fg = MyFgRegister()

# Use your new register-object.

a = fg.purple + "I have purple foreground" + fg.rs
b = fg.blue + "I have blue foreground" + fg.rs
c = fg.orange + "I have orange foreground" + fg.rs
d = fg.green + "I have a green foreground" + fg.rs

print(a, b, c, d, sep='\n')
# ===== End =====

# ===== Start =====
Example("register-class from scratch")
from sty import Base, renderfunc, Sgr, EightbitFg, RgbFg


def my_eightbit_fg_render_func(num: int) -> str:
    return '\033[38;5;' + str(num) + 'm'


def my_rgb_fg_render_func(r: int, g: int, b: int) -> str:
    return '\x1b[38;2;' + str(r) + ';' + str(g) + ';' + str(b) + 'm'


class FgRegister(Base):

    yellow: str
    red: str
    green: str
    rs: str

    # ...

    def __init__(self):

        super().__init__()

        self.set_renderfunc(Sgr, renderfunc.sgr)
        self.set_renderfunc(EightbitFg, renderfunc.eightbit_fg)
        self.set_renderfunc(RgbFg, renderfunc.rgb_fg)

        self.set_eightbit_call(EightbitFg)
        self.set_rgb_call(RgbFg)

        self.set_style('red', Sgr(31))
        self.set_style('green', Sgr(32))
        self.set_style('rs', Sgr(39))
        self.set_style('yellow', RgbFg(250, 250, 70))
        # ...


# Create new register-object from register-class.

fg = FgRegister()

# Use your new register-object.

a = fg.yellow + "I have yellow foreground" + fg.rs
b = fg.red + "I have red foreground" + fg.rs
c = fg.green + "I have green foreground" + fg.rs

print(a, b, c, sep='\n')

# ===== End =====
