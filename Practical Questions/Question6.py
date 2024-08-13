## Write a generator function in Python that yields the powers of 2 up to a given exponent

def power_generator(base, exponent):
    result = 1
    for _ in range(exponent + 1):
        yield result
        result *= base

# Example Usage
base = 2
exponent = 5
power_gen = power_generator(base, exponent)
print(f"Powers of {base} up to exponent {exponent}:")
for power in power_gen:
    print(power, end=" ")