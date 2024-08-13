# Write a Python function that checks if a given number is prime or not from 1 to 200 ?


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Check if a number is prime from 1 to 200
def check_prime_numbers():
    for num in range(1, 201):
        if is_prime(num):
            print(f"{num} is a prime number")
        else:
            print(f"{num} is not prime number")

# Call the function to check prime numbers from 1 to 200
check_prime_numbers()