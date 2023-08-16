def f(S):
    if len(S) == 2:
        if C[S[0]] == C[S[-1]] or C[S[0]] - C[S[-1]] == 1 or C[S[-1]] - C[S[0]] == 2:
            return [S[0]]
        elif C[S[-1]] - C[S[0]] == 1 or C[S[0]] - C[S[-1]] == 2:
            return [S[-1]]
    elif len(S) == 1:
        return S
    else:
        if len(S) % 2 == 1:
            return f(f(S[0:len(S)//2 + 1]) + f(S[(len(S)//2) + 1:len(S)]))
        else:
            return f(f(S[0:len(S) // 2]) + f(S[(len(S) // 2):len(S)]))

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    C = list(map(int, input().split()))
    C = [0] + C
    S = list(range(1, N + 1))
    print(f"#{tc}", *f(S))