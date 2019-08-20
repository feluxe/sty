
Resetting
=========


Sty uses ANSI SGR parameters to reset previously applied styles.

More about ANSI Select Graphic Rendition (SGR) on wikipedia:
`ANSI SGR <https://en.wikipedia.org/wiki/ANSI_escape_code#SGR_(Select_Graphic_Rendition)_parameters>`__

.. _anchor_reset_register:

Sty's default reset register
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

These are the default attributes for the ``sty.rs`` register-object:

.. rst-class:: table-register

================ ======================
Attribute        Default Renderer
================ ======================
all              sty.renderfunc.sgr(0)
fg               sty.renderfunc.sgr(39)
bg               sty.renderfunc.sgr(49)
bold_faint       sty.renderfunc.sgr(22)
faint_bold       sty.renderfunc.sgr(22)
italic (alias i) sty.renderfunc.sgr(23)
underl (alias u) sty.renderfunc.sgr(24)
blink            sty.renderfunc.sgr(25)
hidden           sty.renderfunc.sgr(28)
strike           sty.renderfunc.sgr(29)
================ ======================

