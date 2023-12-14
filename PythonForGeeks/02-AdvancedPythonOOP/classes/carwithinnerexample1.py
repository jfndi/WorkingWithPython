"""
carwithinnerexample1.py:

    Created on 14-Dec-23
    
    @Author: Jean-François Ndi

    This example shows what type of elements a Pytho class can have:
    * Constructor and destructor.
    * Class methods and attributes.
    * Instance methods and attributes.
    * Nested classes.

"""
class Car:
    """
    Outer class.
    """
    c_mileage_units = "Mi"


    def __init__(self, color, miles, eng_size):
        self.i_color = color
        self.i_mileage = miles
        self.i_engine = self.Engine(eng_size)


    def __del__(self):
        pass


    def __str__(self):
        return f'Car with color {self.i_color}, mileage'\
               f' {self.i_mileage} and engine of {self.i_engine}'


    class Engine:
        """
        Inner class
        """


        def __init__(self, size):
            self.i_size = size


        def __str__(self):
            return self.i_size

if __name__ == "__main__":
    car = Car("blue", 1000, "2.5L")
    print(car)
    print(car.i_engine)