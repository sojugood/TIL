p = 1

q = []

N = 20

m = 0


while m < N:
    q.append((p, 1, 0))
    v, c, my = q.pop(0)
    print(f"큐에 남아있는 사람 수{len(q) + 1} 받아갈 사탕 수{c} 나눠준 사탕 수{m}")

    m += c
    q.append((v, c + 1, my + c))
    p += 1
print(f"마지막 사탕을 받은 사람{v}")