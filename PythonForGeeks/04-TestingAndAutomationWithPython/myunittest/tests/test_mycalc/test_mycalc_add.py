"""
    test_mycalc_add.py
    
    Created by Jean-François Ndi @ 10/01/2024
"""
import unittest
from myunittest.src.mycalc.mycalc import MyCalc


class MyCalcAddTestSuite(unittest.TestCase):
    def setUp(self):
        self.calc = MyCalc()

    def test_add(self):
        self.assertEqual(15, self.calc.add(10, 5), 'Should be 15')
