'''
n = 1 + 36 + 36**2 + 36**3 + 36**4

print(35*n)

N : A ~ Z

A : 10



Z : 35

2 <= B <= 36
'''
n, b = input().split()

n = n[::-1]
num_ten = 0
# A-Z를 리스트로 만듭니다
letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

# 10-35를 리스트로 만듭니다
numbers = list(range(10, 36))

# 두 리스트를 zip 함수로 묶어서 딕셔너리로 만듭니다
letter_to_number = dict(zip(letters, numbers))


for i in range(len(n)):
    if n[i] in letters:
        num_ten += (int(b) ** i) * letter_to_number[n[i]]
    else:
        num_ten += (int(b) ** i) * int(n[i])

print(num_ten)