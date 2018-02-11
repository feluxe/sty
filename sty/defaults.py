from sty.render import sgr

ef = dict(
    b=sgr(1),
    bold=sgr(1),
    faint=sgr(2),
    i=sgr(3),
    italic=sgr(3),
    u=sgr(4),
    underline=sgr(4),
    blink_slow=sgr(5),
    blink_fast=sgr(6),
    reverse=sgr(7),
    conceal=sgr(8),
    strike=sgr(9),
)

fg = dict(
    # Classic terminal foreground color preset.
    # These are well supported.
    black=sgr(30),
    red=sgr(31),
    green=sgr(32),
    yellow=sgr(33),
    blue=sgr(34),
    magenta=sgr(35),
    cyan=sgr(36),
    white=sgr(37),

    rs=sgr(39),

    # These are less supported:
    li_black=sgr(90),
    li_red=sgr(91),
    li_green=sgr(92),
    li_yellow=sgr(93),
    li_blue=sgr(94),
    li_magenta=sgr(95),
    li_cyan=sgr(96),
    li_white=sgr(97),
)

bg = dict(

    # Classic terminal foreground color preset.
    # These are well supported.
    black=sgr(40),
    red=sgr(41),
    green=sgr(42),
    yellow=sgr(43),
    blue=sgr(44),
    magenta=sgr(45),
    cyan=sgr(46),
    white=sgr(47),

    rs=sgr(49),

    # These are less supported:
    li_black=sgr(100),
    li_red=sgr(101),
    li_green=sgr(102),
    li_yellow=sgr(103),
    li_blue=sgr(104),
    li_magenta=sgr(105),
    li_cyan=sgr(106),
    li_white=sgr(107),
)

rs = dict(
    all=sgr(0),
    fg=sgr(39),
    bg=sgr(49),
    b=sgr(21),
    bold=sgr(21),
    faint=sgr(22),
    i=sgr(23),
    italic=sgr(23),
    u=sgr(24),
    underline=sgr(24),
    blink=sgr(25),
    conceal=sgr(28),
    strike=sgr(29),
)
