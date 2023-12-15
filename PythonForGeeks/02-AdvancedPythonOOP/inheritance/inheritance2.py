"""
inheritance2.py:

    Created on 15-Dec-23
    
    @Author: Jean-François Ndi

    This example shows how to use multiple inheritance.

"""
class Vehicle:


    def __init__(self, color):
        self.i_color = color


    def print_vehicle_info(self):
        print(f'This is vehicle and I know my color is {self.i_color}')

class Engine:


    def __init__(self, size):
          self.i_size = size


    def print_engine_info(self):
        print(f'This is Engine and I know my size is {self.i_size}')

class Car(Vehicle, Engine):


    def __init__(self, color, size, seats):
        self.i_color = color
        self.i_size = size
        self.i_seats = seats


    def print_car_info(self):
        print(f'This is car of color {self.i_color} with seats {self.i_seats}'
              f' with engine of size {self.i_size}')

if __name__ == "__main__":
    car = Car("blue", "2.5L", 5)
    car.print_vehicle_info()
    car.print_engine_info()
    car.print_car_info()
