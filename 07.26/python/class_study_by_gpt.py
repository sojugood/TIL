class Person:
    def __init__(self, name):  
        # __init__ 메서드는 생성자라고 부릅니다. 객체가 생성될 때 자동으로 호출됩니다.
        # self는 인스턴스 객체 자신을 참조합니다.
        # 여기서 name은 인스턴스 변수입니다. 각 인스턴스 마다 다른 값을 가질 수 있습니다.
        self.name = name

    def greet(self): 
        # 이것이 인스턴스 메서드입니다. self를 첫 번째 인자로 받아 인스턴스에 접근합니다.
        # 이 메서드는 인스턴스 변수 name을 사용하여 인사를 출력합니다.
        print(f"Hello, my name is {self.name}.")

person = Person("Alice")  
# Person 클래스의 인스턴스를 만들고, 이를 person이라는 변수에 할당합니다.
# 이 때 "Alice"는 __init__ 메서드의 name 파라미터로 전달됩니다.

person.greet()  # "Hello, my name is Alice."
# greet 인스턴스 메서드를 호출합니다. self 인자는 파이썬에서 자동으로 전달됩니다.


