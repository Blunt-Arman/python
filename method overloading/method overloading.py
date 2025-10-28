class Parent:
    def show(self):
        print("Hello")

class Child(Parent):
    def show(self):
        print("Hii")

d = Child()
d.show()
