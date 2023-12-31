"""
contextmgr1.py:

    Created on 31-Dec-23
    
    @Author: Jean-François Ndi
"""
with open("myfile.txt", 'w') as f1:
    f1.write("This is a sample file.\n")
    lines = ["This is a test data.\n", "In two lines.\n"]
    f1.writelines(lines)
    f1.close()

with open("myfile.txt", 'r') as f2:
    for line in f2.readlines():
        print(line)
