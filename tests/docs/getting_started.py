from random import randint

from .. import Example

print("\n\nGETTING STARTED\n" + "=" * 80)

# ===== Start =====
Example("gettings started: sty all the strings")
from sty import bg, ef, fg, rs

foo = fg.red + "This is red text!" + fg.rs
bar = bg.blue + "This has a blue background!" + bg.rs
baz = ef.italic + "This is italic text" + rs.italic
qux = fg(201) + "This is pink text using 8bit colors" + fg.rs
qui = fg(255, 10, 10) + "This is red text using 24bit colors." + fg.rs

# Add custom colors:

from sty import RgbFg, Style

fg.orange = Style(RgbFg(255, 150, 50))

buf = fg.orange + "Yay, Im orange." + fg.rs

print(foo, bar, baz, qux, qui, buf, sep="\n")
# ===== End =====

# ===== Start =====
Example("gettings started: select dynamically")
a = ef("italic") + "Italic text." + rs.italic
b = fg("blue") + "Blue text." + rs.fg
c = bg(randint(0, 254)) + "Random colored bg" + rs.bg

print(a, b, c, sep="\n")
# ===== End =====

# ===== Start =====
Example("gettings started: select 8bit and 24bit directly")
# select an 8bit color directly.
a = fg(196) + "This is red text" + rs.fg

# select a 24bit rgb color directly.
b = bg(50, 255, 50) + "Text with green bg" + rs.bg

print(a, b, sep="\n")
# ===== End =====

# ===== Start =====
Example("hello world")
my_string = fg.black + bg.white + ef.bold + "Hello world!" + rs.all
print(my_string)
# ===== End =====
