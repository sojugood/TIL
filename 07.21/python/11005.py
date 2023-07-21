N, B = map(int,input().split())
result = ""
while N:
    N, i = divmod(N, B)
    result = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"[i] + result
print(result)
