"""
    exception2.py
    
    Created by Jean-François Ndi @ 08/01/2024
"""
try:
    f = open("abc.txt", "w")
except Exception as e:
    print(f'Error: {e}')
else:
    #
    # This block is executed if no exception has occurred.
    #
    f.write("Hello World!")
    f.write("End")
finally:
    #
    # This block is always executed.
    #
    f.close()
