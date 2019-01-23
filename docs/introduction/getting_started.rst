

Getting Started
===============

Install:

::

   pip install sty

   

You can import sty like this:

.. code:: python

   import sty

However, if you need to style a lot of stuff, you might consider
importing the register-objects directly, like this:

.. code:: python

   from sty import fg, bg, ef, rs


*Sty* all the strings!
----------------------

.. literalinclude:: ../../tests/docs/getting_started.py
   :language: py
   :start-after: Example("gettings started: sty all the strings")
   :end-before: # ===== End

output:
 
.. image:: ../../assets/example_so.png
   :alt: example usage



A quick look at the primitives:
-------------------------------

sty provides a bunch of tiny, but flexible primitives (called register-objects) that can be used to style your strings: 

* ``ef`` (effect-register)
* ``fg`` (foreground-register)
* ``bg`` (background-register)
* ``rs`` (reset-register).

Each register-object carries a default selection of attributes (:ref:`effect-register <anchor_effect_register>`, :ref:`color-register <anchor_color_register>`, :ref:`reset-register <anchor_reset_register>`), which you can select like this:


.. code:: python

   ef.italic
   fg.blue
   bg.green
   rs.all

Or like this, which is nice in case you need to dynamically select
attributes:

.. literalinclude:: ../../tests/docs/getting_started.py
   :language: py
   :start-after: Example("gettings started: select dynamically")
   :end-before: # ===== End

``fg`` and ``bg`` are special in the way that they allow you to select
8bit and 24bit colors directly:

.. literalinclude:: ../../tests/docs/getting_started.py
   :language: py
   :start-after: Example("gettings started: select 8bit and 24bit directly")
   :end-before: # ===== End

I think this is all you need to know to get going. Check out the
documentation or the codebase for more detail or feel free to create an
issue and ask. Have fun! :D


