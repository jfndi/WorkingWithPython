"""
carexample1.py:

    Created on 14-Dec-23
    
    @Author: Jean-François Ndi

    This outrageously simple example shows that, in Python, object attributes
    can be added on the fly (making C++ programmers nervous ;-)).
"""
class Car:
    pass

if __name__ == '__main__':
    car = Car()
    car.color = "blue"
    car.miles = 1000
    print(f'Car color {car.color}')
    print(f'Car mileage: {car.miles}')
