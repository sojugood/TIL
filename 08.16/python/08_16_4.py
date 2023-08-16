def f(i, N):
    if i == N:
        print(P)
        lst.append(P[:])
        return
    else:
        for j in range(i, N):   # 자신부터 오른쪽 끝까지
            P[i], P[j] = P[j], P[i]
            f(i + 1, N)
            P[i], P[j] = P[j], P[i]

lst = []
P = [0, 1, 2]
f(0, 3)
print(lst)