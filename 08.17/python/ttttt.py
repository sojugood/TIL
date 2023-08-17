def max_profit_for_month(Ms, chart, month):
    N = len(chart)  # 전체 품목의 수
    candidates = []  # 이익이 발생하는 품목 후보들을 저장하기 위한 리스트

    # 각 품목에 대해 이익이 발생하는지 체크
    for i in range(N):
        cost = chart[i][month]  # 해당 월의 품목 가격
        gain = chart[i][month + 1] - cost  # 다음 달과의 가격 차이 (이익)

        # 이익이 발생한다면
        if gain > 0:
            max_count = Ms // cost  # 최대 구매 가능 수량
            candidates.append((gain, cost, max_count))

    # 이익이 큰 순으로 정렬
    candidates.sort(reverse=True, key=lambda x: x[0])

    max_profit = 0  # 가능한 최대 이익 초기값 설정

    # 후보 품목들 중에서 조합을 확인
    for i in range(len(candidates)):
        remaining_budget = Ms  # 남은 예산
        profit = 0  # 현재 조합의 이익
        for j in range(i, len(candidates)):
            # 해당 품목을 최대한 많이 구매하는 경우
            count = min(candidates[j][2], remaining_budget // candidates[j][1])
            profit += count * candidates[j][0]  # 이익 계산
            remaining_budget -= count * candidates[j][1]  # 예산 감소
        max_profit = max(max_profit, profit)  # 최대 이익 갱신

    return max_profit  # 최대 이익 반환


T = int(input())

for tc in range(1, T + 1):
    Ms, Ma = map(int, input().split())
    N, L = map(int, input().split())
    chart = [list(map(int, input().split())) for _ in range(N)]

    for j in range(L):
        Ms += max_profit_for_month(Ms, chart, j) + Ma  # 해당 월의 이익과 고정 수입을 더함

    print(f"#{tc} {Ms}")  # 결과 출력
