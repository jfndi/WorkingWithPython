"""
abstraction1.py:

    Created on 15-Dec-23
    
    @Author: Jean-François Ndi

    This example shows how to use ABC module and abstractmethod decorator to
    build and abstract class.

"""
from abc import ABC, abstractmethod

class Vehicle(ABC):


    def hello(self):
        print(f'Hello from abstract class')


    @abstractmethod
    def print_me(self):
        pass

class Car(Vehicle):


    def __init__(self, color, seats):
        self.i_color = color
        self.i_seat = seats


    """
    It is a must to implement this method.
    """
    def print_me(self):
        print(f'Car with color {self.i_color} and no of seats {self.i_seat}')

if __name__ == "__main__":
    car = Car("blue", 5)
    car.print_me()
    car.hello()
