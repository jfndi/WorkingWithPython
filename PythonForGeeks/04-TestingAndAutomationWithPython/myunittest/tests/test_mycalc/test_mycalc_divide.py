"""
    test_mycalc_divide.py
    
    Created by Jean-François Ndi @ 10/01/2024
"""
import unittest
from myunittest.src.mycalc.mycalc import MyCalc


class MyCalcDivideTestSuite(unittest.TestCase):
    def setUp(self):
        self.calc = MyCalc()

    def test_add(self):
        self.assertEqual(2, self.calc.divide(10, 5), 'Should be 2')
