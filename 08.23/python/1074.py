direction = [(0, 1), (1, -1), (0, 1)]

N, r, c = map(int, input().split())

i, j = 0, 0

num = 0

temp = []

for k in range(1, N):
    nr = r // (2**k)
    nc = c // (2**k)
    temp.append((nr, nc))

temp = temp[::-1]

for fi, fj in temp:
    if fi == i and fj == j:
        i, j = i*2, j*2
        num *= 4
        continue
    for dx, dy in direction:
        i, j = i + dx, j + dy
        num += 1
        if fi == i and fj == j:
            i, j = i*2, j*2
            num *= 4
            break

if r == i and c == j:
    pass
else:
    for dx, dy in direction:
        i, j = i + dx, j + dy
        num += 1
        if r == i and c == j:
            break
print(num)