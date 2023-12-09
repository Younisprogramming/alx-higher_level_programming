#!/usr/bin/python3
""" rec. """
from models.base import Base
""" this is my file doc """


class Rectangle(Base):
    """class doc"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """ __init__ func doc """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ func1 """
        return self.__width

    @width.setter
    def width(self, value):
        """ func """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ func """
        return self.__height

    @height.setter
    def height(self, value):
        """ func """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ func """
        return self.__x

    @x.setter
    def x(self, value):
        """ func """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ fun """
        return self.__y

    @y.setter
    def y(self, value):
        """ fun """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ return the area of the Rectangle """
        return self.width * self.height

    def display(self):
        """ print Rectangle """
        for i in range(self.height):
            print('#' * self.width)
