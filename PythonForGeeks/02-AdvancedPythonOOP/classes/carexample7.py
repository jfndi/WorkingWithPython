"""
carexample7.py:

    Created on 15-Dec-23
    
    @Author: Jean-François Ndi

    This example shows the traditional way to write attribute getters and setters.

"""
class Car:
    c_mileage_unit = "Mi"


    def __init__(self, color, miles, model):
        self.__color = color
        self.__mileage = miles


    def get_color(self):
        return self.__color


    def get_mileage(self):
        return self.__mileage


    def set_mileage(self, new_mil):
        self.__mileage = new_mil

if __name__ == "__main__":
    car = Car("blue", 1000, "Camry")
    print(car)
    print(car.get_color())
    print(car.get_mileage())
    car.set_mileage(2000)
    print(car.get_color())
    print(car.get_mileage())

