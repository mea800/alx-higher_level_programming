#!/usr/bin/python3
"""Defines"""


from unittest.mock import patch
import unittest
import json
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquareMethods(unittest.TestCase):
    """ Defines """

    def setUp(self):
        """ Method """
        Base._Base__nb_objects = 0

    def tearDown(self):
        """ Cleans up  """
        pass

    def test_new_square(self):
        """ Test  """
        s1 = Square(3)
        s2 = Square(1, 2, 3, 4)
        self.assertEqual(s1.size, 3)
        self.assertEqual(s1.width, 3)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s2.size, 1)
        self.assertEqual(s2.width, 1)
        self.assertEqual(s2.x, 2)
        self.assertEqual(s2.y, 3)
        self.assertEqual(s2.id, 4)

    def test_attributes_1(self):
        """ Test """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("1")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "2")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, "3")

    def test_attributes_2(self):
        """ Test """
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1)
            Square(0)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(1, -2)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(1, 2, -3)

    def test_constructor_no_args(self):
        """ Tests  """
        with self.assertRaises(TypeError) as e:
            r = Square()
        s = "__init__() missing 1 required positional argument: 'size'"
        self.assertEqual(str(e.exception), s)

    def test_C_constructor_many_args(self):
        """ Tests"""
        with self.assertRaises(TypeError) as e:
            r = Square(1, 2, 3, 4, 5)
        s = "__init__() takes from 2 to 5 positional arguments but 6 \
were given"
        self.assertEqual(str(e.exception), s)

    def test_is_Rectangle_instance(self):
        """ Test """
        s1 = Square(1)
        self.assertEqual(True, isinstance(s1, Rectangle))

    def test_area(self):
        """ Test area method """
        s1 = Square(4)
        self.assertEqual(s1.area(), 16)

    def test_area_2(self):
        """ Test  """
        r1 = Square(4)
        self.assertEqual(r1.area(), 16)
        r1.size = 9
        self.assertEqual(r1.area(), 81)

    def test_area_no_args(self):
        """ Test"""
        r = Square(5)
        with self.assertRaises(TypeError) as e:
            Square.area()
        s = "area() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), s)

    def test_load_from_file(self):
        """ Test """
        load_file = Square.load_from_file()
        self.assertEqual(load_file, load_file)

    def test_basic_display(self):
        """ Test  """
        s1 = Square(6)
        result = "######\n######\n######\n######\n######\n######\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            s1.display()
            self.assertEqual(str_out.getvalue(), result)

    def test_display_no_args(self):
        """ Test"""
        r = Square(9)
        with self.assertRaises(TypeError) as e:
            Square.display()
        s = "display() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), s)

    def test_str(self):
        """ Test __str__ return value """
        s1 = Square(3, 1, 3)
        result = "[Square] (1) 1/3 - 3\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(s1)
            self.assertEqual(str_out.getvalue(), result)

    def test_str_no_args(self):
        """ Tests  """
        r = Square(5, 2)
        with self.assertRaises(TypeError) as e:
            Square.__str__()
        s = "__str__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), s)
