from sty.register import FgRegister, BgRegister, RsRegister, EfRegister

# Reset items
ef = EfRegister()
fg = FgRegister()
bg = BgRegister()
rs = RsRegister()

# Getting Started

print('\n')

foo = fg.red + 'This is red text!' + fg.rs
bar = bg.blue + 'This has a blue background!' + bg.rs
baz = ef.italic + 'This is italic text' + rs.italic
qux = fg(201) + 'This is pink text using 8bit colors' + fg.rs
qui = fg(255, 10, 10) + 'This is red text using 24bit colors.' + fg.rs

# Add new colors:


fg.orange = ('rgb', (255, 150, 50))

buf = fg.orange + 'Yay, Im orange.' + fg.rs

print(foo, bar, baz, qux, qui, buf, sep='\n')

# Hello World!

my_string = fg.black + bg.white + ef.bold + 'Hello world!' + rs.all
print(my_string)

# Italic:

a = ef.italic + 'Italic.' + rs.italic

# There are shorthands for this:
b = ef.i + fg.blue + 'Italic.' + rs.i + ' Not italic but blue.' + rs.fg

print(a, b, sep='\n')

# Bold:

a = ef.bold + 'Bold.' + rs.bold

# This has shorthands too:
b = ef.b + 'Bold.' + rs.b + fg.li_yellow + ' Not bold but yellow.' + rs.fg

print(a, b, sep='\n')

# Underlining:

a = ef.underline + 'Underlined.' + rs.underline

# Shorthand version:
b = ef.u + 'Underlined.' + rs.u + fg.green + ' Not underlined but green.' + rs.fg

print(a, b, sep='\n')

# String coloring by name:

a = fg.blue + 'I have a blue foreground.' + rs.fg
b = bg.li_cyan + 'I have a light cyan background' + rs.bg
c = fg.red + bg.green + 'I have a red fg and green bg.' + rs.all

print(a, b, c, sep='\n')

# String coloring by 8-bit number:

a = fg(34) + 'I have a green foreground.' + rs.fg
b = bg(133) + 'I have a pink background' + rs.bg
c = fg(226) + bg(19) + 'I have a light yellow fg and dark blue bg.' + rs.all

print(a, b, c, sep='\n')

# String coloring by 24-bit RGB value:

a = fg(10, 255, 10) + 'I have a green foreground.' + rs.fg
b = bg(255, 150, 50) + 'I have an orange background' + rs.bg
c = fg(90, 90, 90) + bg(32, 32, 32) + 'Grey fg and dark grey bg.' + rs.all

print(a, b, c, sep='\n')

### Direct attribute customization


ef.italic = ('sgr', 1)  # ef.italic now renders bold text.
fg.red = ('sgr', 32)  # fg.red renders green text from now on.
fg.blue = ('eightbit',
           111)  # fg.blue renders blue text from now on (using an 8bit color code).
fg.my_new_item = ('eightbit', 130)  # Create a new item that renders brown text.
bg.green = ('rgb', (0, 128,
                    255))  # bg.green renders blue text from now on (using a 24bit rgb code).
rs.bold = ('sgr', 24)  # rs.all only resets the underline effect from now on.

a = ef.italic + 'This is not italic any more' + rs.italic
b = fg.red + 'This is not red any more.' + rs.fg
c = fg.blue + 'This is not blue any more' + rs.fg
d = fg.my_new_item + 'This is a new attribute' + rs.fg
e = bg.green + 'This is not green bg any more.' + rs.bg
f = 'This does not reset bold any more' + rs.bold + ' -> This is still bold' + rs.all

print(a, b, c, d, e, f, sep='\n')

# Reset items
ef = EfRegister()
fg = FgRegister()
bg = BgRegister()
rs = RsRegister()

### Dynamic attribute customization

my_color_name = 'special_teal'

fg.set(my_color_name, 'eightbit', 51)

a = fg.special_teal + 'This is teal text.' + fg.rs

print(a)

# Reset items
ef = EfRegister()
fg = FgRegister()
bg = BgRegister()
rs = RsRegister()

### Extending the default registers

from sty.register import FgRegister


# Extend default Fg register.
class MyFgRegister(FgRegister):
    black = ('sgr', 31)
    red = ('sgr', 34)
    orange = ('rgb', (255, 128, 0))


fg = MyFgRegister()

a = fg.orange + 'This is orange text.' + rs.fg

print(a)

# Reset items
ef = EfRegister()
fg = FgRegister()
bg = BgRegister()
rs = RsRegister()

### Replace or add renderers

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
# Reset items
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

a = fg(90) + 'I have a colored background now.' + rs.bg
b = fg(40, 50, 200) + 'I have a colored background now.' + rs.bg

print(a, b, sep='\n')
