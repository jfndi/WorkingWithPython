# -*- coding: utf-8 -*-
"""
Created on Fri May 20 17:31:12 2022

@author: Jean-François Ndi
"""

#
# globalmain.py with globals() function
#


def print_globals():
    g = globals()
    for item in g:
        print(f'{item}: {g[item]}')


def hello():
    print("Hello!")


if __name__ == "__main__":
    print_globals()
