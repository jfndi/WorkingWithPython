"""
    exception4.py
    
    Created by Jean-François Ndi @ 09/01/2024
"""
import math

class NumTypeError(TypeError):
    pass


class NegativeNumError(Exception):
    def __init__(self):
        super().__init__("Negative number not supported.")


def sqrt(num):
    if not isinstance(num, (int, float)):
        raise NumTypeError("Only numbers are allowed.")
    if num < 0:
        raise NegativeNumError
    return math.sqrt(num)


if __name__ == "__main__":
    try:
        print(sqrt(9))
        print(sqrt('a'))
        print(sqrt(-9))
    except NumTypeError as e:
        print(e)
    except NegativeNumError as e:
        print(e)
