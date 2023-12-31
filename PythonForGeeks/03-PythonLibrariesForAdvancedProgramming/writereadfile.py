"""
writereadfile.py:

    Created on 31-Dec-23
    
    @Author: Jean-François Ndi
"""
f1 = open("myfile.txt", 'w')
f1.write("This is a sample file.\n")
lines = ["This is a test data.\n", "In two lines.\n"]
f1.writelines(lines)
f1.close()

f2 = open("myfile.txt", 'r')
print(f2.read(4))
print(f2.readline())
print(f2.readline())

f2.seek(0)
for line in f2.readlines():
    print(line)
f2.close()
