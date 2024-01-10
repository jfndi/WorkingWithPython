"""
    test_mycalc_multiply.py
    
    Created by Jean-François Ndi @ 10/01/2024
"""
import unittest
from myunittest.src.mycalc.mycalc import MyCalc


class MyCalcMultiplyTestSuite(unittest.TestCase):
    def setUp(self):
        self.calc = MyCalc()

    def test_add(self):
        self.assertEqual(50, self.calc.multiply(10, 5), 'Should be 50')
