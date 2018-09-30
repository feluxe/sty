from sty import Rule, renderfunc, EfRegister, FgRegister, RsRegister, BgRegister, Render
from random import randint


def reset_registers():
    ef = EfRegister()
    fg = FgRegister()
    bg = BgRegister()
    rs = RsRegister()

    return ef, fg, bg, rs


print('\nGetting Started\n--------------------')
ef, fg, bg, rs = reset_registers()

# from sty import fg, bg, ef, rs, Render

foo = fg.red + 'This is red text!' + fg.rs
bar = bg.blue + 'This has a blue background!' + bg.rs
baz = ef.italic + 'This is italic text' + rs.italic
qux = fg(201) + 'This is pink text using 8bit colors' + fg.rs
qui = fg(255, 10, 10) + 'This is red text using 24bit colors.' + fg.rs

# Add new colors:

fg.orange = Rule(Render.rgb_fg, 255, 150, 50)

buf = fg.orange + 'Yay, Im orange.' + fg.rs

print(foo, bar, baz, qux, qui, buf, sep='\n')

a = ef('italic') + 'Italic text.' + rs.italic
b = fg('blue') + 'Blue text.' + rs.fg
c = bg(randint(0, 254)) + 'Random colored bg' + rs.bg

print(a, b, c, sep='\n')

print('\nHello World!\n--------------------')
ef, fg, bg, rs = reset_registers()

my_string = fg.black + bg.white + ef.bold + 'Hello world!' + rs.all
print(my_string)

print('\nItalic\n--------------------')
ef, fg, bg, rs = reset_registers()

a = ef.italic + 'Italic.' + rs.italic

# There are shorthands for this:
b = ef.i + fg.blue + 'Italic.' + rs.i + ' Not italic but blue.' + rs.fg

print(a, b, sep='\n')

print('\nBold\n--------------------')
ef, fg, bg, rs = reset_registers()

a = ef.bold + 'Bold.' + rs.bold_dim

# This has shorthands too:
b = ef.b + 'Bold.' + rs.bold_dim + fg.li_yellow + ' Not bold but yellow.' + rs.fg

print(a, b, sep='\n')

print('\nUnderline\n--------------------')
ef, fg, bg, rs = reset_registers()

a = ef.underl + 'Underlined.' + rs.underl

# Shorthand version:
b = ef.u + 'Underlined.' + rs.u + fg.green + ' Not underlined but green.' + rs.fg

print(a, b, sep='\n')

print('\nDim\n--------------------')
ef, fg, bg, rs = reset_registers()

a = ef.dim + fg.yellow + 'Dimmed yellow.' + rs.dim_bold + ' Undimmed yellow' + rs.fg

print(a, sep='\n')

print('\nBlink\n--------------------')
ef, fg, bg, rs = reset_registers()

a = ef.blink + 'Blinking.' + rs.blink + ' Not blinking'

print(a, sep='\n')

print('\nInverse\n--------------------')
ef, fg, bg, rs = reset_registers()

a = ef.inverse + 'Inversed.' + rs.inverse + ' Not inversed'

print(a, sep='\n')

print('\nHidden\n--------------------')
ef, fg, bg, rs = reset_registers()

a = ef.hidden + 'Hidden.' + rs.hidden + ' Not Hidden'

print(a, sep='\n')

print('\nStrike\n--------------------')
ef, fg, bg, rs = reset_registers()

a = ef.strike + 'Striked out.' + rs.strike + ' Not Striked out'

print(a, sep='\n')

print('\nString coloring by name\n--------------------')
ef, fg, bg, rs = reset_registers()

a = fg.li_blue + 'I have a light blue foreground.' + rs.fg
b = bg.cyan + 'I have a cyan background' + rs.bg
c = fg.da_red + bg.li_red + 'I have a dark red fg and light red bg.' + rs.all
d = fg('yellow') + 'I have yellow fg.' + rs.fg

print(a, b, c, d, sep='\n')

print('\nString coloring by 8-bit number\n--------------------')
ef, fg, bg, rs = reset_registers()

a = fg(34) + 'I have a green foreground.' + rs.fg
b = bg(133) + 'I have a pink background' + rs.bg
c = fg(226) + bg(19) + 'I have a light yellow fg and dark blue bg.' + rs.all

print(a, b, c, sep='\n')

print('\nString coloring by 24-bit RGB value\n--------------------')
ef, fg, bg, rs = reset_registers()

a = fg(10, 255, 10) + 'I have a green foreground.' + rs.fg
b = bg(255, 150, 50) + 'I have an orange background' + rs.bg
c = fg(90, 90, 90) + bg(32, 32, 32) + 'Grey fg and dark grey bg.' + rs.all

print(a, b, c, sep='\n')

print('\nDirect attribute customization\n--------------------')
ef, fg, bg, rs = reset_registers()

# ef.italic now renders underlined text.
ef.italic = Rule(Render.sgr, 4)

# fg.red renders green text from now on.
fg.red = Rule(Render.sgr, 32)

# fg.blue renders red text from now on (using an 8bit color code).
fg.blue = Rule(Render.eightbit_fg, 88)

# Create a new item that renders brown text.
fg.my_new_item = Rule(Render.eightbit_fg, 130)

# bg.green renders blue bg from now on (using a 24bit rgb code).
bg.green = Rule(Render.rgb_bg, 0, 128, 255)

# rs.all only resets the underline effect from now on.
rs.bold_dim = Rule(Render.sgr, 24)

a = ef.italic + 'This is not italic any more, but underlined' + rs.underl
b = fg.red + 'This is not red any more, but green.' + rs.fg
c = fg.blue + 'This is not blue any more, but red' + rs.fg
d = fg.my_new_item + 'This is a new brown attribute' + rs.fg
e = bg.green + 'This is not green bg any more, but blue.' + rs.bg
f = ef.bold + 'This does not reset bold any more' + rs.bold_dim \
    + ' -> This is still bold' + rs.all

print(a, b, c, d, e, f, sep='\n')

print(
    '\nDirect attribute customization with multiple rules\n--------------------'
)
ef, fg, bg, rs = reset_registers()

fg.green_ul = Rule(Render.sgr, 32), Rule(Render.sgr, 4)
fg.red_i = Rule(Render.sgr, 31), ef.i
fg.blue_b = fg.blue + ef.b

a = fg.green_ul + 'This is green and underline text.' + rs.all
b = fg.red_i + 'This is red and italic text.' + rs.all
c = fg.blue_b + 'This is blue and bold text.' + rs.all

print(a, b, c, sep='\n')

print('\nDynamic attribute customization\n--------------------')
ef, fg, bg, rs = reset_registers()

my_color_name = 'teal'

fg.set_rule(my_color_name, Rule(Render.eightbit_fg, 51))

a = fg.teal + 'This is custom teal text.' + fg.rs

print(a)

print(
    '\nDynamic attribute customization with multiple rules\n--------------------'
)
ef, fg, bg, rs = reset_registers()

my_color_name1 = 'teal_b'
my_color_name2 = 'green_i'
my_color_name3 = 'red_ul'

fg.set_rule(my_color_name1, (Rule(Render.eightbit_fg, 51), Rule(Render.sgr, 1)))
fg.set_rule(my_color_name2, (fg.green, ef.i))
fg.set_rule(my_color_name3, (Rule(Render.sgr, 31), ef.underl))

a = fg.teal_b + 'This is custom teal and bold text.' + rs.all
b = fg.green_i + 'This is green italic text.' + rs.all
c = fg.red_ul + 'This is red and undelrined text.' + rs.all

print(a, b, c, sep='\n')

print('\nExtending the default registers\n--------------------')
ef, fg, bg, rs = reset_registers()

from sty.register import FgRegister, Rule, Render

# Extend default Fg register.


class MyFgRegister(FgRegister):

    black = Rule(Render.sgr, 31)
    red = Rule(Render.sgr, 34)
    orange = Rule(Render.rgb_fg, 255, 128, 0)
    # ...


# Create a new instance from the new Register

fg = MyFgRegister()

a = fg.orange + 'This is orange text from a non default attribute.' + rs.fg

print(a)

print('\nReplace or add renderers\n--------------------')
ef, fg, bg, rs = reset_registers()

from sty.register import FgRegister


def rgb_bg(rgb: tuple):
    r = str(rgb[0])
    g = str(rgb[1])
    b = str(rgb[2])
    return '\x1b[48;2;' + r + ';' + g + ';' + b + 'm'


# Extend default Fg register.
class MyFgRegister(FgRegister):

    def __init__(self):
        super().__init__()
        self.set_renderer(Render.rgb_bg, renderfunc.rgb_bg)

    black = Rule(Render.sgr, 31)
    red = Rule(Render.sgr, 34)
    orange = Rule(Render.rgb_bg, 255, 128, 0)


fg = MyFgRegister()

a = fg.orange + 'I have an orange background instead of an orange fg.' + rs.bg

fg.set_renderer(Render.rgb_bg, renderfunc.rgb_fg)

b = fg.orange + 'I have orange fg again.' + rs.fg

print(a, b, sep='\n')

print('\nChange call renderers\n--------------------')
ef, fg, bg, rs = reset_registers()

from sty.register import FgRegister


class MyFgRegister2(FgRegister):

    def __init__(self):
        super().__init__()
        self.set_renderer(Render.eightbit_bg, renderfunc.eightbit_bg)
        self.set_renderer(Render.rgb_bg, renderfunc.rgb_bg)

    eightbit_call = Rule(Render.eightbit_bg)
    rgb_call = Rule(Render.rgb_bg)

    black = Rule(Render.sgr, 31)
    red = Rule(Render.sgr, 34)
    orange = Rule(Render.rgb_bg, 255, 128, 0)


fg = MyFgRegister2()

a = fg(90) + 'Colored bg instead of colored fg.' + rs.bg
b = fg(40, 50, 200) + 'Colored bg instead of colored fg.' + rs.bg

print(a, b, sep='\n')

print('\nMute Formatting\n--------------------')
ef, fg, bg, rs = reset_registers()

fg.mute()

a = fg.red + 'This red forground was muted.' + fg.rs
b = fg(10) + 'This green foreground was muted.' + fg.rs
c = fg(100, 140, 180) + "This blue foreground was muted." + fg.rs

fg.unmute()

d = fg.red + 'The mute switch is off, so this is red.' + fg.rs
e = fg(10) + 'The mute switch is off, so this is green.' + fg.rs
f = fg(100, 140, 180) + 'The mute switch is off, so this is blue.' + fg.rs

print(a, b, c, d, e, f, sep='\n')
