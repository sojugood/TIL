# 실습 번호.py
'''
실습 4에서 작성한 코드를 활용하여 many_user 변수에 모든 신규 고객 정보 딕셔너리를 요소로 갖는 리스트를 할당한다.

실습 3에서 작성한 코드를 활용하여 book.py에 decrease_book 함수를 작성한다.

rental_book 함수는 info 인자 하나만 할당 받을 수 있다.
	info 인자는 신규 고객의 이름과 나이를 담은 딕셔너리이다.
	신규 고객의 나이를 10으로 나눈 몫을 대여할 책의 수로 활용한다.(decrease_book 함수의 인자)
	info 인자에 사용될 딕셔너리는 many_user와 map을 사용해 새로운 딕셔너리를 생성한다.
		이 떄, map에 사용될 함수는 lambda로 구현한다.
		그 결과를 rental_book 함수에 각각 전달하여 호출한다. 이 때 역시 map 함수를 사용한다.
'''
import book
number_of_people = 0


def increase_user():
    global number_of_people
    number_of_people += 1


name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']


def create_user(name, age, address):
    increase_user()
    print(f"{name}님 환영합니다!")
    return {'name': name, 'age': age, 'address': address}


many_user = list(map(create_user, name, age, address))


def rental_book(info):
    book_number = info['age'] // 10
    book.decrease_book(book_number)
    print(f"{info['name']}님이 {book_number}권의 책을 대여하였습니다.")


users_info = list(map(lambda x: {'name': x['name'], 'age': x['age']}, many_user))


list(map(rental_book, users_info))
