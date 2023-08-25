# 로봇이 바라보는 방향에 따른 이동 순서 및 이동 후 바라보는 방향 좌표
direction = {0: [(-1, 0, 1), (0, -1, 0), (1, 0, 3), (0, 1, 2)],
             1: [(0, 1, 2), (-1, 0, 1), (0, -1, 0), (1, 0, 3)],
             2: [(1, 0, 3), (0, 1, 2), (-1, 0, 1), (0, -1, 0)],
             3: [(0, -1, 0), (1, 0, 3), (0, 1, 2), (-1, 0, 1)]}


def dfs(i, j, rot, day, cnt):
    if day == 0:
        return cnt

    for _ in range(len(lst)): # 씨앗 심은 후 일자 별 성장 상태 수정 및 저장
        x, y, w = lst.pop(0)
        w -= 1
        if w == 0: # 곡식이 되면 수확 가능한 상태인 2로 바꿔줌
            arrs[x][y] = 2
        elif w == 1: # 곡식이 되기까지 하루 남은 경우, 다음 날 이동 가능하니까 1에서 3으로 바꿔줌
            arrs[x][y] = 3
            lst.append((x, y, w))
        else:
            lst.append((x, y, w))

    if arrs[i][j] == 0: # 농지라면
        for dx, dy, r in direction[rot]: # 현재 바라보는 방향의 이동 순서에 맞게 탐색
            ni, nj = i + dx, j + dy
            if 0 <= ni < N and 0 <= nj < N:
                if arrs[ni][nj] != 1: # 이동 가능한 곳이면
                    arrs[i][j] = 1 # 씨앗 심기
                    lst.append((i, j, 5 + visited[i][j])) # 싹이 되기까지 1일 + 3 + K, 정보 저장
                    visited[i][j] += 1 # 해당 농지에 대해 K번째 갱신
                    return dfs(ni, nj, r, day - 1, cnt) # 이동(오후의 행동)
        else: # 이동 가능한 곳이 없다면
            return dfs(i, j, rot, day - 1, cnt) # 제자리에 머문다

    elif arrs[i][j] == 2: # 곡식이 있으면 수확한다
        for dx, dy, r in direction[rot]:
            ni, nj = i + dx, j + dy
            if 0 <= ni < N and 0 <= nj < N:
                if arrs[ni][nj] != 1:
                    arrs[i][j] = 0 # 수확
                    return dfs(ni, nj, r, day - 1, cnt + 1)
        else: # 이동가능한 곳이 없으면 수확하고 제자리
            arrs[i][j] = 0
            return dfs(i, j, rot, day - 1, cnt + 1)


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                for k in range(4):
                    arrs = [row[:] for row in arr]
                    visited = [[1] * N for _ in range(N)]
                    lst = []
                    result = max(result, dfs(i, j, k, M, 0))
    print(f"#{tc} {result}")
