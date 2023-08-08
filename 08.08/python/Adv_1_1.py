direction_changes = {
    1: {(1, 1): (1, 2), (-1, -1): (3, 4), (1, -1): (2, 3), (-1, 1): (3, 4)},
    2: {(1, 1): (3, 1), (-1, -1): (2, 4), (1, -1): (1, 3), (-1, 1): (3, 1)},
    3: {(1, 1): (3, 2), (-1, -1): (1, 4), (1, -1): (3, 2), (-1, 1): (2, 1)},
    4: {(1, 1): (2, 2), (-1, -1): (3, 3), (1, -1): (3, 3), (-1, 1): (1, 1)}
}
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    number_of_apple = [(0, 0)]*10
    count = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                count += 1
                number_of_apple[arr[i][j] - 1] = (i, j)
    location_x, location_y = 0, 0
    direction = 1
    result = 0
    for target in range(count):
        x, y = number_of_apple[target]
        dx = 1 if x - location_x > 0 else -1
        dy = 1 if y - location_y > 0 else -1
        turns, next_direction = direction_changes[direction][(dx, dy)]
        result += turns
        direction = next_direction
        location_x, location_y = x, y
    print(f"#{tc} {result}")