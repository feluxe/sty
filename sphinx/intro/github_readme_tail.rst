

Install
-------

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

.. code:: python

    from sty import fg, bg, ef, rs, RgbFg

    foo = fg.red + 'This is red text!' + fg.rs
    bar = bg.blue + 'This has a blue background!' + bg.rs
    baz = ef.italic + 'This is italic text' + rs.italic
    qux = fg(201) + 'This is pink text using 8bit colors' + fg.rs
    qui = fg(255, 10, 10) + 'This is red text using 24bit colors.' + fg.rs

    # Add new colors:

    fg.set_style('orange', RgbFg(255, 150, 50))

    buf = fg.orange + 'Yay, Im orange.' + fg.rs

    print(foo, bar, baz, qux, qui, buf, sep='\n')



.. image:: https://raw.githubusercontent.com/feluxe/sty/master/assets/example_so.png
   :target: https://raw.githubusercontent.com/feluxe/sty/master/assets/example_so.png
   :align: center
   :alt: examples
   :width: 600px



Documentation
-------------

https://sty.mewo.dev
