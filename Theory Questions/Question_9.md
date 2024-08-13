Explain the purpose and usage of the map() function in Python / with example ? 

Answer >

The map() function in Python is a built-in function that applies a given function to each item of an iterable (such as a list, tuple, or string) and returns a list of the results.

Purpose:

The purpose of map() is to transform or manipulate each element of an iterable by applying a function to it, without modifying the original iterable.

Usage:

The syntax for map() is:

map(function, iterable)

Where:
1. function is the function to be applied to each element of the iterable.
2. iterable is the iterable (such as a list, tuple, or string) to be processed.
Example:
Let's say we have a list of numbers and we want to square each number:

numbers = [1, 2, 3, 4, 5]
# Define a function to square a number
def square(x):
    return x ** 2
# Use map() to apply the square function to each number
squared_numbers = list(map(square, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]


In this example, the map() function applies the square() function to each element of the numbers list, returning a new list squared_numbers with the squared values.

Note: In Python 3.x, map() returns an iterator, so we need to convert it to a list using the list() function. In Python 2.x, map() returns a list directly.

Lambda Function Example:

We can also use a lambda function with map() to make the code more concise:

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

In this example, the lambda function lambda x: x ** 2 is applied to each element of the numbers list, returning a new list with the squared values