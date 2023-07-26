class Robot:
    def __init__(self):
        print("부모 클래스의 func1 메서드 실행")
        self.money = 100

class Study_bot(Robot):
    def __init__(self):
        super().__init__()
        print("자식 클래스의 func2 메서드 실행")
        self.book = 10

bot1 = Study_bot()
print(bot1.book)
print(bot1.money)
