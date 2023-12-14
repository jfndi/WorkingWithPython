"""
pkgmain1.py:

    Created on 14-Dec-23
    
    @Author: Jean-François Ndi
"""
# pkgmain1.py with from statements.
import os
import sys

dir_path = os.path.abspath(os.path.join(os.path.dirname(
                           os.path.abspath(__file__)), os.pardir))
assert isinstance(dir_path, str)
sys.path.append(dir_path)

from masifutil import mycalculator as calc
from masifutil import myrandom as rand
from masifutil.advcalc import advcalculator as acalc

def my_main():
    """
    This is a main function which generate two random\
    numbers and then apply calculator functions on them.

    :return: None.
    """
    x = rand.random_2d()
    y = rand.random_1d()

    sum = calc.add(x, y)
    diff = calc.subtract(x, y)
    sroot = acalc.sqrt(x)
    log10x = acalc.log(x)
    log2x = acalc.log2(x)

    print(f'x = {x}, y = {y}')
    print(f'sum is {sum}')
    print(f'diff is {diff}')
    print(f'square root is {sroot}')
    print(f'log base of 10 is {log10x}')
    print(f'log base of 2 is {log2x}')


if __name__ == '__main__':
    my_main()