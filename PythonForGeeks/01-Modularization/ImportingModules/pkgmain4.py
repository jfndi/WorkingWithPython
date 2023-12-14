"""
pkgmain4.py:

    Created on 14-Dec-23
    
    @Author: Jean-François Ndi
"""
# pkgmain4.py with sys.path append code.
import os
import sys

dir_path = os.path.dirname(os.path.abspath(__file__))
assert isinstance(dir_path, str)
sys.path.append(dir_path)

import masifutil

def my_main():
    """
    This is a main function which generate two random\
    numbers and then apply calculator functions on them.

    :return: None.
    """
    x = masifutil.random_2d()
    y = masifutil.random_1d()

    sum = masifutil.add(x, y)
    diff = masifutil.subtract(x, y)
    sroot = masifutil.sqrt(x)
    log10x = masifutil.log(x)
    log2x = masifutil.log2(x)

    print(f'x = {x}, y = {y}')
    print(f'sum is {sum}')
    print(f'diff is {diff}')
    print(f'square root is {sroot}')
    print(f'log base of 10 is {log10x}')
    print(f'log base of 2 is {log2x}')


if __name__ == '__main__':
    my_main()
