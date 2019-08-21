
Effects
=======

Sty uses ANSI SGR parameters to apply effects. More about ANSI Select Graphic Rendition (SGR) on wikipedia:
`ANSI SGR <https://en.wikipedia.org/wiki/ANSI_escape_code#SGR_(Select_Graphic_Rendition)_parameters>`__


.. _anchor_effect_register:

Sty's default effect register
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

These are the default attributes for the ``sty.ef`` register-object.

.. rst-class:: table-register

================ ============================ =====================
Attribute        Description                  Default Renderer
================ ============================ =====================
bold (alias b)   Bold or increased intensity  sty.renderfunc.sgr(1)
dim              Decreased intensity          sty.renderfunc.sgr(2)
italic (alias i) Italic..                     sty.renderfunc.sgr(3)
underl (alias u) Underline..                  sty.renderfunc.sgr(4)
blink            Blink..                      sty.renderfunc.sgr(5)
inverse          Inverse fore- and background sty.renderfunc.sgr(7)
hidden           Conceal/Hide                 sty.renderfunc.sgr(8)
strike           Strike-trhough               sty.renderfunc.sgr(9)
================ ============================ =====================

Italic
~~~~~~

.. literalinclude:: ../../tests/docs/effects.py
   :language: py
   :start-after: Example("italic")
   :end-before: # ===== End

.. image:: ../../assets/italic.png
   :alt: italic example


Bold
~~~~

.. literalinclude:: ../../tests/docs/effects.py
   :language: py
   :start-after: Example("bold")
   :end-before: # ===== End

.. image:: ../../assets/bold.png
   :alt: bold example


Underline
~~~~~~~~~

.. literalinclude:: ../../tests/docs/effects.py
   :language: py
   :start-after: Example("underline")
   :end-before: # ===== End

.. image:: ../../assets/underline.png
   :alt: underline example


TODO:
~~~~~

Add examples for, strike, blink, etc..

