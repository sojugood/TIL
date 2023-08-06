import sys
input = sys.stdin.readline

N = int(input())

num_list = []

for _ in range(N):
    num = int(input())
    num_list.append(num)

# 산술평균
def rounding(n):
    if n >= 0:
        return int(n) + 1 if n - int(n) >= 0.5 else int(n)
    else:
        return -(int(-n) + 1) if -n - int(-n) >= 0.5 else -int(-n)

result_1 = rounding(sum(num_list) / len(num_list))

# 중앙값
num_list.sort()

result_2 = num_list[N//2]

# 최빈값
# 빈도수 계산
frequency_dict = {}
for num in num_list:
    frequency_dict[num] = frequency_dict.get(num, 0) + 1

# 최빈값 찾기
max_count = max(frequency_dict.values())
most_frequent_values = [k for k, v in frequency_dict.items() if v == max_count]

# 두 번째 최빈값 처리 (최빈값이 둘 이상인 경우)
most_frequent_values.sort()
result_3 = most_frequent_values[1] if len(most_frequent_values) > 1 else most_frequent_values[0]


# 범위
result_4 = num_list[-1] - num_list[0]

# 출력
print(result_1)
print(result_2)
print(result_3)
print(result_4)