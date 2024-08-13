## Write a Python program that uses `map()` to convert a list of temperatures from Celsius to Fahrenheit?

# Celsius to Fahrenheit conversion function
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# List of temperatures in Celsius
celsius_temperatures = [0, 12, 45.21, 34, 99.91]

# Use map() to convert the list of temperatures to Fahrenheit
fahrenheit_temperatures = list(map(celsius_to_fahrenheit, celsius_temperatures))

# Output the original and converted temperatures
print("Celsius temperatures:", celsius_temperatures)
print("Fahrenheit temperatures:", fahrenheit_temperatures)