"""
    exception1.py
    
    Created by Jean-François Ndi @ 08/01/2024
"""

try:
    # Uncomment the following line to avoid NameError exception.
    # x = 0
    print(x)
    x = 5
    y = 0
    # Comment out the previous line and uncomment the following to avoid the divide by zero exception.
    # y = 1
    z = x / y
    # The following line will trigger a concatenation exception.
    print('x' + y)
except NameError as e:
    print(e)
except ZeroDivisionError:
    print("Division by zero not allowed")
except Exception as e:
    print("An error occurred")
    print(e)
