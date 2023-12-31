"""
methodexample1.py:

    Created on 14-Dec-23
    
    @Author: Jean-François Ndi

    This example gives examples of the three types of methods supported in
    Python:
    * Instance methods.
    * Class methods.
    * Static methods.

"""
class Car:
    c_mileage_units = "Mi"


    def __init__(self, color, miles):
        self.i_color = color
        self.i_mileage = miles


    def print_color(self):
        print(f'Color of the car is {self.i_color}.')


    @classmethod
    def print_units(cls):
        print(f'Mileage unit is: {cls.c_mileage_units}.')
        print(f'Class name is {cls.__name__}.')


    @staticmethod
    def print_hello():
        print('Hello from a static method.')

if __name__ == "__main__":
    car = Car("blue", 1000)
    car.print_color()
    car.print_units()
    car.print_hello()

    Car.print_color(car)
    Car.print_units()
    Car.print_hello()
