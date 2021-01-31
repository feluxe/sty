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
from sty import RgbFg, Style, fg

fg_copy = fg.copy()
fg_no_copy = fg

fg.orange = Style(RgbFg(255, 200, 35))

# 'fg' and 'fg_no_copy' point to the same instance, therefore both can access 'orange':
assert hasattr(fg, "orange") == True
assert hasattr(fg_no_copy, "orange") == True

# fg_copy is not effected by the changes made to the global 'fg' register-object.
assert hasattr(fg_copy, "orange") == False
# ===== End =====
print("Copy works if no exception was thrown.")

