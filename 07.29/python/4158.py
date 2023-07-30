import sys
input = sys.stdin.readline

while True:
    N, M = map(int, input().split())

    if N == 0 and M == 0:
        break
    else:
        N_set = set()
        M_set = set()
        for _ in range(N):
            n = int(input())
            N_set.add(n)

        for _ in range(M):
            m = int(input())
            M_set.add(m)

        result = len(N_set & M_set)
        print(result)