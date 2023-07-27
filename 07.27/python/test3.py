class Student():
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