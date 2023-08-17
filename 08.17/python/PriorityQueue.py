from queue import PriorityQueue

q = PriorityQueue(maxsize = 8)



# 추가
q.put((1, 'B'))
q.put((2, 'D'))
q.put((3, 'A'))
q.put((4, 'C'))

print(q.get()[1])
print(q.get())
print(q.get())
print(q.get())