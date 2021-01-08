from .. import Example

print("\n\nEFFECTS\n" + "=" * 80)

# ===== Start =====
Example("italic")
from sty import ef, fg, rs

a = ef.italic + "Italic." + rs.italic

# There are shorthands for this:
b = ef.i + fg.blue + "Italic." + rs.i + " Not italic but blue." + rs.fg

print(a, b, sep="\n")
# ===== End =====

# ===== Start =====
Example("bold")
from sty import ef, fg, rs

a = ef.bold + "Bold." + rs.bold_dim

# This has shorthands too:
b = ef.b + "Bold." + rs.bold_dim + fg.li_yellow + " Not bold but yellow." + rs.fg

print(a, b, sep="\n")
# ===== End =====

# ===== Start =====
Example("underline")
from sty import ef, fg, rs

a = ef.underl + "Underlined." + rs.underl

# Shorthand version:
b = ef.u + "Underlined." + rs.u + fg.green + " Not underlined but green." + rs.fg

print(a, b, sep="\n")
# ===== End =====

# ===== Start =====
Example("dim")
from sty import ef, fg, rs

a = ef.dim + fg.yellow + "Dimmed yellow." + rs.dim_bold + " Undimmed yellow" + rs.fg

print(a, sep="\n")
# ===== End =====

# ===== Start =====
Example("blink")
from sty import ef, rs

a = ef.blink + "Blinking." + rs.blink + " Not blinking"

print(a, sep="\n")
# ===== End =====

# ===== Start =====
Example("inverse")
from sty import ef, rs

a = ef.inverse + "Inversed." + rs.inverse + " Not inversed"

print(a, sep="\n")
# ===== End =====

# ===== Start =====
Example("hidden")
from sty import ef, rs

a = ef.hidden + "Hidden." + rs.hidden + " Not Hidden"

print(a, sep="\n")
# ===== End =====

# ===== Start =====
Example("strike")
from sty import ef, rs

a = ef.strike + "Striked out." + rs.strike + " Not Striked out"

print(a, sep="\n")
# ===== End =====

# ===== Start =====
Example("Reset multiple effects")
from sty import ef

a = ef.strike + ef.underl + "Striked out and underlined." + rs.all + " No more effects."

print(a, sep="\n")
# ===== End =====
