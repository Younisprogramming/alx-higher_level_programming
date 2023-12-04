#!/usr/bin/python3
"""aaaaaaaaaaaaaaaaaaaaa"""


class BaseGeometry:
    """bbbbbbbbbbbbbbbbbbbb"""

    def area(self):
        """cccccccccccccccccc"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ddddddddddddddddddddddd"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
