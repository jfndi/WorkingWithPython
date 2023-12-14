"""
carexample4.py:

    Created on 14-Dec-23
    
    @Author: Jean-François Ndi

    This example shows the effect of calling print on a class instance not
    providing some sort of to_string method.

"""
class Car:


    def __init__(self, color, miles):
        self.i_color = color
        self.i_mileage = miles

if __name__ == "__main__":
    car = Car("blue", 1000)
    print(car)
