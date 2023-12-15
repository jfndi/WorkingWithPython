"""
carexample8.py:

    Created on 15-Dec-23
    
    @Author: Jean-François Ndi

    This example shows how to use attribute decorators to define getter and setters.

"""
class Car:
    c_mileage_unit = "Mi"


    def __init__(self, color, miles, model):
        self.__color = color
        self.__mileage = miles


    def __str__(self):
        return f'Car with color {self.__color}, mileage '\
               f'{self.__mileage}.'


    @property
    def color(self):
        return self.__color


    @property
    def mileage(self):
        return self.__mileage


    @mileage.setter
    def mileage(self, new_mil):
        self.__mileage = new_mil

if __name__ == "__main__":
    car = Car("blue", 1000, "Camry")
    print(car)
    print(car.color)
    print(car.mileage)
    car.mileage = 2000
    print(car.color)
    print(car.mileage)