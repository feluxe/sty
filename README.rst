
.. image:: https://raw.githubusercontent.com/feluxe/sty/master/assets/README_logo_aliased.svg
   :target: https://raw.githubusercontent.com/feluxe/sty/master/assets/README_logo_aliased.svg
   :alt: sty_logo
   :width: 30%
   :class: intro-logo

|

|badge-total-downloads| |badge-monthly-downloads|

.. |badge-total-downloads| image:: https://static.pepy.tech/personalized-badge/sty?period=total&units=international_system&left_color=grey&right_color=lightgrey&left_text=downloads
   :target: https://static.pepy.tech/personalized-badge/sty?period=total&units=international_system&left_color=grey&right_color=lightgrey&left_text=downloads
   :alt: badge-total-downloads

.. |badge-monthly-downloads| image:: https://static.pepy.tech/personalized-badge/sty?period=month&units=international_system&left_color=grey&right_color=lightgrey&left_text=downloads/month
   :target: https://static.pepy.tech/personalized-badge/sty?period=month&units=international_system&left_color=grey&right_color=lightgrey&left_text=downloads/month
   :alt: badge-monthly-downloads

------------

.. image:: https://raw.githubusercontent.com/feluxe/sty/master/assets/README_demo.png
   :target: https://raw.githubusercontent.com/feluxe/sty/master/assets/README_demo.png
   :alt: sty_demo
   :width: 100%


Release 1.0.6 (November 27. 2023)
---------------------------------

Code Changes:

* Use PEP-484 compatible exports to satisfy static type checkers.


Release 1.0.5 (November 22. 2023)
---------------------------------

Code Changes:

* Add `py.typed` file for better typing support. Thanks! @Eisfunke
* Use explicit imports: `from .lib import` is now `from sty.lib import`.
* More and better doc-strings. `help(x)` should be much more useful now.

Other:

* Add svg logo. Thanks! @kubinka0505
* Replace `pipenv` with `poetry`.
* Remove `make.py` build system.
* Remove all dev dependencies.


Description
-----------

Sty's goal is to provide Python with a simple, customizable and performant string styling markup, which
is decoupled from color palettes and terminal implementations.

* Sty supports 3/4bit, 8bit and 24bit (truecolor/RGB) colors as well as effects like `bold`, `italic`, `underline`, etc.
* Sty should work on most Unix platforms with most terminals. It works with recent Windows terminals. Window legacy terminal (cmd) needs a `shim <https://github.com/feluxe/sty/issues/2#issuecomment-501890699>`__ to work.
* Sty comes with default color palettes and renderers, but you can easily replace/customize them, without touching the markup in your code.
* Sty allows you to mute/unmute all styles in your codebase.
* Sty provides high access performance for all styling rules.
* Sty is fully typed, you should get good editor support for it.
* Sty does not implicitly mess with globals. E.g.: `colorama` overrides `sys.stdout` which causes a lot of trouble.
* Sty has no dependencies.
* Sty follows `semver <https://semver.org/>`__.
* Sty will support Python `>=3.7` for as long as possible.

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
   :alt: example
   :width: 600px


You can use the `Register` class or the default registers `FgRegister`, `BgRegister`, `EfRegister` and `RsRegister` to create your own registers:

.. code:: python

    # Extending the default FgRegister

    from sty import FgRegister, Style, RgbFg, Sgr

    class MyFgRegister(FgRegister):

        def __init__(self):
            super().__init__()

            self.purple = Style(Sgr(35))
            self.blue = Style(Sgr(34))
            self.orange = Style(RgbFg(255, 128, 0))
            # ...

     fg = MyFgRegister()


Documentation
-------------

Documentation-Website: https://sty.mewo.dev

Documentation-Website-Source: https://github.com/feluxe/sty-docs

