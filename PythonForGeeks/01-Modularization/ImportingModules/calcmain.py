# -*- coding: utf-8 -*-
"""
Created on Fri May 20 15:59:16 2022

@author: Jean-François Ndi
"""

#
# calcmain.py with a main function
#

import mycalculator
import myrandom


def my_main():
    """ This function is a main function which generates two random \
        numbers and then apply calculator functions on them """
    x = myrandom.random_2d()
    y = myrandom.random_1d()

    result = mycalculator.add(x, y)
    diff = mycalculator.subtract(x, y)

    print("x = {}, y = {}".format(x, y))
    print("Sum is {}".format(result))
    print("Diff is {}".format(diff))


""" This is executed only if the special variable '__name__' is set as main """
if __name__ == "__main__":
    my_main()
