"""
    test_mycalc_subtract.py
    
    Created by Jean-François Ndi @ 10/01/2024
"""
import unittest
from myunittest.src.mycalc.mycalc import MyCalc


class MyCalcSubtractTestSuite(unittest.TestCase):
    def setUp(self):
        self.calc = MyCalc()

    def test_add(self):
        self.assertEqual(5, self.calc.subtract(10, 5), 'Should be 5')
