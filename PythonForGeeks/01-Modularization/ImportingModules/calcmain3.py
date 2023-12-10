# -*- coding: utf-8 -*-
"""
Created on Sun May 22 18:01:35 2022

@author: Jean-François Ndi
"""

#
# calcmain.py with a main function and with from and aliases combined
#

from mycalculator import add as my_add
from mycalculator import subtract as my_subtract
from myrandom import random_1d, random_2d


def my_main():
    """ This function is a main function which generates two random \
        numbers and then apply calculator functions on them """
    x = random_2d()
    y = random_1d()
    
    result = my_add(x, y)
    diff = my_subtract(x, y)
    
    print("x = {}, y = {}".format(x, y))
    print("Sum is {}".format(result))
    print("Diff is {}".format(diff))
    
    print(globals())


""" This is executed only if the special variable '__name__' is set as main """
if __name__ == "__main__":
    my_main()
