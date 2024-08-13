## Use a lambda function in Python to sort a list of tuples based on the second element of each tuple?

# List of tuples
tuple_list = [('apple', 5), ('banana', 2), ('cherry', 10), ('date', 7)]

# Sort the list of tuples based on the second element of each tuple using a lambda function
sorted_tuples = sorted(tuple_list, key=lambda x: x[1])

# Output the sorted list
print(sorted_tuples)