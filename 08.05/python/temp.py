from collections import deque

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    documents = list(map(int, input().split()))
    queue = deque([(value, idx) for idx, value in enumerate(documents)])
    count = 0

    while queue:
        # 큐의 맨 앞 문서와 나머지 문서 중 중요도가 높은 문서를 찾는다.
        current = queue.popleft()
        if any(current[0] < x[0] for x in queue):
            queue.append(current) # 중요도가 높은 문서가 있다면 맨 뒤로 보낸다.
        else:
            count += 1 # 중요도가 높은 문서가 없다면 인쇄한다.
            if current[1] == M: # 궁금한 문서가 인쇄된 경우
                print(count)
                break