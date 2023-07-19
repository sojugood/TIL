number_of_people = 0

def increase_user():
    global number_of_people
    number_of_people += 1

def create_user(user_info):
    increase_user()
    print(f"{user_info['name']}님 환영합니다!")

names = ['김시습', '허균', '남영로', '임제', '박지원']
ages = [20, 16, 52, 36, 60]
addresses = ['서울', '강릉', '조선', '나주', '한성부']

users_info = [{'name': n, 'age': a, 'address': ad} for n, a, ad in zip(names, ages, addresses)]

list(map(create_user, users_info))

# 마지막에 한 번만 딕셔너리 리스트 출력
print(users_info)
