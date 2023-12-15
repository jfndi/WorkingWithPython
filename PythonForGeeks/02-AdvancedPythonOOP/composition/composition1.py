"""
composition1.py:

    Created on 15-Dec-23
    
    @Author: Jean-François Ndi

    This example illustrates the concept of composition.

"""
class Seat:


    def __init__(self, seat_type):
        self.i_type = seat_type


    def __str__(self):
        return f'Seat type: {self.i_type}'

class Engine:


    def __init__(self, size):
        self.i_size = size


    def __str__(self):
        return f'Engine: {self.i_size}'

class Car:


    def __init__(self, color, eng_size, seat_type):
        self.i_color = color
        self.engine = Engine(eng_size)
        self.seat = Seat(seat_type)


    def print_me(self):
        print (f'This car of color {self.i_color} with {self.engine} and '
               f'{self.seat}')

if __name__ == "__main__":
    car = Car("blue", "2.5L", "Leather")
    car .print_me()
    print(car.engine)
    print(car.seat)
    print(car.i_color)
    print(car.engine.i_size)
    print(car.seat.i_type)
