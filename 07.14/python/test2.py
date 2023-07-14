import random
import time


students = [
    '강문수','김동영','김민진','박수빈','박영진','배영환','서준하','서지수','손유정','신현중','심상익','원종현',
    '유영준','윤태우','이상훈','이장하','이재진','장지민','정세진','정종길','최도훈','황호철','추합1','추합2'
]

random.shuffle(students)

count_num = 0
team_num = 1

check_last_team = len(students)


def make_team():
    global count_num
    global team_num
    global check_last_team

    if count_num % 3 == 0:
        print(team_num, end=' ')
        team_num += 1
    print(student, end=' ')
    time.sleep(1)

    count_num += 1
    check_last_team -= 1

    if count_num % 3 == 0:
        print()


for student in students:
    if len(students) % 2 == 0:
        make_team()

    else:
        make_team()
        if check_last_team == 3:
            print(team_num, end=' ')
            print(' '.join(students[-3:]))
            break

numbers = [1,2,3,4,5,6,7,8]
random.shuffle(numbers)
print(numbers)