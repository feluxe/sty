
Muting
======

The ``mute`` and ``unmute`` methods
-----------------------------------

Sometimes its useful to disable the formatting for a register-object.
You can do so by invoking the ``mute`` and ``unmute`` methods:

.. literalinclude:: ../../tests/docs/muting.py
   :language: py
   :start-after: Example("mute formatting")
   :end-before: # ===== End


The ``mute`` and ``unmute`` batch functions
-------------------------------------------

If you want to mute multiple register-objects at the same time you can
use the ``mute`` and ``unmute`` functions that you find in ``sty.mute``,
``sty.unmute``:

.. literalinclude:: ../../tests/docs/muting.py
   :language: py
   :start-after: Example("mute formatting batch")
   :end-before: # ===== End

