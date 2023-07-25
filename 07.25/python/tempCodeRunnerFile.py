# case 2 : .get()
new_dict = {}
# blood_types를 순회하면서
for blood_type in blood_types:
    # get( , 0) + 1 <- default 값에 0을 넣고 get 메서드 밖에 1을 더해주어야 값이 존재할 경우에 +1을 할 수 있음. default는 값이 없을 때 처리하는 부분이기 때문
    new_dict[blood_type] = new_dict.get(blood_type, 0) + 1
    
print(new_dict)