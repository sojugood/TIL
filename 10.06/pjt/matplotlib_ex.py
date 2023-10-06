import matplotlib.pyplot as plt

# 1. x, y 가 같을 때
plt.plot([0, 1, 2, 3])
# plt.show()

# 지금까지 그렸던 plot 지우기
plt.clf()


# 2. x, y 가 다를 때
x = [1, 2, 3, 4]
y = [2, 4, 8, 16]
plt.plot(x, y)
# plt.show()

plt.clf()


# 3. 제목 + 각 축의 설명
plt.plot(x, y)

# 제목
plt.title("Test graph")

# x, y 축
plt.ylabel('y label')
plt.xlabel('x label')

# plt.show()


# 파일로 저장하기(plt.show() 하면 정보가 날라가기 때문에 show 하지 말고 저장)
plt.savefig('filename.png')