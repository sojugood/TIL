import sys
input = sys.stdin.readline

A, K = map(int, input().split())

cnt = 0

while K != A:
    if K % 2 == 0:
        if K // 2 >= A:
            K = K // 2
            cnt += 1
        else:
            while K != A:
                K -= 1
                cnt += 1
    else:
        K -= 1
        cnt += 1

print(cnt)