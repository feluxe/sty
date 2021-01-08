
.. image:: https://raw.githubusercontent.com/feluxe/sty/master/assets/README_logo.png
   :target: https://raw.githubusercontent.com/feluxe/sty/master/assets/README_logo.png
   :align: center
   :alt: sty_logo

------------

.. image:: https://raw.githubusercontent.com/feluxe/sty/master/assets/README_demo.png
   :target: https://raw.githubusercontent.com/feluxe/sty/master/assets/README_demo.png
   :align: center
   :alt: sty_demo
   :width: 600px

Release 1.0.0-rc.0 (January 08. 2021)
-------------------------------------

Sty version `1.0.0` is now feature complete.

* I'm going to support Python version `>=3.7` indefinitely.
* Sty will follow `semver` so there won't be any breaking changes for version `1.x.x`. This release is the last one with breaking changes.
* This is a pre-release (`rc.0`). I'll release `1.0.0` in a couple of month if no major bugs are reported.

`Breaking Changes <https://github.com/feluxe/sty/releases/tag/1.0.0-rc.0>`__


Description
-----------

Simple, flexible and extensible string styling for your terminal.
Supports 3/4bit, 8bit and 24bit (truecolor, rgb) colors. Should work on most
Unix platfroms with most terminals. Works with recent Windows terminals. Window
legacy terminal (cmd) needs a `shim <https://github.com/feluxe/sty/issues/2#issuecomment-501890699>`__ to work.

Sty comes with default color palettes and renderers, but you can easily
replace/customize them, without touching the markup.

Sty's goal is to provide Python with a little string styling markup, which
is decoupled from color palettes and terminal implementations.

Sty has no dependencies.

If you run into compatibility problems with sty, please file an `issue <https://github.com/feluxe/sty/issues>`__!


Code Example
------------

.. code:: python

    from sty import fg, bg, ef, rs

    foo = fg.red + 'This is red text!' + fg.rs
    bar = bg.blue + 'This has a blue background!' + bg.rs
    baz = ef.italic + 'This is italic text' + rs.italic
    qux = fg(201) + 'This is pink text using 8bit colors' + fg.rs
    qui = fg(255, 10, 10) + 'This is red text using 24bit colors.' + fg.rs

    # Add custom colors:

    from sty import Style, RgbFg

    fg.orange = Style(RgbFg(255, 150, 50))

    buf = fg.orange + 'Yay, Im orange.' + fg.rs

    print(foo, bar, baz, qux, qui, buf, sep='\n')

The code above will print like this in the terminal:

.. image:: https://raw.githubusercontent.com/feluxe/sty/master/assets/README_example.png
   :target: https://raw.githubusercontent.com/feluxe/sty/master/assets/README_example.png
   :align: center
   :alt: example
   :width: 600px


Documentation
-------------

Documentation-Website: https://sty.mewo.dev

Documentation-Website-Source: https://github.com/feluxe/sty-docs

