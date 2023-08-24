T = int(input())
 
for tc in range(1, T + 1):
    N, num = map(str, input().split())
    res = ''
    for i in num:
        s = format(int(i, 16), '04b')
        res += s
    print(f"#{tc} {res}")