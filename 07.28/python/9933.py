N = int(input())

password_list = []

for i in range(N):
    n = input()
    password_list.append(n)

for i in password_list:
    if i[::-1] in password_list:
        print(len(i), i[len(i) // 2])
        break
