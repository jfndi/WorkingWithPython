"""
carexample2.py:

    Created on 14-Dec-23
    
    @Author: Jean-François Ndi

    This outrageously simple example shows how a constructor method can be used
    to initialize object attributes during the object creation.

"""
class Car:
    c_mileage_units = "Mi"  # Class attribute.


    def __init__(self, color, miles):
        self.i_color = color  # Object attribute 1.
        self.i_mileage = miles  # Object attribute 2.

if __name__ == "__main__":
    car1 = Car("blue", 1000)

    print(f'Car color: {car1.i_color}')
    print(f'Car mileage: {car1.i_mileage} {Car.c_mileage_units}')
