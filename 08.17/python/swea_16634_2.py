from collections import deque

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    cheese = list(map(int, input().split()))

    # 각 피자에 대한 정보를 (피자 번호, 치즈 양) 형태의 튜플로 저장
    oven = deque([(i+1, cheese[i]) for i in range(N)])
    next_pizza_idx = N

    while len(oven) > 1:
        pizza_idx, cheese_amount = oven.popleft()

        cheese_amount //= 2  # 치즈 양 반감

        if cheese_amount == 0:  # 치즈가 모두 녹았을 경우
            if next_pizza_idx < M:  # 아직 화덕에 넣지 않은 피자가 있다면
                oven.append((next_pizza_idx+1, cheese[next_pizza_idx]))
                next_pizza_idx += 1
        else:  # 치즈가 아직 남아있을 경우
            oven.append((pizza_idx, cheese_amount))

    print(f"#{tc} {oven[0][0]}")
