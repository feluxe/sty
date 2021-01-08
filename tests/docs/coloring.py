from .. import Example

print("\n\nCOLORING\n" + "=" * 80)

# ===== Start =====
Example("coloring by name")
from sty import bg, fg, rs

a = fg.li_blue + "I have a light blue foreground." + rs.fg
b = bg.cyan + "I have a cyan background" + rs.bg
c = fg.da_red + bg.li_red + "I have a dark red fg and light red bg." + rs.all
d = fg("yellow") + "I have yellow fg." + rs.fg

print(a, b, c, d, sep="\n")
# ===== End =====

# ===== Start =====
Example("coloring by 8bit number")
from sty import bg, fg, rs

a = fg(34) + "I have a green foreground." + rs.fg
b = bg(133) + "I have a pink background" + rs.bg
c = fg(226) + bg(19) + "I have a light yellow fg and dark blue bg." + rs.all

print(a, b, c, sep="\n")
# ===== End =====

# ===== Start =====
Example("coloring by 24bit rgb number")
from sty import bg, fg, rs

a = fg(10, 255, 10) + "I have a green foreground." + rs.fg
b = bg(255, 150, 50) + "I have an orange background" + rs.bg
c = fg(90, 90, 90) + bg(32, 32, 32) + "Grey fg and dark grey bg." + rs.all

print(a, b, c, sep="\n")
# ===== End =====
