T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    answer = list(map(int, input().split()))
    exam = [list(map(int, input().split())) for _ in range(N)]
    max_score = 0
    min_score = 10**10
    for i in range(N):
        score = 0
        temp = 0
        for j in range(M):
            if exam[i][j] == answer[j]:
                score += (1 + temp)
                temp += 1
            else:
                temp = 0
        if score > max_score:
            max_score = score
        if score < min_score:
            min_score = score
    result = max_score - min_score
    print(f"#{tc} {result}")