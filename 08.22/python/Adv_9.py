memo = {}

def shot(lst):
    state = ','.join(map(str, lst))
    if state in memo:
        return memo[state]

    EA = len(lst)
    if EA == 1:
        return lst[0]

    max_score = 0
    for i in range(EA):
        temp_score = 0
        if i == 0:
            temp_score += lst[1]
        elif i == EA - 1:
            temp_score += lst[EA - 2]
        else:
            temp_score += (lst[i - 1] * lst[i + 1])

        temp = lst[:i] + lst[i + 1:]
        curr_score = temp_score + shot(temp)
        max_score = max(max_score, curr_score)

    memo[state] = max_score
    return max_score

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    result = shot(lst)
    print(f"#{tc} {result}")
