What are iterators in Python and how do they differ from iterables ?

Answer >

In Python, an iterable is an object that can be iterated over, meaning it can be used in a for loop or with the iter() function to access its elements one at a time. Examples of iterables include lists, tuples, strings, dictionaries, and sets.

An iterator, on the other hand, is an object that keeps track of its position in a sequence and yields the next value in the sequence when its __next__() method is called. In other words, an iterator is an object that allows you to iterate over an iterable.

Here's a key difference:

An iterable is the object itself (e.g., a list or string).
An iterator is an object that helps you iterate over the iterable (e.g., a pointer to the current element in the list or string).

When you create an iterator from an iterable using the iter() function, the iterator remembers its position in the sequence. Each time you call __next__() on the iterator, it returns the next value in the sequence. When there are no more values, it raises a StopIteration exception.

Here's an example:

my_list = [1, 2, 3, 4, 5]  # iterable
my_iterator = iter(my_list)  # create an iterator from the iterable

print(next(my_iterator))  # 1
print(next(my_iterator))  # 2
print(next(my_iterator))  # 3
print(next(my_iterator))  # 4
print(next(my_iterator))  # 5
print(next(my_iterator))  # raises StopIteration

In summary:
Iterables are objects that can be iterated over.
Iterators are objects that help you iterate over iterables, keeping track of their position in the sequence.