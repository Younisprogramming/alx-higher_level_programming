#!/usr/bin/python3
""" this is my doc .... """


class Base():
    """ this is my class doc. """

    __nb_objects = 0
    def __init__(self, id=None):
        """ this is my func. doc """
        if id is not None:
            self.id = id
        else:
            __nb_objects++
            self.id = __nb_objects
