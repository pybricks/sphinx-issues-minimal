:mod:`bugs <bugs>` -- Formatting issues
============================================================

.. module:: bugs

1. Default string values in overloaded functions
------------------------------------------------

Below, autodoc formats ``sep`` and ``end`` as::

    sep: str = "' '", end: str = "'\\n'"

But it should be::

    sep: str = "", end: str = "\n"

.. autofunction:: bugs.print_overloaded

2. Default values rendered as string literal
--------------------------------------------

Additionally the above seems to be a variant of `Bug 8693`_.

The default file is rendered as ``'sys.stdin'``.

.. _Bug 8693: https://github.com/sphinx-doc/sphinx/issues/8693

3. Overridden, overloaded class docstring return type rendered as ``None``
--------------------------------------------------------------------------

This shows ``--> None`` in the class signature, but it shouldn't.

.. autoclass:: bugs.MyComplex

This is the correct behavior.

.. autoclass:: bugs.MyBool
