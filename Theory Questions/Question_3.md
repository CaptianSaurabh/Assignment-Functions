What are the different ways to define and call a function in Python ?

Answer > Here are the different ways to define and call a function in Python:

Defining a Function:


1. Simple Function: def func_name(parameters):
def greet(name):
    print("Hello, " + name)


2. Function with Default Values: def func_name(parameters = default_value):
def greet(name = "World"):
    print("Hello, " + name)


3. Lambda Function: func_name = lambda parameters: expression
greet = lambda name: print("Hello, " + name)


4. Generator Function: def func_name(parameters): yield expression
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1


Calling a Function:
1. Positional Arguments: func_name(arg1, arg2, ...)
greet("John")

2. Keyword Arguments: func_name(param1 = arg1, param2 = arg2, ...)
greet(name = "John")

3. Default Argument Values: func_name(arg1, arg2 = default_value, ...)
greet("John", age = 30)


4. Variable Number of Arguments: func_name(*args, **kwargs)
def greet_multiple(*names):
    for name in names:
        print("Hello, " + name)

greet_multiple("John", "Alice", "Bob")


Note: This is not an exhaustive list, but it covers the most common ways to define and call functions in Python.