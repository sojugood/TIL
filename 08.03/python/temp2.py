def binarySearch(e, key):
    start = 1
    end = e
    count = 0
    while start <= end:
        count += 1
        middle = (start + end) // 2
        if middle == key:
            return count
        elif middle > key:
            end = middle
        else:
            start = middle

T = int(input())
for tc in range(1, T + 1):
    P, A, B = map(int, input().split())
    A_count = binarySearch(P, A)
    B_count = binarySearch(P, B)
    if A_count > B_count:
        print(f"#{tc} B")
    elif A_count < B_count:
        print(f"#{tc} A")
    else:
        print(f"#{tc} 0")
