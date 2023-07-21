trash = set()

for i in range(10):
    n = int(input())
    t = n % 42
    trash.add(t)

print(len(trash))
