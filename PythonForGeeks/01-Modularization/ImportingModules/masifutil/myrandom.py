# -*- coding: utf-8 -*-
"""
Created on Fri May 20 15:49:01 2022

@author: Jean-François Ndi
"""

#
# myrandom.py with default and custom random functions
#

import random


def random_1d():
    """ This function generates a random number between 0 \
        and 9 """
    return random.randint(0, 9)


def random_2d():
    """ This function generates a random number between 10 \
        and 99 """
    return random.randint(10, 99)
