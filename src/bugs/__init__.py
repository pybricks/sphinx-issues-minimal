"""
The following functions and exceptions can be used without importing anything.
"""

from typing import (
    overload,
    Any,
    Union,
    SupportsComplex,
    SupportsFloat,
)

import io
import sys


@overload
def print_overloaded(*objects):
    ...


@overload
def print_overloaded(*objects, sep: str = " ", end: str = "\n", file: io.FileIO = sys.stdin):
    ...


def print_overloaded(*args):
    """
    Prints text or other objects in the terminal window.

    Arguments:
        args: One or more objects to print.

    Keyword Arguments:
        sep: This is printed between objects, if there is more than one.
        end: This is printed after the last object.
        file: By default, the result is printed in the terminal window. This argument lets you print it to a file instead.
    """


class MyBool:
    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, x: Any) -> None:
        ...

    def __init__(self, *args) -> None:
        """
        Creates a boolean value, which is either ``True`` or ``False``.

        Arguments:
            x: Value that is tested for being ``True`` or ``False``. It is
               converted using the standard truth testing procedure.

        Returns:
            Result of the truth-test. If no object is given, it returns ``False``.
        """


class MyComplex:
    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(
        self, real: Union[float, SupportsFloat, complex, SupportsComplex]
    ) -> None:
        ...

    @overload
    def __init__(
        self,
        real: Union[float, SupportsFloat, complex, SupportsComplex],
        imag: Union[float, SupportsFloat, complex, SupportsComplex],
    ) -> None:
        ...

    @overload
    def __init__(self, value: str) -> None:
        ...

    def __init__(self, *args) -> None:
        """MyComplex()
        MyComplex(string: str)
        MyComplex(a: Union[float, complex], b: Union[float, complex] = 0)

        Creates a complex number from a string or from a pair of numbers.

        If a string is given, it must be of the form ``'1+2j'``.
        If a pair of numbers is provided, the result is computed
        as: ``a + b * j``.

        Arguments:
            string: A string of the form ``'1+2j'`` .
            a: A real-valued or complex number.
            b: A real-valued or complex number.

        Returns:
            Complex number, obtained from the string or as the result of ``a + b * j``.
        """
