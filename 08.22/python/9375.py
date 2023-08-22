T = int(input())

for _ in range(T):
    dic = dict()
    n = int(input())
    for _ in range(n):
        name, typ = map(str, input().split())
        if typ not in dic:
            dic[typ] = 2
        else:
            dic[typ] += 1
    res = 1
    for v in dic.values():
        res *= v
    result = res - 1
    print(result)