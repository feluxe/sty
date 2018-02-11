from sty import ef, fg, bg, rs, render

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

# Customizing name register

custom_register = dict(
    orange=render.eightbit_fg(214),  # Add 'orange' to fg (using 8-bit code)
    green=render.rgb_fg(255, 0, 0),  # Modify value for 'green' (using rgb code)
    blue=render.sgr(95),  # Turn 'blue' into magenta (using sgr code)
)

a = fg.green + 'I have a green foreground.' + rs.fg
b = fg.blue + 'I have a blue foreground.' + rs.fg

fg(custom_register)

c = fg.green + 'I have a red foreground now.' + rs.fg
d = fg.blue + 'I have a magenta foreground now.' + rs.fg
e = fg.orange + 'I was set orange by a newly registered color name.' + rs.fg

print(a, b, c, d, e, sep='\n')
