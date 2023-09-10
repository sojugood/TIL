import math

R = 6

hole = [254, 127]

target = [200, 80]

ball = [100, 50]

rad1 = math.atan2(hole[1] - target[1], hole[0] - target[0])

goal = [None, None]

goal[0] = R * math.cos(rad1)
goal[1] = R * math.sin(rad1)

print(goal)
# [4.525828316586867, 3.939146868140421]

real_goal = [target[0] - goal[0], target[1] - goal[1]]

print(real_goal)
# [195.47417168341315, 76.06085313185957]

rad2 = math.atan2(real_goal[1] - ball[1], real_goal[0] - ball[0])

print(90 - math.degrees(rad2))
# 74.73234620836267