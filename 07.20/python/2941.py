n = input()

replacements = {'c=' : '1', 'c-' : '2', 'dz=' : '3', 'd-' : '4', 'lj' : '5', 'nj' : '6', 's=' : '7', 'z=' : '8'}

for old, new in replacements.items():
    n = n.replace(old, new)

print(len(n))