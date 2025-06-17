# Initial lists
names = ["Bob", "Angel", "Jimi", "Alan", "Ada"]
full_names = ["Bob Martin", "Angel Harlem", "Jimi Hendrix", "Alan Turing", "Ada Lovelace"]
almost_numbers = ['0', '10', '21', '3', '-7', '88', '9']
# TODO: list comprehension to create a list of all the full_names in lowercase format
lowercase_full_names = [name.lower() for name in full_names]
print(lowercase_full_names)
# TODO: list comprehension to create a list of integers from the above list of strings
numbers = [int(number) for number in almost_numbers]
print(numbers)
# TODO: list comprehension to create a list of only the numbers that are greater than 9
greater_than_nine = [number for number in numbers if number > 9]
print(greater_than_nine)
# TODO: (more advanced) use a list comprehension and the join string method
# to create a string (not list) of the last names for those full names longer than 11 characters
long_full_names = [name.split()[1] for name in full_names if len(name) > 11]
last_names_string = ", ".join(long_full_names)
print(last_names_string)