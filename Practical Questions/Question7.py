## Implement a generator function that reads a file line by line and yields each line as a string

def file_reader(filepath):
    with open(filepath, 'r') as file:
        for line in file:
            yield line.strip()

# Example Usage
file_path = "example.txt"
line_generator = file_reader(file_path)
for line in line_generator:
    print(line)