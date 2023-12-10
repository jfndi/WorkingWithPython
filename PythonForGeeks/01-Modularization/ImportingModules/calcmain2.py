# -*- coding: utf-8 -*-
"""
Created on Sun May 22 17:58:26 2022

@author: Jean-François Ndi
"""
#
# calcmain.py with a main function and aliases for modules
#

import mycalculator as calc
import myrandom as rand


def my_main():
    """ This function is a main function which generates two random \
        numbers and then apply calculator functions on them """
    x = rand.random_2d()
    y = rand.random_1d()
    
    result = calc.add(x, y)
    diff = calc.subtract(x, y)
    
    print("x = {}, y = {}".format(x, y))
    print("Sum is {}".format(result))
    print("Diff is {}".format(diff))


""" This is executed only if the special variable '__name__' is set as main """
if __name__ == "__main__":
    my_main()
