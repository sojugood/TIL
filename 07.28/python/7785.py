import sys
input = sys.stdin.readline

n = int(input())

status_dict = {}

for i in range(n):
    name, status = input().split()
    if status == 'enter':
        status_dict[name] = status
    else:
        if name in status_dict:
            del status_dict[name]

result = sorted(status_dict.keys(), reverse=True)

print('\n'.join(result))