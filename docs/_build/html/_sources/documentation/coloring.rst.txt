
Coloring
========


Sty uses ANSI escape sequences for coloring.

More about ANSI colors on wikipedia:
`3/4bit colors <https://en.wikipedia.org/wiki/ANSI_escape_code#3/4_bit>`__
| `8bit colors <https://en.wikipedia.org/wiki/ANSI_escape_code#8-bit>`__
| `24bit colors <https://en.wikipedia.org/wiki/ANSI_escape_code#24-bit>`__.


.. _anchor_color_register:

Sty's default color register
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Foreground
----------

The default colors for the ``sty.fg`` register-object.

These are most widely supported. (using sgr codes).

======= ======================
normal  Default Renderer
======= ======================
black   sty.renderfunc.sgr(30)
red     sty.renderfunc.sgr(31)
green   sty.renderfunc.sgr(32)
yellow  sty.renderfunc.sgr(33)
blue    sty.renderfunc.sgr(34)
magenta sty.renderfunc.sgr(35)
cyan    sty.renderfunc.sgr(36)
white   sty.renderfunc.sgr(37)
======= ======================

These are less widely supported. (using less common set of sgr codes).

========== ======================
light      Default Renderer
========== ======================
li_black   sty.renderfunc.sgr(90)
li_red     sty.renderfunc.sgr(91)
li_green   sty.renderfunc.sgr(92)
li_yellow  sty.renderfunc.sgr(93)
li_blue    sty.renderfunc.sgr(94)
li_magenta sty.renderfunc.sgr(95)
li_cyan    sty.renderfunc.sgr(96)
li_white   sty.renderfunc.sgr(97)
========== ======================

These are even less widely supported. (using 8bit color codes).

========== ===============================
dark       Default Renderer
========== ===============================
da_black   sty.renderfunc.eightbit_fg(0)
da_red     sty.renderfunc.eightbit_fg(88)
da_green   sty.renderfunc.eightbit_fg(22)
da_yellow  sty.renderfunc.eightbit_fg(58)
da_blue    sty.renderfunc.eightbit_fg(18)
da_magenta sty.renderfunc.eightbit_fg(89)
da_cyan    sty.renderfunc.eightbit_fg(23)
da_white   sty.renderfunc.eightbit_fg(249)
========== ===============================

Background
----------

The default colors for the ``sty.bg`` register-object.

These are most widely supported. (using sgr codes).

======= ======================
normal  Default Renderer
======= ======================
black   sty.renderfunc.sgr(40)
red     sty.renderfunc.sgr(41)
green   sty.renderfunc.sgr(42)
yellow  sty.renderfunc.sgr(43)
blue    sty.renderfunc.sgr(44)
magenta sty.renderfunc.sgr(45)
cyan    sty.renderfunc.sgr(46)
white   sty.renderfunc.sgr(47)
======= ======================

These are less widely supported. (using less common set of sgr codes).

========== =======================
light      Default Renderer
========== =======================
li_black   sty.renderfunc.sgr(100)
li_red     sty.renderfunc.sgr(101)
li_green   sty.renderfunc.sgr(102)
li_yellow  sty.renderfunc.sgr(103)
li_blue    sty.renderfunc.sgr(104)
li_magenta sty.renderfunc.sgr(105)
li_cyan    sty.renderfunc.sgr(106)
li_white   sty.renderfunc.sgr(107)
========== =======================

These are even less widely supported. (using 8bit color codes).

========== ===============================
dark       Default Renderer
========== ===============================
da_black   sty.renderfunc.eightbit_bg(0)
da_red     sty.renderfunc.eightbit_bg(88)
da_green   sty.renderfunc.eightbit_bg(22)
da_yellow  sty.renderfunc.eightbit_bg(58)
da_blue    sty.renderfunc.eightbit_bg(18)
da_magenta sty.renderfunc.eightbit_bg(89)
da_cyan    sty.renderfunc.eightbit_bg(23)
da_white   sty.renderfunc.eightbit_bg(249)
========== ===============================


Coloring by name
~~~~~~~~~~~~~~~~

.. literalinclude:: ../../tests/docs/coloring.py
   :language: py
   :start-after: Example("coloring by name")
   :end-before: # ===== End

.. image:: ../../assets/color_by_name.png
   :alt: coloring by name


Coloring with 8-bit codes
~~~~~~~~~~~~~~~~~~~~~~~~~

Link:
`wikipedia:8bit <https://en.wikipedia.org/wiki/ANSI_escape_code#8-bit>`__

.. literalinclude:: ../../tests/docs/coloring.py
   :language: py
   :start-after: Example("coloring by 8bit number")
   :end-before: # ===== End

.. image:: ../../assets/8bit.png
   :alt: coloring by 8bit number


Coloring with 24bit codes
~~~~~~~~~~~~~~~~~~~~~~~~~

Link:
`wikipedia:24bit <https://en.wikipedia.org/wiki/ANSI_escape_code#24-bit>`__

.. literalinclude:: ../../tests/docs/coloring.py
   :language: py
   :start-after: Example("coloring by 24bit rgb number")
   :end-before: # ===== End

.. image:: ../../assets/24bit.png
   :alt: coloring by 24bit number



