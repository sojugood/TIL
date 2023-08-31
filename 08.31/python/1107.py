import sys
input = sys.stdin.readline

def move(channel):
    for n in str(channel):
        if n in X:
            return False
    return True

N = int(input())

M = int(input())

X = set(input().split()) if M else set()

result = abs(100 - N)

for channel in range(1000000):
    if move(channel):
        result = min(result, abs(N - channel) + len(str(channel)))

print(result)