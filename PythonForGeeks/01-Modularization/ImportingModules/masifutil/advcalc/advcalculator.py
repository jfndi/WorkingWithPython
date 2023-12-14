"""
advcalculator.py:

    Created on 14-Dec-23
    
    @Author: Jean-François Ndi
"""
# Advcalculator.py with sqrt, log and ln functions.
import math


def sqrt(x):
    """
    This function takes square root of a number.

    :param x: The input to be square rooted.
    :return: The square rootT

    """
    return math.sqrt(x)


def log(x):
    """
    This function returns log of base 10.

    :param x: The input whose log value will be returned.
    :return: The log value of the input.

    """
    return math.log(x, 10)


def log2(x):
    """
    This function returns log of base 2.

    :param x: The input value whose log2 value will be returned.
    :return: The log2 value of the input.

    """
    return math.log(x, 2)
