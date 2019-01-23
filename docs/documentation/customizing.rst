
Customizing
===========

Sty allows you to change or to extend the default registers as you like.
You can also create a complete new register. More on these things in the
following chapters.


   .. rubric:: Warning:
      :name: warning:

   If you create a library that is shared among other projects, I highly
   suggest not to customize the "global" register-objects (sty.fg,
   sty.bg, sty.ef, sty.rs) directly, because that might cause conflicts
   with other packages that share the same sty dependency within the
   same project.

   If you want to use custom register-objects in a library project, you
   should create new register-object instances from the register-classes
   dedicated to your project only. More on this int the chapter
   *"Extending the default registers and creating new instances"*.



``set_style`` method
~~~~~~~~~~~~~~~~~~~~

Each register-object has a mehtod called ``set_style``, with it you can add or change styles for a register-object:

.. literalinclude:: ../../tests/docs/customizing.py
   :language: py
   :start-after: Example("customizing the register-objects: set_style")
   :end-before: # ===== End


Render Types
~~~~~~~~~~~~

To define the values for a style you have to use ``rendertypes``:

* ``Sgr(num: int)``
* ``EightbitFg(num: int)``
* ``EightbitBg(num: int)``
* ``RgbFg(r: int, g: int, b: int)``
* ``RgbBg(r: int, g: int, b: int)``


.. literalinclude:: ../../tests/docs/customizing.py
   :language: py
   :start-after: Example("customizing the register-objects: render_types")
   :end-before: # ===== End


``get_style`` method
~~~~~~~~~~~~~~~~~~~~

Each register-object has a method called ``get_style``. With it you can retrieve styling rules from a register-object.
This is useful in case you want to create new styles composed out of existing styles:

.. literalinclude:: ../../tests/docs/customizing.py
   :language: py
   :start-after: Example("customizing the register-objects: get_style")
   :end-before: # ===== End


``set_renderfunc`` method
~~~~~~~~~~~~~~~~~~~~~~~~~

Each register-object has a method called ``set_renderfunc``. With it you can add or replace render-functions for a given register-object:

.. literalinclude:: ../../tests/docs/customizing.py
   :language: py
   :start-after: Example("customizing the register-objects: render-func")
   :end-before: # ===== End


``set_eightbit_call`` and ``set_rgb_call`` methods
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remember that you can call the register-objects like a function:

.. code:: python

    fg(201) + 'This is pink text using 8bit colors' + fg.rs
    fg(255, 10, 10) + 'This is red text using 24bit colors.' + fg.rs


By default ``fg(201)`` invokes the eightbit foreground render-function and ``fg(255, 10, 10)`` invokes the rgb foreground render-function.

You can set custom rendertypes for these calls, like this:

.. literalinclude:: ../../tests/docs/customizing.py
   :language: py
   :start-after: Example("customizing the register-objects: calls")
   :end-before: # ===== End



Extending register-classes and creating new instances
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you want to set a larger register of custom attributes, it may be
more convenient to extend the default register-classes and create new
register-objects from them.

Customizing sty this way has some advantages:

* You get better editor support (mypy, pylint, etc).
* You aren't mutating sty's global register-objects (``sty.ef``, ``sty.fg``, etc.). This may be important for library projects.

In order to extend the register-classes we use the same functions as in the chapters above (``set_style``, ``set_renderfunc``, etc.):

.. literalinclude:: ../../tests/docs/customizing.py
   :language: py
   :start-after: Example("extending register-classes")
   :end-before: # ===== End


A register-class from scratch
-----------------------------

This example show how to create a complete register class from scratch:

.. literalinclude:: ../../tests/docs/customizing.py
   :language: py
   :start-after: Example("register-class from scratch")
   :end-before: # ===== End



This is exactly how the default register-classes are created in
``sty.register``.


