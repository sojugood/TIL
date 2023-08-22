from collections import deque

direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def bfs():
    queue = deque([(0, 0, 0)])  # 초기 위치와 연료를 저장
    visited = [[float("inf")] * N for _ in range(N)] # 백트래킹 하기 위해 좌표까지 도달하는데 사용된 연료량 갱신
    visited[0][0] = 0
    result = float("inf")

    while queue:
        i, j, fuel = queue.popleft()

        if i == N - 1 and j == N - 1: # 도착하면 최소 연료값 갱신
            result = min(result, fuel)
            continue

        h = arr[i][j]

        for dx, dy in direction:
            ni, nj = i + dx, j + dy
            if 0 <= ni < N and 0 <= nj < N:
                diff = arr[ni][nj] - h
                if diff > 0:
                    new_fuel = fuel + (diff * 2)
                elif diff == 0:
                    new_fuel = fuel + 1
                else:
                    new_fuel = fuel

                if new_fuel < visited[ni][nj]: # 사용될 누적 연료량이 이미 알고있는 연료량 정보보다 작으면 그 길을 선택
                    visited[ni][nj] = new_fuel
                    queue.append((ni, nj, new_fuel))

        for (Ai, Aj, Bi, Bj, C) in tunnel:
            if i == Ai - 1 and j == Aj - 1:
                new_fuel = fuel + C
                if new_fuel < visited[Bi - 1][Bj - 1]:
                    visited[Bi - 1][Bj - 1] = new_fuel
                    queue.append((Bi - 1, Bj - 1, new_fuel))
            elif i == Bi - 1 and j == Bj - 1:
                new_fuel = fuel + C
                if new_fuel < visited[Ai - 1][Aj - 1]:
                    visited[Ai - 1][Aj - 1] = new_fuel
                    queue.append((Ai - 1, Aj - 1, new_fuel))

    return result

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    tunnel = [tuple(map(int, input().split())) for _ in range(M)]

    print(f"#{tc} {bfs()}")
