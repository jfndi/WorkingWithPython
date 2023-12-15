"""
ducktype1.py:

    Created on 15-Dec-23
    
    @Author: Jean-François Ndi

    This example illustrates the concept of ducktyping.

"""
class Car:


    def start(self):
        print(f'Start engine by ignition/battery')

class Cycle:


    def start(self):
        print(f'Start by pushing paddles')

class Horse:


    def start(self):
        print(f'Start by pulling/releasing the reins')

if __name__ == "__main__":
    for obj in Car(), Cycle(), Horse():
        obj.start()
