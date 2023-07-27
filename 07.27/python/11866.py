N, K = map(int, input().split())

circle_list = list(range(1, N + 1))
result_list = []

index = 0
for _ in range(N):
    index += K - 1
    if index >= len(circle_list): # 리스트 범위를 벗어나는 경우
        index = index % len(circle_list)
    out = circle_list.pop(index)
    result_list.append(out)

print(f"<{', '.join(map(str, result_list))}>")
