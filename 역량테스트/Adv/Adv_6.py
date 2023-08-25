T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    tree = list(map(int, input().split()))
    target = max(tree)
    cnt = 0
    for i in range(N):
        tree[i] = (target - tree[i])
        # cnt += ((target - tree[i]) // 3) * 2
        # tree[i] = (target - tree[i]) % 3
    grow = 1
    tree.sort()
    while sum(tree) > 0:
        for j in range(N):
            if tree[j] == 2 and sum(tree) == 2 and grow == 1:
                grow = 2
                cnt += 1
                break
            if tree[j] - grow >= 0:
                tree[j] -= grow
                cnt += 1
                if grow == 1:
                    grow = 2
                    break
                elif grow == 2:
                    grow = 1
                    break

        else:
            if grow == 1:
                grow = 2
                cnt += 1
            elif grow == 2:
                grow = 1
                cnt += 1
    print(f"#{tc} {cnt}")