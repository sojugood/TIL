import sys
input = sys.stdin.readline

def kmp_search(text, pattern):
    global cnt
    F = [0] * len(pattern)
    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[j] != pattern[i]:
            j = F[j - 1]
        if pattern[j] == pattern[i]:
            j += 1
        F[i] = j
    
    j = 0
    for i in range(len(text)):
        while j > 0 and text[i] != pattern[j]:
            j = F[j - 1]
        if text[i] == pattern[j]:
            if j == len(pattern) - 1:
                cnt += 1
                j = F[j]
            else:
                j += 1

N = int(input())

M = int(input())

S = input().strip()

find = 'IO' * N + "I"

cnt = 0

kmp_search(S, find)

print(cnt)