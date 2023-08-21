N, M, B = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 2차원 리스트를 1차원 리스트로 변환
blocks = []
for row in arr:
    blocks.extend(row)

# 최소 높이와 최대 높이 설정
min_height = min(blocks)
max_height = min(256, max(blocks) + B // (N * M))

result_time = float('inf')
result_height = -1

# 각 높이에 대해 시간 계산
for height in range(min_height, max_height + 1):
    time = 0
    need = 0
    remove = 0

    for block in blocks:
        if block < height:
            need += height - block
            time += (height - block)
        else:
            remove += block - height
            time += (block - height) * 2

    # 필요한 블록 수가 가진 블록 수와 제거한 블록 수의 합보다 작거나 같은 경우
    if need <= B + remove:
        if time <= result_time:
            result_time = time
            result_height = height

print(result_time, result_height)
