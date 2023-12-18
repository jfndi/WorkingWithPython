"""
iterator2.py:

    Created on 18-Dec-23
    
    @Author: Jean-François Ndi

    This example implements the Week class, which stores the numbers and names
    of all weekdays in a dictionary. This class is not iterable by default. To
    make it iterable the __iter__ method is implemented. The __next__ method
    is also added.
    NOTE: The way described is not the recommended approach. The reason is that
    in the code below, the iterator is the object itself.

"""
class Week:
    def __init__(self):
        self.days = {1: 'Monday', 2: 'Tuesday',
                     3: 'Wednesday', 4: 'Thursday',
                     5: 'Friday', 6: 'Saturday',
                     7: 'Sunday'}
        self._index = 1


    def __iter__(self):
        self._index = 1
        return self

    def __next__(self):
        if self._index < 1 | self._index > 7:
            raise StopIteration
        else:
            ret_value = self.days[self._index]
            self._index += 1

        return ret_value

if __name__ == "__main__":
    wk = Week()
    for day in wk:
        print(day)
