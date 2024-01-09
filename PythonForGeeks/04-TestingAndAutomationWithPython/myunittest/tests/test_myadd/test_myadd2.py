"""
    test_myadd2.py
    
    Created by Jean-François Ndi @ 09/01/2024
"""
import unittest
from myunittest.src.myadd.myadd2 import MyAdd

class MyAddTestSuite(unittest.TestCase):


    def setUp(self):
        self.myadd = MyAdd()


    def tearDown(self):
        del (self.myadd)


    def test_add1(self):
        self.assertEqual(15, self.myadd.add(10, 5), 'Should be 15')


    def test_add2(self):
        self.assertEqual(5, self.myadd.add(10, -5), 'Should be 5')
