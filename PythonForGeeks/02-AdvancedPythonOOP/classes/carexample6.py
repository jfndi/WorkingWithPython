"""
carexample6.py:

    Created on 14-Dec-23
    
    @Author: Jean-François Ndi

    This example shows how to define private and protected attributes and/or
    methods.
    NOTE: There is still some way to access them directly (not shown here) but
    it is considered as REALLY TERRIBLE practice as it nullify the information
    hiding paradigm.

"""
class Car:
    c_mileage_unit = "Mi"
    __max_speed = 200


    def __init__(self, color, miles, model):
        self.i_color = color
        self.i_mileage = miles
        self.__no_doors = 4
        self._model = model


    def __str__(self):
        return f'Car with color {self.i_color}, mileage '\
               f'{self.i_mileage}, model {self._model} and doors'\
               f'{self.__no_doors}'


    def __doors(self):
        return self.__no_doors

if __name__ == "__main__":
    car = Car("blue", 1000, "Camry")
    print(car)
