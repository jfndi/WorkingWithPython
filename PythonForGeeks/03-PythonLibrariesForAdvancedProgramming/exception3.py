"""
    exception3.py
    
    Created by Jean-François Ndi @ 09/01/2024
"""
import math


def sqrt(num):
    if not isinstance(num, (int, float)):
        raise TypeError("Only numbers are allowed.")
    if num < 0:
        raise Exception("Negative number not supported.")
    return math.sqrt(num)


if __name__ == "__main__":
    try:
        print(sqrt(9))
        print(sqrt('a'))
        print(sqrt(-9))
    except Exception as e:
        print(e)
