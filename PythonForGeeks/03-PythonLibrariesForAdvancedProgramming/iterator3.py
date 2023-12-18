"""
iterator3.py:

    Created on 18-Dec-23
    
    @Author: Jean-François Ndi

    This example shows the best approach to create an iterator: use a separate
    class and always create a new instance of an iterator through the __iter__
    method.

"""
class Week:
    def __init__(self):
        self.days = {1: 'Monday', 2: 'Tuesday',
                     3: 'Wednesday', 4: 'Thursday',
                     5: 'Friday', 6: 'Saturday',
                     7: 'Sunday'}


    def __iter__(self):
        return WeekIterator(self.days)

class WeekIterator:
    def __init__(self, dayss):
        self.days_ref = dayss
        self._index = 1


    def __next__(self):
        if self._index < 1 | self._index > 7:
            raise StopIteration
        else:
            ret_value = self.days_ref[self._index]
            self._index += 1

        return ret_value

if __name__ == "__main__":
    wk = Week()
    iter1 = iter(wk)
    iter2 = iter(wk)
    print(iter1.__next__())
    print(iter2.__next__())
    print(next(iter1))
    print(next(iter2))
