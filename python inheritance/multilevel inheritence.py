# Grandparent class
class Grandparent:
    def greet_grandparent(self):
        print("Hello from Grandparent")

# Parent class 
class Parent(Grandparent):
    def greet_parent(self):
        print("Hello from Parent")

# Child class 
class Child(Parent):
    def greet_child(self):
        print("Hello from Child")

# Create object of Child
c = Child()

# Access methods from all classes
c.greet_grandparent() 
c.greet_parent()      
c.greet_child()       
