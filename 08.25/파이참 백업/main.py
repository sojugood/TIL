from collections import deque

def baseball(lst):
    score = 0
    temp = 0
    cnt = 0
    q = deque(lst)

    while cnt < 3:
        s = q.popleft()

        if s == 0:
            cnt += 1
        elif s == 1:
            temp += 1
        elif s == 2:
            temp += 2
        elif s == 3:
            temp += 3
        else:
            score += (temp + 1)
            temp = 0

        if temp >= 4:
            score += (temp - 3)
            temp = 1
        q.append(s)

    return score

# N = int(input())
# for i in range(N):
#     p_lst = list(map(int, input().split()))
#     t_lst = [0] * 9
#     t_lst[3] = p_lst[0]
#     for j in range(1, 9):
#         p_lst[j]
#     print(t_lst)
#     q = deque(p_lst)
#     s = q.popleft()
#     print(s)
#     print(q)

a = [1, 2, 1, 0, 4, 0, 1, 1, 0]
print(baseball(a))