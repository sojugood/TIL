class Person:
    blood_color = 'red' # 클래스 변수
    def __init__(self, name):
        self.name = name

	#   p.name = 'Kim'
    def singing(self):
        return f'{self.name}가 노래합니다.'




p = Person('Kim') # (self.name = p.name(인스턴스 변수) / name = Kim)
print(p.name)
print(p.singing())