from .. import Example

print("\n\nMUTING\n" + "=" * 80)

# ===== Start =====
Example("mute formatting")
from sty import fg

fg.mute()

a = fg.red + "This red forground was muted." + fg.rs
b = fg(10) + "This green foreground was muted." + fg.rs
c = fg(100, 140, 180) + "This blue foreground was muted." + fg.rs

fg.unmute()

d = fg.red + "The mute switch is off, so this is red." + fg.rs
e = fg(10) + "The mute switch is off, so this is green." + fg.rs
f = fg(100, 140, 180) + "The mute switch is off, so this is blue." + fg.rs

print(a, b, c, d, e, f, sep="\n")
# ===== End =====

# ===== Start =====
Example("mute formatting batch")
from sty import bg, ef, fg, mute, rs, unmute

a1 = fg.red + "This text is red." + fg.rs
a2 = bg.red + "This bg is red." + bg.rs
a3 = ef.italic + "This text is italic" + rs.italic

mute(fg, bg, ef, rs)

b1 = fg.red + "This text is NOT red." + fg.rs
b2 = bg.red + "This bg is NOT red." + bg.rs
b3 = ef.italic + "This text is NOT italic" + rs.italic

unmute(fg, bg, ef, rs)

c1 = fg.red + "This text is red." + fg.rs
c2 = bg.red + "This bg is red." + bg.rs
c3 = ef.italic + "This text is italic" + rs.italic

print(a1, a2, a3, b1, b2, b3, c1, c2, c3, sep="\n")
# ===== End =====
