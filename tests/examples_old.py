from sty import Rule, renderfunc, Render
from random import randint
from sty import EfRegister, FgRegister, BgRegister, RsRegister


def get_new_registers():
    ef = EfRegister()
    fg = FgRegister()
    bg = BgRegister()
    rs = RsRegister()

    return ef, fg, bg, rs


def getting_started(args):
    fg, bg, ef, rs = args

    # from sty import fg, bg, ef, rs, Render

    foo = fg.red + 'This is red text!' + fg.rs
    bar = bg.blue + 'This has a blue background!' + bg.rs
    baz = ef.italic + 'This is italic text' + rs.italic
    qux = fg(201) + 'This is pink text using 8bit colors' + fg.rs
    qui = fg(255, 10, 10) + 'This is red text using 24bit colors.' + fg.rs

    # Add new colors:

    fg.set_rule('orange', Rule(Render.rgb_fg, 255, 150, 50))

    buf = fg.orange + 'Yay, Im orange.' + fg.rs

    print(foo, bar, baz, qux, qui, buf, sep='\n')

    a = ef('italic') + 'Italic text.' + rs.italic
    b = fg('blue') + 'Blue text.' + rs.fg
    c = bg(randint(0, 254)) + 'Random colored bg' + rs.bg

    print(a, b, c, sep='\n')


def hello_world(args):
    fg, bg, ef, rs = args

    my_string = fg.black + bg.white + ef.bold + 'Hello world!' + rs.all
    print(my_string)


def italic(args):
    fg, bg, ef, rs = args

    a = ef.italic + 'Italic.' + rs.italic

    # There are shorthands for this:
    b = ef.i + fg.blue + 'Italic.' + rs.i + ' Not italic but blue.' + rs.fg

    print(a, b, sep='\n')


def bold():
    fg, bg, ef, rs = args

    a = ef.bold + 'Bold.' + rs.bold_dim

    # This has shorthands too:
    b = ef.b + 'Bold.' + rs.bold_dim + fg.li_yellow + ' Not bold but yellow.' + rs.fg

    print(a, b, sep='\n')


def underline():
    fg, bg, ef, rs = args

    a = ef.underl + 'Underlined.' + rs.underl

    # Shorthand version:
    b = ef.u + 'Underlined.' + rs.u + fg.green + ' Not underlined but green.' + rs.fg

    print(a, b, sep='\n')


def dim():

    a = ef.dim + fg.yellow + 'Dimmed yellow.' + rs.dim_bold + ' Undimmed yellow' + rs.fg

    print(a, sep='\n')


def blink():

    a = ef.blink + 'Blinking.' + rs.blink + ' Not blinking'

    print(a, sep='\n')


def inverse():

    a = ef.inverse + 'Inversed.' + rs.inverse + ' Not inversed'

    print(a, sep='\n')


def hidden():

    a = ef.hidden + 'Hidden.' + rs.hidden + ' Not Hidden'

    print(a, sep='\n')


def strike():

    a = ef.strike + 'Striked out.' + rs.strike + ' Not Striked out'

    print(a, sep='\n')


inverse()


def string_coloring_by_name():

    a = fg.li_blue + 'I have a light blue foreground.' + rs.fg
    b = bg.cyan + 'I have a cyan background' + rs.bg
    c = fg.da_red + bg.li_red + 'I have a dark red fg and light red bg.' + rs.all
    d = fg('yellow') + 'I have yellow fg.' + rs.fg

    print(a, b, c, d, sep='\n')


def string_coloring_by_8bit_number():

    a = fg(34) + 'I have a green foreground.' + rs.fg
    b = bg(133) + 'I have a pink background' + rs.bg
    c = fg(226
           ) + bg(19) + 'I have a light yellow fg and dark blue bg.' + rs.all

    print(a, b, c, sep='\n')


def string_coloring_by_24bit_rgb_number():

    a = fg(10, 255, 10) + 'I have a green foreground.' + rs.fg
    b = bg(255, 150, 50) + 'I have an orange background' + rs.bg
    c = fg(90, 90, 90) + bg(32, 32, 32) + 'Grey fg and dark grey bg.' + rs.all

    print(a, b, c, sep='\n')


def direct_attribute_customization():

    # ef.italic now renders underlined text.
    ef.set_rule('italic', Rule(Render.sgr, 4))

    # fg.red renders green text from now on.
    fg.set_rule('red', Rule(Render.sgr, 32))

    # fg.blue renders red text from now on (using an 8bit color code).
    fg.set_rule('blue', Rule(Render.eightbit_fg, 88))

    # Create a new item that renders brown text.
    fg.set_rule('my_new_item', Rule(Render.eightbit_fg, 130))

    # bg.green renders blue bg from now on (using a 24bit rgb code).
    bg.set_rule('green', Rule(Render.rgb_bg, 0, 128, 255))

    # rs.all only resets the underline effect from now on.
    rs.set_rule('bold_dim', Rule(Render.sgr, 24))

    a = ef.italic + 'This is not italic any more, but underlined' + rs.underl
    b = fg.red + 'This is not red any more, but green.' + rs.fg
    c = fg.blue + 'This is not blue any more, but red' + rs.fg
    d = fg.my_new_item + 'This is a new brown attribute' + rs.fg
    e = bg.green + 'This is not green bg any more, but blue.' + rs.bg
    f = ef.bold + 'This does not reset bold any more' + rs.bold_dim \
        + ' -> This is still bold' + rs.all

    print(a, b, c, d, e, f, sep='\n')


def direct_attribute_customization_with_multiple_rules():

    fg.set_rule('green_ul', Rule(Render.sgr, 32), Rule(Render.sgr, 4))
    fg.set_rule('red_i', Rule(Render.sgr, 31), ef.i)
    fg.blue_b = fg.blue + ef.b

    a = fg.green_ul + 'This is green and underline text.' + rs.all
    b = fg.red_i + 'This is red and italic text.' + rs.all
    c = fg.blue_b + 'This is blue and bold text.' + rs.all

    print(a, b, c, sep='\n')


def dynamic_attribute_customization():

    my_color_name = 'teal'

    fg.set_rule(my_color_name, Rule(Render.eightbit_fg, 51))

    a = fg.teal + 'This is custom teal text.' + fg.rs

    print(a)


def dynamic_attribute_customization_with_multiple_rules():

    my_color_name1 = 'teal_b'
    my_color_name2 = 'green_i'
    my_color_name3 = 'red_ul'

    fg.set_rule(
        my_color_name1, Rule(Render.eightbit_fg, 51), Rule(Render.sgr, 1)
    )
    fg.set_rule(my_color_name2, fg.green, ef.i)
    fg.set_rule(my_color_name3, Rule(Render.sgr, 31), ef.underl)

    a = fg.teal_b + 'This is custom teal and bold text.' + rs.all
    b = fg.green_i + 'This is green italic text.' + rs.all
    c = fg.red_ul + 'This is red and undelrined text.' + rs.all

    print(a, b, c, sep='\n')


def extending_the_default_registers():

    from sty.register import FgRegister, Rule, Render

    # Extend default Fg register.
    class MyFgRegister(FgRegister):

        orange = ''  # Set the new attribute here as well, for better editor support.

        def __init__(self):
            super().__init__()

            self.set_rule('black', Rule(Render.sgr, 31))
            self.set_rule('red', Rule(Render.sgr, 34))
            self.set_rule('orange', Rule(Render.rgb_fg, 255, 128, 0))

        # ...

    # Create a new instance from the new Register

    fg = MyFgRegister()

    a = fg.orange + 'This is orange text from a non default attribute.' + rs.fg

    print(a)


def replace_or_add_render_functions():

    from sty.register import FgRegister

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


def change_call_functions():

    from sty.register import FgRegister

    class MyFgRegister2(FgRegister):

        def __init__(self):
            super().__init__()
            self.set_renderfunc(Render.eightbit_bg, renderfunc.eightbit_bg)
            self.set_renderfunc(Render.rgb_bg, renderfunc.rgb_bg)

            self.set_eightbit_callfunc(Render.eightbit_bg)
            self.set_rgb_callfunc(Render.rgb_bg)

            self.set_rule('black', Rule(Render.sgr, 31))
            self.set_rule('red', Rule(Render.sgr, 34))
            self.set_rule('orange', Rule(Render.rgb_bg, 255, 128, 0))

    fg = MyFgRegister2()

    a = fg(90) + 'Colored bg instead of colored fg.' + rs.bg
    b = fg(40, 50, 200) + 'Colored bg instead of colored fg.' + rs.bg

    print(a, b, sep='\n')


def mute_formatting():

    fg.mute()

    a = fg.red + 'This red foreground was muted.' + fg.rs
    b = fg(10) + 'This green foreground was muted.' + fg.rs
    c = fg(100, 140, 180) + "This blue foreground was muted." + fg.rs

    fg.unmute()

    d = fg.red + 'The mute switch is off, so this is red.' + fg.rs
    e = fg(10) + 'The mute switch is off, so this is green.' + fg.rs
    f = fg(100, 140, 180) + 'The mute switch is off, so this is blue.' + fg.rs

    print(a, b, c, d, e, f, sep='\n')


def asdict():
    pass


def copy():
    pass
