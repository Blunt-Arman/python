# Parent class
class Parent:
    def display(self):
        print("This is the Parent class")

# Child class 1
class Child1(Parent):
    def show1(self):
        print("This is Child1 class")

# Child class 2
class Child2(Parent):
    def show2(self):
        print("This is Child2 class")

# Create objects
obj1 = Child1()
obj2 = Child2()

# Access parent method from both children
obj1.display()
obj1.show1()

obj2.display()
obj2.show2()
