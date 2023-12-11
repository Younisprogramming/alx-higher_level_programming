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
        if self.y > 0:
            for i in range(self.y):
                print()
        for i in range(self.height):
            if self.x > 0:
                print(self.x * " ", end='')
            print('#' * self.width)

    def __str__(self):
        """  returns the object representation in a string format """
        i = self.id
        x = self.x
        y = self.y
        width = self.width
        height = self.height
        return f'[Rectangle] ({i}) {x}/{y} - {width}/{height}'

    def update(self, *args):
        """ update func. """
        self.id = args[0]
        if len(args) == 5:
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        elif len(args) == 4:
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
        elif len(args) == 3:
            self.width = args[1]
            self.height = args[2]
        elif len(args) == 2:
            self.width = args[1]
