#!/usr/bin/python3
"""uheoiwt uhet uhiewt iet u
 uireauahoud gr
 uoa eri

 """


class Rectangle:
    """eurjhg uhjseihse"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """e gr r rea ga frrega aer"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """wetg wey w tw yrt h"""
        if self.__height == 0 or self.__width == 0:
            return ''
        new_str = ''
        for i in range(self.__height - 1):
            new_str += (str(self.print_symbol) * self.width) + '\n'
        new_str += str(self.print_symbol) * self.width
        return new_str

    def __repr__(self):
        """reht reth wrht wrth r"""
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """srthwrht tr hydt hj"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ry 5er6 uer6 ue65 uw556 """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        area_1 = rect_1.width * rect_1.height
        area_2 = rect_2.width * rect_2.height

        if area_1 >= area_2:
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """weoitj roi ytwoijry """
        return cls(size, size)
