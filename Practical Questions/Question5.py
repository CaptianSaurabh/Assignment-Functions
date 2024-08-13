## Create an iterator class in Python that generates the Fibonacci sequence up to a specified number of terms ?

class FibonacciIterator:
    def __init__(self, max_terms):
        self.max_terms = max_terms
        self.a = 0
        self.b = 1
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.max_terms:
            result = self.a
            self.a, self.b = self.b, self.a + self.b
            self.count += 1
            return result
        else:
            raise StopIteration

# Example Usage
fibonacci_terms = 10
fib_sequence = FibonacciIterator(fibonacci_terms)
for term in fib_sequence:
    print(term, end=" ")