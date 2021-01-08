# type: ignore
from .. import Example

print("\n\nETC\n" + "=" * 80)

# ===== Start =====
Example("as dict")
from sty import fg as fg_obj

fg = fg_obj.as_dict()

a = fg["red"] + "I have a red fg." + fg["rs"]

print(a)
# ===== End =====

# ===== Start =====
Example("as namedtuple")
from sty import fg as fg_obj

fg = fg_obj.as_namedtuple()

a = fg.yellow + "I have a yellow fg." + fg.rs

print(a)
# ===== End =====

# ===== Start =====
Example("copy")
from sty import FgRegister, RgbFg
from sty import fg as fg_a

fg_b = fg_a

fg_c = fg_a.copy()

fg_a.set_style("orange", RgbFg(255, 200, 35))

a = fg_a.orange + "I have an orange fg." + fg.rs
b = fg_b.orange + "I have an orange fg too." + fg.rs

print(a, b, sep="\n")

try:
    msg = "But I have no orange fg, because I'm an earlier copy."
    fg_c.orange + msg + fg.rs
except AttributeError:
    print(msg)

# # ===== End =====
