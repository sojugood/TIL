N = int(input())

result_list = []

for i in range(N):
    stack = []
    L = list(input().split())
    for word in reversed(L):
        stack.append(word)
    result_list.append(stack)

for i, j in zip(range(N), result_list):
    print(f"Case #{i + 1}: {' '.join(j)}")
