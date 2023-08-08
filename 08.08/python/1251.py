N = input()
result = []
for i in range(1, len(N) - 1):
    for j in range(1 + i, len(N)):
        word = N[0:i][::-1] + N[i:j][::-1] + N[j:len(N)][::-1]
        result.append(word)
if not result:
    print(N)
else:
    print(min(result))