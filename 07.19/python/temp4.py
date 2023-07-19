# main.py
import book
number_of_people = 0

def increase_user():
    global number_of_people
    number_of_people += 1

def create_user(name, age, address):
    increase_user()
    print(f"{name}님 환영합니다!")
    return {'name': name, 'age': age, 'address': address}

def rental_book(info):
    book_number = info['age'] // 10
    book.decrease_book(book_number)
    print(f"{info['name']}님이 {book_number}권의 책을 대여하였습니다.")

names = ['김시습', '허균', '남영로', '임제', '박지원']
ages = [20, 16, 52, 36, 60]
addresses = ['서울', '강릉', '조선', '나주', '한성부']

users_info = list(map(create_user, names, ages, addresses))

many_user = list(map(lambda x: {'name': x['name'], 'age': x['age']}, users_info))

list(map(rental_book, many_user))

