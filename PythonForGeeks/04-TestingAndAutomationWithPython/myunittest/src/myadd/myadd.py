"""
    myadd.py
    
    Created by Jean-François Ndi @ 09/01/2024
"""


def add(x, y):
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise TypeError("Add only accepts numbers.")
    return x + y
