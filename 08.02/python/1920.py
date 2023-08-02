N = int(input())

numbers = set(map(int, input().split()))

M = int(input())

test_numbers = list(map(int, input().split()))

for i in test_numbers:
    if i in numbers:
        print(1)
    else:
        print(0)