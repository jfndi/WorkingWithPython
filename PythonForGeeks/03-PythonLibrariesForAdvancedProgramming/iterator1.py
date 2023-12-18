"""
iterator1.py:

    Created on 18-Dec-23
    
    @Author: Jean-François Ndi

    This script provides a few examples of using the for loop for iteration
    purposes in Python.

"""
#
# Example 1: Iterating on a list.
#
for x in [1, 2, 3]:
    print(x)

#
# Example 2: Iterating a string.
#
for x in "Python for Geeks":
    print(x, end="")
print('')

#
# Example 3: Iterating on a dictionary.
#
week_days = {1: 'Mon', 2: 'Tue',
             3: 'Wed', 4: 'Thu',
             5: 'Fri', 6: 'Sat',
             7: 'Sun'}
for k in week_days:
    print(k, week_days[k])

#
# Example 4: Iterating on a file.
#
for row in open('iterator1.py'):
    print(row, end='')
