"""
    multifileread.py
    
    Created by Jean-Fançois Ndi @ 08/01/2024
    
"""

with open('1.txt') as file1, open('2.txt') as file2:
    print(file2.readline())
    print(file1.readline())
