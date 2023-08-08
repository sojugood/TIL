T = int(input())
for _ in range(T):
    s = [input().split() for _ in range(9)]
    r = 1

    for i in range(9):
        # 행 검사
        if len(set(s[i])) != 9:
            r = 0
            break

        c = set()  # 열 검사용 set
        g = set()  # 서브그리드 검사용 set

        for j in range(9):
            # 열 검사
            c.add(s[j][i])
            # 서브그리드 검사
            g.add(s[3*(i//3) + j//3][3*(i%3) + j%3])

        if len(c) != 9 or len(g) != 9:
            r = 0
            break

    print(f"#{_+1} {r}")
