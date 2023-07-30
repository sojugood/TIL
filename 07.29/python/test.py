N, M = map(int, input().split())

start_B_line = ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']
start_W_line = ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']
test_line = []

for _ in range(N):
    test_line.append(list(input()))

print(test_line)