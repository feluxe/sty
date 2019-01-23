from .. import Example, reset_registers


print("\n\nCUSTOMIZING\n" + "="*80)

# ===== Start =====
# TODO: REMOVE
Example("attribute customization")
from sty import ef, fg, bg, rs, Rule, Render
# ef.italic now renders underlined text.
ef.set_style('italic', Rule(Render.sgr, 4))

# fg.red renders green text from now on.
fg.set_style('red', Rule(Render.sgr, 32))

# fg.blue renders red text from now on (using an 8bit color code).
fg.set_style('blue', Rule(Render.eightbit_fg, 88))

# Create a new item that renders brown text.
fg.set_style('my_new_item', Rule(Render.eightbit_fg, 130))

# bg.green renders blue bg from now on (using a 24bit rgb code).
bg.set_style('green', Rule(Render.rgb_bg, 0, 128, 255))

# rs.all only resets the underline effect from now on.
rs.set_style('bold_dim', Rule(Render.sgr, 24))

# TODO Create a new item that renders brown text.
fg.set_style('my_new_item', fg.styles['red'])

a = ef.italic + 'This is not italic any more, but underlined' + rs.underl
b = fg.red + 'This is not red any more, but green.' + rs.fg
c = fg.blue + 'This is not blue any more, but red' + rs.fg
d = fg.my_new_item + 'This is a new brown attribute' + rs.fg
e = bg.green + 'This is not green bg any more, but blue.' + rs.bg
f = ef.bold + 'This does not reset bold any more' + rs.bold_dim \
    + ' -> This is still bold' + rs.all

print(a, b, c, d, e, f, sep='\n')
# ===== End =====

# ===== Start =====
# TODO: REMOVE
Example("attirbute customization with multiple rules")
fg.set_style('green_ul', Rule(Render.sgr, 32), Rule(Render.sgr, 4))
fg.set_style('red_i', Rule(Render.sgr, 31), ef.styles['i'])
fg.set_style('blue_b', fg.styles['blue'], ef.styles['b'])

a = fg.green_ul + 'This is green and underline text.' + rs.all
b = fg.red_i + 'This is red and italic text.' + rs.all
c = fg.blue_b + 'This is blue and bold text.' + rs.all

print(a, b, c, sep='\n')
# ===== End =====

# ===== Start =====
# TODO: REMOVE
Example("dynamic attribute customization")
# my_color_name = 'teal'

# fg.set_style(my_color_name, Rule(Render.eightbit_fg, 51))

# a = fg.teal + 'This is custom teal text.' + fg.rs

# print(a)
# ===== End =====

# ===== Start =====
# TODO: REMOVE
Example("dynamic attribute customization with multiple rules")
# my_color_name1 = 'teal_b'
# my_color_name2 = 'green_i'
# my_color_name3 = 'red_ul'

# fg.set_style(my_color_name1, Rule(Render.eightbit_fg, 51), Rule(Render.sgr, 1))
# fg.set_style(my_color_name2, fg.styles['green'], ef.styles['i'])
# fg.set_style(my_color_name3, Rule(Render.sgr, 31), ef.styles['underl'])

# fg[my_color_name1] = Rule(Render.eightbit_fg, 51), Rule(Render.sgr, 1)
# fg[my_color_name2] = fg.styles['green'], ef.styles['i']
# fg[my_color_name3] = Rule(Render.sgr, 31), ef.styles['underl']

# a = fg.teal_b + 'This is custom teal and bold text.' + rs.all
# b = fg.green_i + 'This is green italic text.' + rs.all
# c = fg.red_ul + 'This is red and undelrined text.' + rs.all

# print(a, b, c, sep='\n')
# ===== End =====

# ===== Start =====
Example("extending the default registers")
from sty.register import FgRegister, Rule, Render


# Extend default Fg register.
class MyFgRegister(FgRegister):

    orange = ''  # Set the new attribute here as well, for better editor support.

    def __init__(self):
        super().__init__()

        self.set_style('black', Rule(Render.sgr, 31))
        self.set_style('red', Rule(Render.sgr, 34))
        self.set_style('orange', Rule(Render.rgb_fg, 255, 128, 0))

    # ...


# Create a new instance from the new Register

fg = MyFgRegister()

a = fg.orange + 'This is orange text from a non default attribute.' + rs.fg

print(a)
# ===== End =====

# ===== Start =====
Example("replace or add render functions")
from sty.register import FgRegister, renderfunc


def my_eightbit_bg_renderfunc(num: int):
    return '\033[48;5;' + str(num) + 'm'


# Extend default Fg register.
class MyFgRegister(FgRegister):

    def __init__(self):
        super().__init__()

        # Switch fg renderer with bg renderer.
        self.set_renderfunc(Render.eightbit_fg, my_eightbit_bg_renderfunc)


fg = MyFgRegister()

a = fg.da_red + 'I have an red background instead of an red fg.' + rs.bg

fg.set_renderfunc(Render.eightbit_fg, renderfunc.eightbit_fg)

b = fg.red + 'I have red fg again.' + rs.fg

print(a, b, sep='\n')
# ===== End =====

# ===== Start =====
Example("change call functions")
print(a, b, sep='\n')

from sty.register import FgRegister


class MyFgRegister2(FgRegister):

    def __init__(self):
        super().__init__()
        self.set_renderfunc(Render.eightbit_bg, renderfunc.eightbit_bg)
        self.set_renderfunc(Render.rgb_bg, renderfunc.rgb_bg)

        self.set_eightbit_callfunc(Render.eightbit_bg)
        self.set_rgb_callfunc(Render.rgb_bg)

        self.set_style('black', Rule(Render.sgr, 31))
        self.set_style('red', Rule(Render.sgr, 34))
        self.set_style('orange', Rule(Render.rgb_bg, 255, 128, 0))


fg = MyFgRegister2()

a = fg(90) + 'Colored bg instead of colored fg.' + rs.bg
b = fg(40, 50, 200) + 'Colored bg instead of colored fg.' + rs.bg

print(a, b, sep='\n')
# ===== End =====
