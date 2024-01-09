"""
    test_myadd1.py
    
    Created by Jean-François Ndi @ 09/01/2024

    A test suite example for myadd function.
"""
import unittest
from myunittest.src.myadd.myadd import add

class MyAddTestSuite(unittest.TestCase):


    def test_add1(self):
        self.assertEqual(15, add(10, 5), 'Should be 15')


    def test_add2(self):
        self.assertEqual(5, add(10, -5), 'Should be 5')


    def test_add3(self):
        self.assertEqual(-5, add(-10, 5), 'Should be -5')


    def test_add4(self):
        self.assertEqual(-15, add(-10, -5), 'Should be -15')


if __name__ == "__main__":
    unittest.main()
