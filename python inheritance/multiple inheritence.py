# Parent class 1
class Parent1:
    def greet1(self):
        print("Hello from Parent1")

# Parent class 2
class Parent2:
    def greet2(self):
        print("Hello from Parent2")

# Child class 
class Child(Parent1, Parent2):
    def greet_child(self):
        print("Hello from Child")

# Create object of Child
c = Child()

# Access methods from all classes
c.greet1()       
c.greet2()       
c.greet_child()  
