# 캡슐(은닉)화(Encapsulation)
class Student:
    def __init__(self, name, age, id, grade):
        self.name = name
        self.age = age
        self.id = id
        self.__grade = grade # 은닉

    def grade(self): # 호출
        return self.__grade

Lee = Student('Lee', 24, '204712312', 4.3)
print(Lee.name)
print(Lee.grade())
# __로 은닉하고 접근하기 위해서는 인스턴스 메서드로 해당 변수를 호출해야함


# 추상화 + 다형성
class Animal:
    def __init__(self, name):
        self.name = name

    def bark(self): # 추상적 메서드
        print("울음소리")

class Cat(Animal):
    def bark(self): # Cat 클래스에서 bark 메서드 재정의(오버라이드)
        return "냐옹"
    
class Dog(Animal):
    def bark(self): # Dog 클래스에서 bark 메서드 재정의(오버라이드)
        return "왈왈"
    
cat1 = Cat('고양이1')
dog1 = Dog('개1')
print(cat1.bark())
print(dog1.bark())
# 하나의 인터페이스(메서드)를 다양한 방식으로 구현할 수 있는 능력

