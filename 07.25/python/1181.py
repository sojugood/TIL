N = int(input())

word_set = set()

for _ in range(N):
    n = input()
    word_set.add(n)

word_list = list(word_set)
word_list.sort(key = lambda x: (len(x), x))

for i in word_list:
    print(i)