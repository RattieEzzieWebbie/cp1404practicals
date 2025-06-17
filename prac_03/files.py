# 1. Ask for user's name and write it to a file (using open and close)
name = input("Enter your name: ")
out_file = open("name.txt", "w")
out_file.write(name)
out_file.close()

# 2. Read name from file and greet the user (using open and close)
in_file = open("name.txt", "r")
name_from_file = in_file.read().strip()
in_file.close()
print(f"Hi {name_from_file}!")

# 3. Read first two numbers from numbers.txt, add and print the result (use with and readlines)
with open("numbers.txt", "r") as in_file:
    lines = in_file.readlines()
    number1 = int(lines[0])
    number2 = int(lines[1])
    print(number1 + number2)  # Should print 59

# 4. Read all numbers and print the total (use with and for line in file)
total = 0
with open("numbers.txt", "r") as in_file:
    for line in in_file:
        total += int(line)
print(total)