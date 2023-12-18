"""
generators2.py:

    Created on 18-Dec-23
    
    @Author: Jean-François Ndi

    This example revisits the Week class and its iterator implementation and
    will use a generator instead of an iterator class.

"""
class Week:
    def __init__(self):
        self.days = {1: 'Monday', 2: 'Tuesday',
                     3: 'Wednesday', 4: 'Thursday',
                     5: 'Friday', 6: 'Saturday',
                     7: 'Sunday'}


    def week_gen(self):
        for x in self.days:
            yield self.days[x]

if __name__ == "__main__":
    wk = Week()
    iter1 = wk.week_gen()
    iter2 = iter(wk.week_gen())
    print(iter1.__next__())
    print(iter2.__next__())
    print(next(iter1))
    print(next(iter2))
