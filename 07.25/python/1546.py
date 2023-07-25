N = int(input())

score = list(map(int, input().split()))

score.sort(reverse=True)

max_score = score[0]

score_list = []
for i in score:
    new_score = (i / max_score) * 100
    score_list.append(new_score)

result = sum(score_list) / len(score_list)

print(result)