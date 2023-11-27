"""
String styling for your terminal.

Documentation: https://sty.mewo.dev
Source Code: https://github.com/feluxe/sty

Example: Print bold text with red foreground, green background and reset:

    from sty import fg, bg, ef, rs

    print(f"{ef.b}{fg.red}{bg.green}My String{rs.all}")

Example: Create custom style:

    from sty import RgbFg, Style

    fg.orange = Style(RgbFg(255, 150, 50))

Example: Create your own register:

    from sty import FgRegister, RgbFg, Sgr

    class MyFgRegister(FgRegister):
        def __init__(self):
            super().__init__()

            self.purple = Style(Sgr(35))
            self.blue = Style(Sgr(34))
            # ...

    fg = MyFgRegister()

For more info see the docs.
"""

# NOTE: These are PEP-484 compatible exports using "*" and "... as ...".
from sty.lib import *

from sty.primitive import Register as Register
from sty.primitive import Style as Style

from sty.register import BgRegister as BgRegister
from sty.register import EfRegister as EfRegister
from sty.register import FgRegister as FgRegister
from sty.register import RsRegister as RsRegister
from sty.register import bg as bg
from sty.register import ef as ef
from sty.register import fg as fg
from sty.register import rs as rs

from sty.rendertype import *
