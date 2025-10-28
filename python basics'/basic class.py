class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def intro(self):
        print("hello my name is " + self.name)
        print("Age " + self.age)

result = Person("arman", "18")
result.intro()
