#!/usr/bin/python3
""" rec. """
from models.base import Base
""" this is my file doc """


class Rectangle(Base):
    """class doc"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """ __init__ func doc """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """ func1 """
        return self.__width

    @width.setter
    def width(self, value):
        """ func2 """
        self.__width = value

    @property
    def height(self):
        """ fun3 """
        return self.__height

    @height.setter
    def height(self, value):
        """ func4 """
        self.__height = value

    @property
    def x(self):
        """ func5 """
        return self.__x

    @x.setter
    def x(self, value):
        """ func6 """
        self.__x = value

    @property
    def y(self):
        """ func7 """
        return self.__y

    @y.setter
    def y(self, value):
        """ func8 """
        self.__y = value
