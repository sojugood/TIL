import park

# 세 명의 키를 입력받습니다.
height1, height2, height3 = map(int, input().split())

# 각각의 키에 대해 탈 수 있는 놀이기구를 찾습니다.
rides1 = set(park.allowedrides(height1))
rides2 = set(park.allowedrides(height2))
rides3 = set(park.allowedrides(height3))

# 세 사람이 모두 탈 수 있는 놀이기구는 세 set의 교집합입니다.
common_rides = rides1 & rides2 & rides3

# 결과를 출력합니다.
print("\n")
for ride in common_rides:
    print(ride)
