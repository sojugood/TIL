N = int(input())

numbers = map(int, input().split())

student_list = list(range(1, N + 1))

for i, j in zip(numbers, range(N)):
    number = student_list[j]
    student_list.remove(number)
    student_list.insert(j - i, number)

print(*student_list)