N, M, B = map(int, input().split())

arr = [map(int, input().split()) for _ in range(N)]

arr.sort()

if arr[-1] == arr[0]:
    print(0, arr[-1])
else:
    while True:
        target1 = sum(arr) // len(arr)
        target2 = (sum(arr) // len(arr)) + 1
        count1 = 0
        count2 = 0
        for i in arr:
            count1 += target1 - i
            count2 += target2 - i
        if count1 < 0:
            time = count1 * 2
        else:
            time = count1 * 1