import sys
input = sys.stdin.readline

K, N = map(int, input().split())
lis = [int(input()) for _ in range(K)]

low, high = 1, max(lis)

while low <= high:
    mid = (low + high) // 2
    lines = sum(i // mid for i in lis)
    
    if lines >= N:
        low = mid + 1
    else:
        high = mid - 1

print(high)
