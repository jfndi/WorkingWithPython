"""
    test_myadd3.py
    
    Created by Jean-François Ndi @ 10/01/2024

    This examples uses a test suite to validate errors.
"""
import unittest
from myunittest.src.myadd.myadd2 import MyAdd

class MyAddTestSuite(unittest.TestCase):

    def setUp(self):
        self.myadd = MyAdd()

    def tearDown(self):
        del (self.myadd)

    def test_typeerror1(self):
        self.assertRaises(TypeError, self.myadd.add, 'a', -5)

    def test_typeerror2(self):
        self.assertRaises(TypeError, self.myadd.add, 'a', 'b')
