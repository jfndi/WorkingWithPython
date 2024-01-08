"""
    multifileread2.py
    
    Created by Jean-François Ndi @ 08/01/2024
"""
with open("1.txt") as file1, open("3.txt", "w") as file3:
    for line in file1.readlines():
        file3.write(line)
