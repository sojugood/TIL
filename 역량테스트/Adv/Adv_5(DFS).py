direction_1 = [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (-1, 1)] # DFS로 탐색 시 현재 열이 짝수 번호일 때 나아갈 수 있는 방향 벡터
direction_2 = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (1, 1)] # DFS로 탐색 시 현재 열이 홀수 번호일 때 나아갈 수 있는 방향 벡터
direction_3 = [[(1, 0), (0, 1), (0, -1)], [(-1, 0), (0, 1), (0, -1)], [(1, 0), (-1, -1), (-1, 1)]] # 현재 좌표에서 인접한 3방향 탐색(열 번호 짝수)
direction_4 = [[(1, 0), (0, 1), (0, -1)], [(-1, 0), (0, 1), (0, -1)], [(-1, 0), (1, -1), (1, 1)]] # 현재 좌표에서 인접한 3방향 탐색(열 번호 홀수)

def dfs(arr, i, j, depth, v, visited):
    global total

    if depth == 4 or v + (4 - depth) * max_val <= total: # 4방향 탐색 완료 혹은 탐색 중 누적된 값이 가질 수 있는 최대합이 현재 저장된 최대합보다 작을 경우
        total = max(total, v) # 최대값 비교 후 갱신
        return # 탐색 종료

    visited[i][j] = True # 중복 탐색하지 않기 위해 해당 좌표 방문 처리
    directions = direction_1 if j % 2 == 0 else direction_2 # 현재 좌표의 열 번호에 따른 탐색 방향 설정

    for dx, dy in directions:
        ni, nj = i + dx, j + dy
        if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
            dfs(arr, ni, nj, depth + 1, v + arr[ni][nj], visited)

    visited[i][j] = False # 다음 DFS를 위해 방문한 좌표 초기화

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_val = max(max(row) for row in arr) # 현재 벌집 정보에서 가장 큰 값
    total = 0 # 4칸의 최대합 저장할 변수
    visited = [[False] * M for _ in range(N)] # 방문 확인 행렬

    for i in range(N):
        for j in range(M):
            dfs(arr, i, j, 1, arr[i][j], visited)
            dirs = direction_3 if j % 2 == 0 else direction_4 # 현재 열 번호 기준 인접한 3곳 탐색
            for dir in dirs:
                temp = arr[i][j]
                for dx, dy in dir:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < N and 0 <= nj < M:
                        temp += arr[ni][nj]
                    else: # 3방향 중 한 방향이라도 갈 수 없으면 4개가 되지 않으므로 중단
                        break
                total = max(total, temp)

    print(f"#{tc} {total}")
