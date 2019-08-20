
Renderers
=========

The default render-functions are stored in ``sty.renderfunc``.

Sty's default render function register
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: table-register

========================== ============================================================================================================================================================================
Render-Function            Description
========================== ============================================================================================================================================================================
sty.renderfunc.sgr         Render `SGR codes (wikipedia:SGR) <https://en.wikipedia.org/wiki/ANSI_escape_code#SGR_(Select_Graphic_Rendition)_parameters>`__ (works for fg-colors, bg-colors and effects)
sty.renderfunc.eightbit_fg Render foreground using `8bit color codes (wikipedia:8bit) <https://en.wikipedia.org/wiki/ANSI_escape_code#8-bit>`__
sty.renderfunc.eightbit_bg Render background using 8bit color codes
sty.renderfunc.rgb_fg      Render foreground using `24bit (RGB) color codes (wikipedia:24bit) <https://en.wikipedia.org/wiki/ANSI_escape_code#24-bit>`__
sty.renderfunc.rgb_bg      Render background using 24bit (RGB) color codes
========================== ============================================================================================================================================================================

