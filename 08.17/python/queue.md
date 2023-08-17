# queue1

def enQ(data):
    global rear
    # if rear == Qsize - 1:
    if Full():
        print("Queue full")
    rear += 1
    Q[rear] = data

def deQ():
    global front
    # if front == Qsize - 1:
    if isEmpty():
        print("Queue empty")
    else:
        front += 1
        return Q[front]

def isEmpty():
    global front
    global rear
    return front == rear

def Full():
    global front
    global rear
    return rear == len(Q) - 1

def Qpeek():
    global front
    if isEmpty():
        print("Queue empty")
    else:
        return Q[front+1]



Q = [0] * 3
Qsize = len(Q)
rear = -1
front = -1

enQ(1)
enQ(2)
enQ(3)


print(deQ())
print(deQ())
print(Qpeek())



# queue 2

# Q = []
# #추가
# Q.append('a')
# Q.append('B')
# print(Q)
# #삭제
# print(Q.pop(0))
# print(Q.pop(0))
#
# queue = [0] * 100
# front = -1
# rear = -1
#
# rear += 1
# queue[rear] = 'a'
# rear += 1
# queue[rear] = 'b'
# print(queue)
#
# front += 1
# print(queue[front])
# front += 1
# print(queue[front])

from collections import deque
q = deque()
q.append('a')
q.append('b')
print(q)
print(q.popleft())
print(q.popleft())



# queue 3

#초기 공백 상태
front = rear = 0

#index 순환 -> front와 rear가 배열의 마지막 인덱스인 n-1을 가리킨 후
#그다음 0으로이동해야함 -> 나머지 연산자 mod 사용
#기존에 mod n만 추가한다고 생각


# 원형 큐
def enq(data):
    global rear
    global front
    # if (rear+1) % cQsize == front:
    #     print("cQ is Full")
    if (rear+1) % cQsize == front:
        front = (front+1) % cQsize
    #Queue가 가득찼을때 덮어쓰기
    else:
        rear = (rear + 1) % cQsize
        cQ[rear] = data

def deq():
    global front
    front = (front + 1) % cQsize
    return cQ[front]


cQsize = 4
cQ = [0] * cQsize
front = 0
rear = 0


enq(1)
enq(2)
enq(3)
enq(4)
enq(5)
print(deq())
print(deq())
print(cQ)
