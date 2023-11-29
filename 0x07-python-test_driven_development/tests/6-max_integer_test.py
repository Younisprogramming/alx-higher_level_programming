#!/usr/bin/python3
"""Unittest for the max_integer module
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """TestCase for the max_integer function."""

    def test_regular(self):
        """Test with a regular list of ints: should return the max result"""
        m = [1, 2, 3, 4, 5]
        result = max_integer(m)
        self.assertEqual(result, 5)

    def test_m(self):
        """kbdfg ureil ugt rui reiqgual iruqegl"""
        m = [-1, -2, -3, 0]
        result = max_integer(m)
        self.assertEqual(result, 0)

    def test_t(self):
        """kbdfg ureil ugt rui reiqgual iruqegl"""
        m = [-1, 2, -9, 7]
        result = max_integer(m)
        self.assertEqual(result, 7)

    def test_ghgh(self):
        """kbdfg ureil ugt rui reiqgual iruqegl"""
        m = [100, 100 ,100]
        result = max_integer(m)
        self.assertEqual(result, 100)

    def test_hhh(self):
        """kbdfg ureil ugt rui reiqgual iruqegl"""
        m = [2.5, 2.6, 2.9]
        result = max_integer(m)
        self.assertEqual(result, 2.9)

    def test_ggghj(self):
        """kbdfg ureil ugt rui reiqgual iruqegl"""
        m = []
        result = max_integer(m)
        self.assertEqual(result, None)

    def test_one_number_in_a_list(self):
        """kbdfg ureil ugt rui reiqgual iruqegl"""
        self.assertEqual(max_integer([1]), 1)

    def test_string_number_in_a_list(self):
        """kbdfg ureil ugt rui reiqgual iruqegl"""
        with self.assertRaises(TypeError):
            max_integer([0, '1'])

    def test_tuple_in_a_list(self):
        """kbdfg ureil ugt rui reiqgual iruqegl"""
        with self.assertRaises(TypeError):
            max_integer([10, (20, 30)])

if  __name__ == '__main__':
    unittest.main()
