try:
    with open('example.txt', 'w') as file:
        file.write("Hello world")
except FileNotFoundError:
    print("File not found")

try:
    with open('example.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found")

try:
    with open('example.txt', 'a') as file:
        file.write("\nThis is a new line")
except FileNotFoundError:
    print("File not found")

try:
    with open('example.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found")