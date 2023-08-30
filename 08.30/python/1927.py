import heapq
import sys
input = sys.stdin.readline

N = int(input())

lst = []
heapq.heapify(lst)

for _ in range(N):
    x = int(input())
    if x == 0:
        if lst:
            tmp = heapq.heappop(lst)
            print(tmp)
        else:
            print(0)
    else:
        heapq.heappush(lst, x)

'''

import heapq

# 리스트를 힙으로 만들기
nums = [3, 1, 4, 1, 5, 9, 2, 6, 5]
heapq.heapify(nums)

# 힙에 원소 추가
heapq.heappush(nums, 7)

# 힙에서 최솟값 제거 후 반환
min_val = heapq.heappop(nums)

# 힙에 원소 추가 후 최솟값 제거 및 반환
min_val = heapq.heappushpop(nums, 8)

# 힙에서 최솟값 제거 후 새 원소 추가
min_val = heapq.heapreplace(nums, 0)

# 힙에서 가장 작은 N개의 아이템 반환
smallest_items = heapq.nsmallest(3, nums)

# 힙에서 가장 큰 N개의 아이템 반환
largest_items = heapq.nlargest(3, nums)

'''