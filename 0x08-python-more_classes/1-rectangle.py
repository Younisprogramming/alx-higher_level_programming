#!/usr/bin/python3
"""theis is a doc ... """


class Rectangle:
    """this is ths dc inside my class"""

    def __init__(self, width=0, height=0):
        """Initialization of the data."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter method to retrieve."""
        return self.__width

    @width.setter
    def width(self, value):
        """aaaaaa bbbbbbb ccccccc"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method to retrieve."""
        return self.__height

    @height.setter
    def height(self, value):
        """aaaaaa bbbbbbb ccccccc"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
