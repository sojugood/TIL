import sys
import heapq
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    min_heap = []
    max_heap = []

    exist = {}

    k = int(input())

    for _ in range(k):
        op, num = input().split()
        num = int(num)

        if op == 'I':
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)

            if num in exist:
                exist[num] += 1
            else:
                exist[num] = 1

        elif op == 'D':
            target_heap = max_heap if num == 1 else min_heap

            while target_heap:
                val = -heapq.heappop(target_heap) if num == 1 else heapq.heappop(target_heap)
                if exist[val] > 0:
                    exist[val] -= 1
                    break

    min_val, max_val = None, None

    while min_heap:
        val = heapq.heappop(min_heap)
        if exist[val] > 0:
            min_val = val
            break

    while max_heap:
        val = -heapq.heappop(max_heap)
        if exist[val] > 0:
            max_val = val
            break

    if min_val is not None and max_val is not None:
        print(max_val, min_val)
    else:
        print("EMPTY")
