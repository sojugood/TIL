replacements = {'A+' : 4.5, 'A0' : 4.0, 'B+' : 3.5, 'B0' : 3.0, 'C+' : 2.5, 'C0' : 2.0, 'D+' : 1.5, 'D0' : 1.0, 'F' : 0.0}

level = []
scores = []

for _ in range(20):
    n = input().split()
    if 'P' in n[2]:
        continue
    else:
        for i, word in enumerate(n):
            if word in replacements:
                n[i] = replacements[word]

        level.append(float(n[1]))
        score = float(n[1]) * float(n[2])
        scores.append(score)


result = sum(scores) / sum(level)
print(result)
