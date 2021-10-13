class Person:
    arms_count= 2

    def greet(self):
        print(f'Hi {self.name}!')

    def __init__(self):
        self.name = 'Test'


me=Person()
you=Person()

me.name='Nick'
you.name="Vasya"

print(me.arms_count, you.arms_count)
me.greet()
you.greet()

me.arms_count = 5
print(me.arms_count, you.arms_count)

print(me.name, you.name)

me.age=23
print(me.age)