"""
CP1404/CP5632 - Practical
What's your name?
Let's sum it up.
"""


# Task 1: Ask the user for their name and write it to a file
name = input("What is your name? ")
file = open('name.txt', 'w')
file.write(name)
file.close()

# Task 2: Open "name.txt", read the name, and print it
file = open('name.txt', 'r')
name_from_file = file.read()
file.close()
print(f"Hi {name_from_file}!")

# Task 3: Create a file "numbers.txt", write numbers, and sum the first two
numbers = [17, 42, 400]
with open('numbers.txt', 'w') as file:
    for number in numbers:
        file.write(f"{number}\n")

with open('numbers.txt', 'r') as file:
    number1 = int(file.readline())
    number2 = int(file.readline())

sum_result = number1 + number2
print(f"The sum of the first two numbers is: {sum_result}")

# Task 4: Print the total sum of all numbers in the "numbers.txt"
total = 0
with open('numbers.txt', 'r') as file:
    for line in file:
        total += int(line)

print(f"The total of all numbers is: {total}")