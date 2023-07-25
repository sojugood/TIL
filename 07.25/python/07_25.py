# 혈액형 인원수 세기
# 결과 => {'A': 3, 'B': 3, 'O': 3, 'AB': 3}
blood_types = ['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB']

# case 1 : []
new_dict = {}
# blood_types를 순회하면서
for blood_type in blood_types:
    # 기존에 키가 이미 존재한다면,
    if blood_type in new_dict:
        # 해당 키의 값을 +1
        new_dict[blood_type] += 1
    # 키가 존재하지 않는다면(처음 설정되는 키)
    else:
        new_dict[blood_type] = 1

print(new_dict)


# case 2 : .get()
new_dict = {}
# blood_types를 순회하면서
for blood_type in blood_types:
    # get( , 0) + 1 <- default 값에 0을 넣고 get 메서드 밖에 1을 더해주어야 값이 존재할 경우에 +1을 할 수 있음. default는 값이 없을 때 처리하는 부분이기 때문
    new_dict[blood_type] = new_dict.get(blood_type, 0) + 1
    
print(new_dict)


# case 3 : .setdefault()
new_dict = {}

for blood_type in blood_types:
    new_dict.setdefault(blood_type, 0)
    new_dict[blood_type] += 1
    
print(new_dict)