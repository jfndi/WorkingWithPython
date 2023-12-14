"""
carexample5.py:

    Created on 14-Dec-23
    
    @Author: Jean-François Ndi

    This example shows the effect of calling print on a class instance
    providing an implementation of the __str__ special function.

"""
class Car:


    def __init__(self, color, miles):
        self.i_color = color
        self.i_mileage = miles


    def __str__(self):
        return f'Car with color {self.i_color} and' \
               f' mileage {self.i_mileage}.'

if __name__ == "__main__":
    car = Car("blue", 1000)
    print(car)
