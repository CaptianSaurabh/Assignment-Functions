What is the difference between a function and a method in Python ?

Answer >> In Python, a function and a method are both blocks of code that can be executed multiple times from different parts of your program. The key difference is:

> A function is a standalone block of code that can be called multiple times from different parts of your program.
> A method is a block of code that is part of a class or object, and is used to perform a specific action on that object.


In other words, all methods are functions, but not all functions are methods.

Example.. 

# Function
def greet(name):
    print("Hello, " + name)

greet("John")  # Output: Hello, John

# Method
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello, " + self.name)

p = Person("John")
p.greet()  # Output: Hello, John