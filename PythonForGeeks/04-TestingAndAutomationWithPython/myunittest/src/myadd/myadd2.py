"""
    myadd2.py
    
    Created by Jean-François Ndi @ 09/01/2024
"""


class MyAdd:
    def add(self, x, y):
        if not (isinstance(x, (int, float)) & isinstance(y, (int, float))):
            raise TypeError("Add only accepts numbers.")
        return x + y


if __name__ == '__main__':
    try:
        myadd = MyAdd()
        myadd.add('a', 5)
    except TypeError as e:
        print(e)
