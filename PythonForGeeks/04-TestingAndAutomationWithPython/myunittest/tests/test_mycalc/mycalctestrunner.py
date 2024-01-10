"""
    mycalctestrunner.py
    
    Created by Jean-François Ndi @ 10/01/2024
"""
import unittest

from test_mycalc_add import MyCalcAddTestSuite
from test_mycalc_subtract import MyCalcSubtractTestSuite
from test_mycalc_multiply import MyCalcMultiplyTestSuite
from test_mycalc_divide import MyCalcDivideTestSuite


def run_mytests():
    test_classes = [
        MyCalcAddTestSuite,
        MyCalcSubtractTestSuite,
        MyCalcMultiplyTestSuite,
        MyCalcDivideTestSuite
    ]

    loader = unittest.TestLoader()

    test_suites = []
    for t_class in test_classes:
        suite = loader.loadTestsFromTestCase(t_class)
        test_suites.append(suite)

    final_suite = unittest.TestSuite(test_suites)

    runner = unittest.TextTestRunner()
    results = runner.run(final_suite)


if __name__ == '__main__':
    run_mytests()
