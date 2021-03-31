#!/usr/bin/python3
"""Unittest for console.py"""
import unittest
import os
from io import StringIO
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class test_console(unittest.TestCase):
    def setUp(self):
        pass

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == "db")
    def test_create(self):
        """test do_create command with empty class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            error_msg = f.getvalue()[:-1]
            self.assertEqual(error_msg, "**missing class name**")
        """test do_create command with wrong class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create dummy")
            error_msg = f.getvalue()[:-1]
            self.assertEqual(error_msg, "**class doesn't exist**")

    def test_all(self):
        """test do_all command with classes"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all State")
            self.assertEqual("[]\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all City")
            self.assertEqual("[]\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all User")
            self.assertEqual("[]\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all Place")
            self.assertEqual("[]\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all Amenity)
            self.assertEqual("[]\n", f.getvalue())
        """test do_all command with wrong class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all dummy")
            error_msg = f.getvalue()[:-1]
            self.assertEqual(error_msg, "**class doesn't exist**")
        """test do_all command with empty name"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")
            error_msg = f.getvalue()[:-1]
            self.assertEqual(error_msg, "**missing class name**")

    def good_test(self):
        """correct test case"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create State name="Oklahoma"')
            HBNBCommand().onecmd('all State')
            value = f.getvalue()[:-1]
            self.assertTrue("'name': 'Oklahoma'" in value)

if __name__ == "__main__":
    unittest.main()
