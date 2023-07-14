import os
f = open('Python_for_Fun.txt')
lines = f.readlines()
for i in lines[-6:]:
    print(i, end='')