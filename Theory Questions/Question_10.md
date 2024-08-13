What is the difference between map(), reduce(), and filter() functions in Python ?

Answer > 
Here's a brief overview of each function with an example:

1. map(): Applies a function to each item in an iterable, returning a new iterable with the results.

Example: list(map(lambda x: x**2, [1, 2, 3, 4, 5])) → [1, 4, 9, 16, 25]

2. reduce(): Applies a function to the first two items in an iterable, then to the result and the next item, and so on, reducing the iterable to a single output.

Example: from functools import reduce; reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) → 15

3. filter(): Returns a new iterable with only the items from the original iterable that meet a certain condition.

Example: list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5])) → [2, 4]

In short: map() transforms, reduce() aggregates, and filter() selects!