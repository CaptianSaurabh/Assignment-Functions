# # Write a Python function that takes a list of numbers as input and returns the sum of all even numbers in the list


def sum_of_even_numbers(numbers):
    return sum(num for num in numbers if num % 2 == 0)

input_list = [1, 2, 3, 4, 5, 6]
result = sum_of_even_numbers(input_list)
print(result)  # This will output 12, which is the sum of 2, 4, and 6 from the input list


