"""
generators3.py:

    Created on 18-Dec-23
    
    @Author: Jean-François Ndi

    This example demonstrates the use of generator expressions. Generator
    expressions can be used to create simple generators (also known as
    anonymous functions) on the fly without writing a special method.

"""
L =[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
f1 = [x + 1 for x in L] # A list.
g1 = (x + 1 for x in L) # A tuple.

print(g1.__next__())
print(g1.__next__())
