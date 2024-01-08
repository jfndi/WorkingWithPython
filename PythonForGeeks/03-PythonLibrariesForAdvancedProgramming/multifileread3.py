"""
    multifileread3.py
    
    Created by Jean-François Ndi @ 08/01/2024
"""
import fileinput

with fileinput.input(files=('1.txt', '2.txt')) as f:
    for line in f:
        print(f.filename())
        print(line)
