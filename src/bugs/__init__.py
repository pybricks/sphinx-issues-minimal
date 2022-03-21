"""
The following functions and exceptions can be used without importing anything.
"""

from typing import (
    overload,
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
