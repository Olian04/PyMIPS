"""
MIPS:esk binding for python.
----------------------------

    >>> import pymips
    >>> s0 = Registry("s0", 1)
    >>> s1 = Registry("s1", 3)
    >>> addi(s0, zero, -2)
    >>> add(s1, s1, s0)
    >>> print(s0, s1)

"""
from pymips.register import (
    Registry, zero
)
from pymips.operation import (
    add, addi,
    beq
)
from pymips.config import config
