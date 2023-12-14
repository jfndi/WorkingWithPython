"""
carexample3.py:

    Created on 14-Dec-23
    
    @Author: Jean-François Ndi

    This outrageously simple example shows what happens when:
    * We update a class attribute using a class instance vs when
    * we update a class attribute using the class name.

"""
class Car:
    c_mileage_units = "Mi"  # Class attribute.


    def __init__(self, color, miles):
        self.i_color = color  # Object attribute 1.
        self.i_mileage = miles  # Object attribute 2.

if __name__== "__main__":
    car1 = Car("blue", 1000)
    car2 = Car("red", 2000)

    print(f'Using car1: {car1.c_mileage_units}')
    print(f'Using car2: {car2.c_mileage_units}')
    print(f'Using Car: {Car.c_mileage_units}')

    print('\nModifying car1 object class attribute:')
    car1.c_mileage_units = "km"
    print(f'Using car1: {car1.c_mileage_units}')
    print(f'Using car2: {car2.c_mileage_units}')
    print(f'Using Car: {Car.c_mileage_units}')

    print('\nModifying Car class attribute:')
    Car.c_mileage_units = "NP"
    print(f'Using car1: {car1.c_mileage_units}') # This will still be "km"!!!
    print(f'Using car2: {car2.c_mileage_units}')
    print(f'Using Car: {Car.c_mileage_units}')
