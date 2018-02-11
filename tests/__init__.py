from tests import test_ansi_values
from tests import examples
from tests import charts


from sty.register import DefaultFg
from sty.render import sgr

class MyFg(DefaultFg):
    # Classic terminal foreground color preset.
    # These are well supported.
    black = sgr(31)
    red = sgr(34)

fg = MyFg()


