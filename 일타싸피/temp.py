import socket
import time
import math

# User and Game Server Information
NICKNAME = '파이썬'
HOST = '127.0.0.1'
PORT = 1447 # Do not modify

# predefined variables(Do not modify these values)
TABLE_WIDTH = 254
TABLE_HEIGHT = 124
NUMBER_OF_BALLS = 5
HOLES = [ [0, 0], [130, 0], [260, 0], [0, 130], [130, 130], [260, 130] ]

class Conn:
    def __init__(self):
        self.sock = socket.socket()
        print('Trying to Connect: ' + HOST + ':' + str(PORT))
        self.sock.connect((HOST, PORT))
        print('Connected: ' + HOST + ':' + str(PORT))
        send_data = '9901/' + NICKNAME
        self.sock.send(send_data.encode('utf-8'))
        print('Ready to play.\n--------------------')
    def request(self):
        self.sock.send('9902/9902'.encode())
        print('Received Data has been currupted, Resend Requested.')
    def receive(self):
        recv_data = (self.sock.recv(1024)).decode()
        print('Data Received: ' + recv_data)
        return recv_data
    def send(self, angle, power):
        merged_data = '%d/%d' % (angle, power)
        self.sock.send(merged_data.encode('utf-8'))
        print('Data Sent: ' + merged_data)
    def close(self):
        self.sock.close()

class GameData:
    def __init__(self):
        self.reset()
    def reset(self):
        self.balls = [[0, 0] for i in range(NUMBER_OF_BALLS)]
    def read(self, conn):
        recv_data = conn.receive()
        split_data = recv_data.split('/')
        idx = 0
        try:
            for i in range(NUMBER_OF_BALLS):
                for j in range(2):
                    self.balls[i][j] = int(split_data[idx])
                    idx += 1
        except:
            self.reset()
            conn.request()
            self.read(conn)
    def show(self):
        print('=== Arrays ===')
        for i in range(NUMBER_OF_BALLS):
            print('Ball%d: %d, %d' % (i, self.balls[i][0], self.balls[i][1]))
        print()

# 자신의 차례가 되어 게임을 진행해야 할 때 호출되는 Method
def cal(balls):
    palyer_ball = balls[0]
    target_ball = None
    min_distance = float("inf")

    for ball in balls[1:]:
        distance = math.sqrt((ball[0] - palyer_ball[0])**2 + (ball[1] - palyer_ball[1])**2)
        if distance < min_distance and ball[0] != 0 and ball[1] != 0:
            target_ball = ball
            min_distance = distance
    
    dx = target_ball[0] - palyer_ball[0]
    dy = target_ball[1] - palyer_ball[1]

    radian_angle = math.atan2(dy, dx)
    angle = 90 - math.degrees(radian_angle)

    if min_distance < 50:
        power = 50
    elif min_distance < 100:
        power = 100
    else:
        power = 150

    return angle, power

def play(conn, gameData):
    angle = 0
    power = 0

    angle, power = cal(gameData.balls)
    ######################################################################################
    # 주어진 정보를 바탕으로 샷을 할 방향과 세기를 결정해서 angle, power 값으로 지정 #
    ######################################################################################
    conn.send(angle, power)


def main():
    conn = Conn()
    gameData = GameData()
    while True:
        gameData.read(conn)
        gameData.show()
        play(conn, gameData)        
    conn.close()
    print('Connection Closed')

if __name__ == '__main__':
    main()