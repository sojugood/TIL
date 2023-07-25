from math import factorial as fac

N, K = map(int, input().split())

result = fac(N) // (fac(K) * fac(N - K))

print(result)