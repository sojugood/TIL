class Person:
    name = 'unknown'

    def talk(self):
        print(self.name)

p1 = Person()
p1.talk()

p1.address = 'korea'
print(p1.address)

p2 = Person()
p2.talk()
p2.name = 'Kim'
p2.talk()

print(Person.name)
print(p1.name)
print(p2.name)