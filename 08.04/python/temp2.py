import sys
input = sys.stdin.readline
N = int(input())
if N == 0:
    print(0)
else:
    score_list = []
    for _ in range(N):
        n = int(input())
        score_list.append(n)

    def rounding(n): return int(n) + 1 if n - int(n) >= 0.5 else int(n)

    delete = rounding(N * 0.15)
    score_list.sort()
    score_list = score_list[delete:-delete] if delete != 0 else score_list

    result = rounding(sum(score_list) / len(score_list))
    print(result)