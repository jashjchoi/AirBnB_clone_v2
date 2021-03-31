#!/usr/bin/python3
"""Unittest for console.py"""
import unittest
import os
import pep8
from io import StringIO
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


@unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == "db", "using db")
class test_console(unittest.TestCase):
    def setUp(self):
        pass

    def test_pep8_errors(self):
        style_checker = pep8.StyleGuide(quiet=True)
        res = style_checker.check_fiiles(['console.py'])
        self.assertEqual(res.total_error, 0)

    def test_create(self):
        """test do_create command with empty class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            self.assertEqual("**missing class name**\n", f.getvalue())
        """test do_create command with wrong class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create dummy")
            self.assertEqual("**class doesn't exist**\n", f.getvalue())

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
            self.assertEqual("**class doesn't exist**\n", f.getvalue())
        """test do_all command with empty name"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")
            self.assertEqual("**missing class name**\n", f.getvalue())

    def test_show(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
            self.assertEqual("**missing class name**\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show dummy")
            self.assertEqual("**class doesn't exist**\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show State")
            self.assertEqual("**No instance**\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show State 11111")
            self.assertEqual("**Invalid Instance**\n", f.getvalue())

    def test_update(self):
        """test do_update command with classes"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update")
            self.assertEqual("**missing class name**\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update dummy")
            self.assertEqual("**class doesn't exist**\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update State")
            self.assertEqual("**No instance**\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update State 11111")
            self.assertEqual("**Invalid Instance**\n", f.getvalue())

    def test_destroy(self):
        """test do_destroy command with classes"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
            self.assertEqual("**missing class name**\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy dummy")
            self.assertEqual("**class doesn't exist**\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy State")
            self.assertEqual("**No instance**\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy State 11111")
            self.assertEqual("**Invalid Instance**\n", f.getvalue())

    def good_test(self):
        """correct test case"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create State name="Oklahoma"')
            HBNBCommand().onecmd('all State')
            value = f.getvalue()[:-1]
            self.assertTrue("'name': 'Oklahoma'" in value)

if __name__ == "__main__":
    if os.getenv("HBNB_TYPE_STORAGE") != "db":
        unittest.main()
