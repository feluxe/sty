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
from sty.lib import *
from sty.primitive import Register, Style
from sty.register import BgRegister, EfRegister, FgRegister, RsRegister, bg, ef, fg, rs
from sty.rendertype import *
