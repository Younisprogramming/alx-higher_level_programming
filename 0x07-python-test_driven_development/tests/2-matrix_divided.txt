================================
The ``2-matrix_divided`` module
================================

Using ``matrix_divided``
------------------------

Import the function:

    >>> matrix_divided = __import__('2-matrix_divided').matrix_divided

Now test it:

    >>> matrix_divided([[1, 2, 3], [4, 5, 6]], 3)
    [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]

    >>> matrix_divided([["Hello", "Holberton"], [6, 7]], 3)
    Traceback (most recent call last):
    TypeError: matrix must be a matrix (list of lists) of integers/floats

    >>> matrix_divided([[3, 4, 5], [6, 7]], 3)
    Traceback (most recent call last):
    TypeError: Each row of the matrix must have the same size

    >>> matrix_divided([[3, 4], [6, 7]], "Hello")
    Traceback (most recent call last):
    TypeError: div must be a number

    >>> matrix_divided("Hello", 9)
    Traceback (most recent call last):
    TypeError: matrix must be a matrix (list of lists) of integers/floats

    >>> matrix_divided([[3, 4], [6, 7]], 0)
    Traceback (most recent call last):
    ZeroDivisionError: division by zero

    >>> matrix_divided([[3, 4], [6, 7]], -2)
    [[-1.5, -2.0], [-3.0, -3.5]]


    >>> matrix_divided([[3, 4]])
    Traceback (most recent call last):
    TypeError: matrix_divided() missing 1 required positional argument: 'div'

    >>> matrix_divided()
    Traceback (most recent call last):
    TypeError: matrix_divided() missing 2 required positional arguments: 'matrix' and 'div'

	Dividing a matrix by a float number:

    >>> matrix_divided([[10, 20, 30], [1.33, 3.74, 6.89], [-8, -9.71, 0]], 5.3)
    [[1.89, 3.77, 5.66], [0.25, 0.71, 1.3], [-1.51, -1.83, 0.0]]

Passing an empty matrix:

    >>> matrix_divided([], 10)
    Traceback (most recent call last):
    	      ...
    TypeError: matrix must be a matrix (list of lists) of integers/floats

Passing a tuple as an argument:

    >>> matrix_divided((3, 6, 9), 3)
    Traceback (most recent call last):
    	      ...
    TypeError: matrix must be a matrix (list of lists) of integers/floats

Dividing a matrix which its rows don't have the same size:

    >>> matrix_divided([[22, 34], [2.78, 7.1, -10, 2], [-8]], 3)
    Traceback (most recent call last):
    	      ...
    TypeError: Each row of the matrix must have the same size

Dividing a matrix which its rows don't have the same size 2:

    >>> matrix_divided([[2, 4], [6.8], [10, 12]], 12)
    Traceback (most recent call last):
    	      ...
    TypeError: Each row of the matrix must have the same size

Dividing a matrix which its elements aren't integer/float numbers:

    >>> matrix_divided([["Hello", "World"], ["Hello", "Holberton"]], 10)
    Traceback (most recent call last):
     	       ...
    TypeError: matrix must be a matrix (list of lists) of integers/floats
