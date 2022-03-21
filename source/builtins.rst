Built-in classes and functions
=====================================================

The classes and functions shown on this page can be used without
importing anything.

Input and output
------------------------

.. autofunction:: ubuiltins.input

.. autofunction:: ubuiltins.print

Basic types
---------------------------

.. autoclass:: ubuiltins.bool

.. autoclass:: ubuiltins.complex

.. autoclass:: ubuiltins.dict

.. autoclass:: ubuiltins.float

..
   _comment: The int class is defined manually because otherwise the classmethod is hidden, see https://github.com/pybricks/pybricks-api/issues/86

.. autoclass:: ubuiltins.int
    :no-members:

    .. automethod:: ubuiltins.int.to_bytes

    .. classmethod:: from_bytes(bytes: Union[bytes, bytearray], byteorder: Literal["little", "big"]) -> int

        Returns the integer represented by the given bytes.

        :param bytes: The bytes to convert.
        :param byteorder: Determines the byte order used to represent the
            integer. If byteorder is ``"big"``, the most significant byte is at
            the beginning of the byte sequence. If byteorder is ``"little"``,
            the most significant byte is at the end of the byte sequence.

        :returns: The integer represented by the bytes.


.. autoclass:: ubuiltins.object

.. autoclass:: ubuiltins.type

Sequences
---------------------------

.. autoclass:: ubuiltins.bytearray

.. autoclass:: ubuiltins.bytes

.. autofunction:: ubuiltins.len

.. autoclass:: ubuiltins.list

.. autoclass:: ubuiltins.slice

.. autoclass:: ubuiltins.str

.. autoclass:: ubuiltins.tuple

Iterators
--------------------------

.. autofunction:: ubuiltins.all

.. autofunction:: ubuiltins.any

.. autoclass:: ubuiltins.enumerate

.. autofunction:: ubuiltins.iter

.. autofunction:: ubuiltins.map

.. autofunction:: ubuiltins.next

.. autoclass:: ubuiltins.range

.. autofunction:: ubuiltins.reversed

.. autofunction:: ubuiltins.sorted

.. autofunction:: ubuiltins.zip

Conversion functions
------------------------

.. autofunction:: ubuiltins.bin

.. autofunction:: ubuiltins.chr

.. autofunction:: ubuiltins.hex

.. autofunction:: ubuiltins.oct

.. autofunction:: ubuiltins.ord

.. autofunction:: ubuiltins.repr

.. _builtinmath:

Math functions
----------------------

See also :mod:`umath` for floating point math operations.

.. autofunction:: ubuiltins.abs

.. autofunction:: ubuiltins.divmod

.. autofunction:: ubuiltins.max

.. autofunction:: ubuiltins.min

.. autofunction:: ubuiltins.pow

.. autofunction:: ubuiltins.round

.. autofunction:: ubuiltins.sum

Runtime functions
-------------------------

.. autofunction:: ubuiltins.eval

.. autofunction:: ubuiltins.exec

.. autofunction:: ubuiltins.globals

.. autofunction:: ubuiltins.hash

.. autofunction:: ubuiltins.help

.. autofunction:: ubuiltins.id

.. autofunction:: ubuiltins.locals


Class functions
------------------------

.. autofunction:: ubuiltins.callable

.. autofunction:: ubuiltins.dir

.. autofunction:: ubuiltins.getattr

.. autofunction:: ubuiltins.hasattr

.. autofunction:: ubuiltins.isinstance

.. autofunction:: ubuiltins.issubclass

.. autofunction:: ubuiltins.setattr

.. autofunction:: ubuiltins.super


Method decorators
-----------------

.. autodecorator:: ubuiltins.classmethod

.. autodecorator:: ubuiltins.staticmethod
