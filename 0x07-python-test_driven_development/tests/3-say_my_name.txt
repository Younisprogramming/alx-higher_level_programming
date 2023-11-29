=============================
The ``3-say_my_name`` module
=============================

Using ``say_my_name``
----------------------

import module:
	>>> say_my_name = __import__('3-say_my_name').say_my_name

str and str
	>>> say_my_name("salma", "sami")
	My name is salma sami

str and none
	>>> say_my_name("salma", "")
	My name is salma 

number and str
	>>> say_my_name("ahmed", 12)
	Traceback (most recent call last):
	TypeError: last_name must be a string

no first name
	>>> say_my_name("", "ahmed")
	My name is  ahmed

str and number
	>>> say_my_name(32, "salma")
	Traceback (most recent call last):
	TypeError: first_name must be a string
