:mod:`bugs <bugs>` -- Formatting issues
============================================================

.. module:: bugs

Default string values in overloaded functions
---------------------------------------------

Below, autodoc formats ``sep`` and ``end`` as::

    sep: str = "' '", end: str = "'\\n'"

But it should be::

    sep: str = "", end: str = "\n"

.. autofunction:: bugs.print_overloaded
