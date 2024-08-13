## Implement a Python function that takes a list of integers and returns a new list containing the squares of each number?

def square_numbers(input_list):
    return [x**2 for x in input_list]

# Example Usage
input_list = [1, 2, 3, 4, 5]
squared_list = square_numbers(input_list)
print(squared_list)