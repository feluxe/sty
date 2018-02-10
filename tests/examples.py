from sty.register import FgRegister, BgRegister, RsRegister, EfRegister
from random import randint

print('\nGetting Started\n--------------------')

ef = EfRegister()
fg = FgRegister()
bg = BgRegister()
rs = RsRegister()

foo = fg.red + 'This is red text!' + fg.rs
bar = bg.blue + 'This has a blue background!' + bg.rs
baz = ef.italic + 'This is italic text' + rs.italic
qux = fg(201) + 'This is pink text using 8bit colors' + fg.rs
qui = fg(255, 10, 10) + 'This is red text using 24bit colors.' + fg.rs

# Add new colors:

fg.orange = ('rgb', (255, 150, 50))

buf = fg.orange + 'Yay, Im orange.' + fg.rs

print(foo, bar, baz, qux, qui, buf, sep='\n')

a = ef('italic') + 'Italic text.' + rs.italic
b = fg('blue') + 'Blue text.' + rs.fg
c = bg(randint(0, 254)) + 'Random colored bg' + rs.bg

print(a, b, c , sep='\n')

print('\nHello World!\n--------------------')
ef = EfRegister()
fg = FgRegister()
bg = BgRegister()
rs = RsRegister()

my_string = fg.black + bg.white + ef.bold + 'Hello world!' + rs.all
print(my_string)

print('\nItalic\n--------------------')
ef = EfRegister()
fg = FgRegister()
bg = BgRegister()
rs = RsRegister()

a = ef.italic + 'Italic.' + rs.italic

# There are shorthands for this:
b = ef.i + fg.blue + 'Italic.' + rs.i + ' Not italic but blue.' + rs.fg

print(a, b, sep='\n')

print('\nBold\n--------------------')
ef = EfRegister()
fg = FgRegister()
bg = BgRegister()
rs = RsRegister()

a = ef.bold + 'Bold.' + rs.bold

# This has shorthands too:
b = ef.b + 'Bold.' + rs.b + fg.li_yellow + ' Not bold but yellow.' + rs.fg

print(a, b, sep='\n')

print('\nUnderlining\n--------------------')
ef = EfRegister()
fg = FgRegister()
bg = BgRegister()
rs = RsRegister()

a = ef.underline + 'Underlined.' + rs.underline

# Shorthand version:
b = ef.u + 'Underlined.' + rs.u + fg.green + ' Not underlined but green.' + rs.fg

print(a, b, sep='\n')

print('\nString coloring by name\n--------------------')
ef = EfRegister()
fg = FgRegister()
bg = BgRegister()
rs = RsRegister()

a = fg.blue + 'I have a blue foreground.' + rs.fg
b = bg.li_cyan + 'I have a light cyan background' + rs.bg
c = fg.red + bg.green + 'I have a red fg and green bg.' + rs.all

print(a, b, c, sep='\n')

print('\nString coloring by 8-bit number\n--------------------')
ef = EfRegister()
fg = FgRegister()
bg = BgRegister()
rs = RsRegister()

a = fg(34) + 'I have a green foreground.' + rs.fg
b = bg(133) + 'I have a pink background' + rs.bg
c = fg(226) + bg(19) + 'I have a light yellow fg and dark blue bg.' + rs.all

print(a, b, c, sep='\n')

print('\nString coloring by 24-bit RGB value\n--------------------')
ef = EfRegister()
fg = FgRegister()
bg = BgRegister()
rs = RsRegister()

a = fg(10, 255, 10) + 'I have a green foreground.' + rs.fg
b = bg(255, 150, 50) + 'I have an orange background' + rs.bg
c = fg(90, 90, 90) + bg(32, 32, 32) + 'Grey fg and dark grey bg.' + rs.all

print(a, b, c, sep='\n')

print('\nDirect attribute customization\n--------------------')
ef = EfRegister()
fg = FgRegister()
bg = BgRegister()
rs = RsRegister()

ef.italic = ('sgr', 4)  # ef.italic now renders underlined text.
fg.red = ('sgr', 32)  # fg.red renders green text from now on.
fg.blue = ('eightbit',
           88)  # fg.blue renders red text from now on (using an 8bit color code).
fg.my_new_item = ('eightbit', 130)  # Create a new item that renders brown text.
bg.green = ('rgb', (0, 128,
                    255))  # bg.green renders blue text from now on (using a 24bit rgb code).
rs.bold = ('sgr', 24)  # rs.all only resets the underline effect from now on.

a = ef.italic + 'This is not italic any more, but underlined' + rs.underline
b = fg.red + 'This is not red any more, but green.' + rs.fg
c = fg.blue + 'This is not blue any more, but red' + rs.fg
d = fg.my_new_item + 'This is a new brown attribute' + rs.fg
e = bg.green + 'This is not green bg any more, but blue.' + rs.bg
f = ef.bold + 'This does not reset bold any more' + rs.bold \
    + ' -> This is still bold' + rs.all

print(a, b, c, d, e, f, sep='\n')

print('\nDynamic attribute customization\n--------------------')
ef = EfRegister()
fg = FgRegister()
bg = BgRegister()
rs = RsRegister()

my_color_name = 'special_teal'

fg.set(my_color_name, 'eightbit', 51)

a = fg.special_teal + 'This is custom teal text.' + fg.rs

print(a)

print('\nExtending the default registers\n--------------------')
ef = EfRegister()
fg = FgRegister()
bg = BgRegister()
rs = RsRegister()

from sty.register import FgRegister


# Extend default Fg register.
class MyFgRegister(FgRegister):
    black = ('sgr', 31)
    red = ('sgr', 34)
    orange = ('rgb', (255, 128, 0))


fg = MyFgRegister()

a = fg.orange + 'This is custom orange text.' + rs.fg

print(a)

print('\nReplace or add renderers\n--------------------')
ef = EfRegister()
fg = FgRegister()
bg = BgRegister()
rs = RsRegister()

from sty.register import FgRegister


def rgb_bg(rgb: tuple):
    return f'\x1b[48;2;{str(rgb[0])};{str(rgb[1])};{str(rgb[2])}m'


# Extend default Fg register.
class MyFgRegister(FgRegister):

    def rgb(self, *args):
        return rgb_bg(*args)

    black = ('sgr', 31)
    red = ('sgr', 34)
    orange = ('rgb', (255, 128, 0))


fg = MyFgRegister()

a = fg.orange + 'I have a orange background instead of an orange fg.' + rs.bg

print(a)

print('\nChange call renderers\n--------------------')
ef = EfRegister()
fg = FgRegister()
bg = BgRegister()
rs = RsRegister()

from sty.register import FgRegister
from sty.renderer import rgb_bg, eightbit_bg


class MyFgRegister(FgRegister):

    def _num_call(self, num):
        return eightbit_bg(*num)  # default renderer is `eightbit`.

    def _rgb_call(self, *args):
        return rgb_bg(*args)  # default renderer is `rgb`.

    black = ('sgr', 31)
    red = ('sgr', 34)
    orange = ('rgb', (255, 128, 0))


fg = MyFgRegister()

a = fg(90) + 'Colored bg instead of colored fg.' + rs.bg
b = fg(40, 50, 200) + 'Colored bg instead of colored fg.' + rs.bg

print(a, b, sep='\n')
