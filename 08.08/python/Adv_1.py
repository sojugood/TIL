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
        if x - location_x > 0 and y - location_y > 0:
            if direction == 1:
                result += 1
                direction = 2
            elif direction == 2:
                result += 3
                direction = 1
            elif direction == 3:
                result += 3
                direction = 2
            elif direction == 4:
                result += 2
                direction = 2
        elif x - location_x > 0 and y - location_y < 0:
            if direction == 1:
                result += 2
                direction = 3
            elif direction == 2:
                result += 1
                direction = 3
            elif direction == 3:
                result += 3
                direction = 2
            elif direction == 4:
                result += 3
                direction = 3
        elif x - location_x < 0 and y - location_y < 0:
            if direction == 1:
                result += 3
                direction = 4
            elif direction == 2:
                result += 2
                direction = 4
            elif direction == 3:
                result += 1
                direction = 4
            elif direction == 4:
                result += 3
                direction = 3
        elif x - location_x < 0 and y - location_y > 0:
            if direction == 1:
                result += 3
                direction = 4
            elif direction == 2:
                result += 3
                direction = 1
            elif direction == 3:
                result += 2
                direction = 1
            elif direction == 4:
                result += 1
                direction = 1
        location_x, location_y = x, y
    print(f"#{tc} {result}")