"""
    mycalc.py
    
    Created by Jean-François Ndi @ 10/01/2024
"""
class MyCalc:
    def add(self, x, y):
        if not (isinstance(x, (int, float)) | isinstance(y, (int, float))):
            raise TypeError('Only numbers are allowed.')

        return x + y

    def subtract(self, x, y):
        if not (isinstance(x, (int, float)) | isinstance(y, (int, float))):
            raise TypeError('Only numbers are allowed.')

        return x - y

    def multiply(self, x, y):
        if not (isinstance(x, (int, float)) | isinstance(y, (int, float))):
            raise TypeError('Only numbers are allowed.')

        return x * y

    def divide(self, x, y):
        if not (isinstance(x, (int, float)) | isinstance(y, (int, float))):
            raise TypeError('Only numbers are allowed.')

        if y == 0:
            raise ZeroDivisionError

        return x / y
