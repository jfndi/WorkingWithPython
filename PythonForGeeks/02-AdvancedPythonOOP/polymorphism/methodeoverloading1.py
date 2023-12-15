"""
methodeoverloading1.py:

    Created on 15-Dec-23
    
    @Author: Jean-François Ndi

    This example shows how to implement method overloading (or sort of) in Python.

"""
class Car:


    def __init__(self, color, seats):
        self.i_color = color
        self.i_seat = seats


    def print_me(self, i = 'basic'):
        if i == 'basic':
            print(f'This car is of color {self.i_color}')
        else:
            print(f'This car is of color {self.i_color} with '
                  f'seats {self.i_seat}')

if __name__ == "__main__":
    car = Car("blue", 5)
    car.print_me()
    car.print_me('blah')  # Yeeerrrk, not pretty at all.
    car.print_me('details')  # ditto
