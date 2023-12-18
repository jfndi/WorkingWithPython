"""
generators1.py:

    Created on 18-Dec-23
    
    @Author: Jean-François Ndi

    This very simple example is used to generate a sequence of the three
    letters of the alphabet.

"""
def my_gen():
    yield 'A'
    yield 'B'
    yield 'C'

if __name__ == "__main__":
    iter1 = my_gen()
    print(iter1.__next__())
    print(next(iter1))
    print(iter1.__next__())
