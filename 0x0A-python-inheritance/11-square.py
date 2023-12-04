#!/usr/bin/python3
"""Defines a class Square that inherits from Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square using Rectangle."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int): The size of the new Square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """Compute the area of the Square."""
        return self._Rectangle__width * self._Rectangle__height

    def __str__(self):
        """Special method that returns a printable string."""
        return f"[Square] {self._Rectangle__width}/{self._Rectangle__height}"
