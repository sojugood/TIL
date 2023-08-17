def max_gain(Ms, month): # 월 별 최대 이익 계산하는 함수
    lst = [] # 현재 매수 시 이득인 종목을 담을 리스트

    for i in range(N):
        cost = chart[i][month]
        V = chart[i][month + 1] - cost
        if V > 0: # 다음 달 가격과 현재 달 가격의 차이가 0보다 크다면 매수할 수 있는 종목이므로 이익과 현재 가격, 최대 구매 가능 수량을 리스트에 추가
            max_count = Ms // cost
            lst.append((V, cost, max_count))

    lst = sorted(lst, reverse=True) # 이익이 제일 큰 종목을 기준으로 정렬

    max_gain = 0 # 최대 이익 초기값 설정
    for i in range(len(lst)): # 각 경우를 따져봄. 이익이 제일 큰 종목을 사지 않고 하위 이익의 종목을 다 샀을 때 총 이익이 더 클수도 있음.
        money = Ms
        gain = 0
        for j in range(i, len(lst)):
            count = min(lst[j][2], money // lst[j][1])
            gain += count * lst[j][0]
            money -= count * lst[j][1]
        max_gain = max(max_gain, gain)

    return max_gain


T = int(input())

for tc in range(1, T + 1):
    Ms, Ma = map(int, input().split())
    N, L = map(int, input().split())
    chart = [list(map(int, input().split())) for _ in range(N)]
    Start = Ms # 시드액 정보 저장(마지막에 계산해주기 위해)

    for j in range(L):
        Ms += max_gain(Ms, j) + Ma

    result = Ms - (Start + (Ma * L)) # 최대 수익 계산(최종 잔고 - 투자 원금)

    print(f"#{tc} {result}")
