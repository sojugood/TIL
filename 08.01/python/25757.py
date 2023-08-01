import sys
input = sys.stdin.readline

N, game = map(str, input().split())

name_set = set()
for i in range(int(N)):
    name = input()
    name_set.add(name)

if game == 'Y':
    result = len(name_set)
elif game == 'F':
    result = len(name_set) // 2
elif game == 'O':
    result = len(name_set) // 3

print(result)