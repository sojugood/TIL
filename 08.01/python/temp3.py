# T = int(input())

# for test_case in range(1, T + 1):
#     N = int(input())
#     number = list(map(int, input().split()))
#     count = [0] * 11
#     for i in number:
#         count[i] += 1
#     min_index = 0
#     for min in count:
#         if min != 0:
#             min_num = min_index
#             break
#         min_index += 1
#     max_index = 10
#     for max in count[::-1]:
#         if max != 0:
#             max_num = max_index
#             break
#         max_index -= 1
#     min_location = 0
#     for i in number:
#         min_location += 1
#         if i == min_num:
#             break
#     max_location = N + 1
#     for i in number[::-1]:
#         max_location -= 1
#         if i == max_num:
#             break
#     result = abs(min_location - max_location)
#     print(f"#{test_case} {result}")
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))

    min_num = max_num = numbers[0]
    min_location = max_location = 0

    for i, num in enumerate(numbers):
        if num < min_num:
            min_num = num
            min_location = i
        if num >= max_num:
            max_num = num
            max_location = i
            
    result = abs(min_location - max_location)
    print(f"#{test_case} {result}")
