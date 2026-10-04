#!/usr/bin/env python3
"""The documentation text"""


class BaseGeometry:
    """The class documentation text"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        elif value < 0:
            raise ValueError(f"{name} must be >= 0")
        else:
            pass
