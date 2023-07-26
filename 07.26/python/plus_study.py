class Robot:
    def func1(self):
        print("부모 클래스의 func1 메서드 실행")
        self.money = 100

class Study_bot(Robot):
    def func2(self):
        print("자식 클래스의 func2 메서드 실행")
        self.book = 10

bot1 = Study_bot()
bot1.func1() # 부모 함수를 실행해야 부모의 속성도 가져오게 된다.
bot1.func2()
print(bot1.book)
print(bot1.money)
