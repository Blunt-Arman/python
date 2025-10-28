# Parent class
class Parent:
    def greet_parent(self):
        print("Hello from Parent")

# Child class inheriting from Parent
class Child(Parent):
    def greet_child(self):
        print("Hello from Child")

# Create object of Child
c = Child()

# Access methods
c.greet_parent()  
c.greet_child()   
