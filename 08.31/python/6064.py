import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    M, N, x, y = map(int, input().split())
    cnt = x  # cnt는 x와 y가 동시에 만족해야 하는 연도를 나타냄. 초기값은 x로 설정.
    while cnt <= M * N:  # 최대 반복 횟수는 M * N
        # cnt에서 M으로 나눈 나머지가 y와 같으면 (나머지가 0이라면 N으로 대체)
        if (cnt - y) % N == 0:
            print(cnt)
            break
        cnt += M  # M만큼 더해주면 x 값은 그대로 유지되고, y 값만 바뀜
    else:
        print(-1)
