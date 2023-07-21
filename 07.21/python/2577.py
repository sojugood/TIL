A = int(input())
B = int(input())
C = int(input())

ABC = A * B * C

ABC_list = list(str(ABC))

for i in range(10):
    print(ABC_list.count(str(i)))