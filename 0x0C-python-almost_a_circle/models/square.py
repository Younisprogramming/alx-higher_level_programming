#!/usr/bin/python3
"""Defines a class Square that inherits Rectangle."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ As you know, a Square is a special Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """doc ... """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ rht wtyh yher"""
        return self.width

    @size.setter
    def size(self, value):
        """ wrhe yrhe yhr"""
        self.width = value
        self.height = value

    def __str__(self):
        """ str method """
        return f'[Square] ({self.id}) {self.x}/{self.y} - {self.size}'
