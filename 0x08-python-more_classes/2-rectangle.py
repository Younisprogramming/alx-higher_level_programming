#!/usr/bin/python3
"""uheoiwt uhet uhiewt iet u
 uireauahoud gr
 uoa eri

 """


class Rectangle:
    """eurjhg uhjseihse"""

    def __init__(self, width=0, height=0):
        """e gr r rea ga frrega aer"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """hi uig  giulyy uo 8igy8 oy"""
        return self.__width

    @width.setter
    def width(self, value):
        """ioserjgoiwe uhoaehrg qeroi gkq"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """oietjg ijetyoi oeji5y gq"""
        return self.__height

    @height.setter
    def height(self, value):
        """ get qerg t"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """iwrhg  uiqeth guwe g"""
        return self.__width * self.__height

    def perimeter(self):
        """uqiot5 uiwe thiue thgu"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
