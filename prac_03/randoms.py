import random

print(random.randint(5, 20))  # line 1
# Smallest = 5, Largest = 20

print(random.randrange(3, 10, 2))  # line 2
# Smallest = 3, Largest = 9
# Could be: 3, 5, 7, 9
# No, it could not have produced a 4

print(random.uniform(2.5, 5.5))  # line 3
# Smallest = 2.5, Largest = 5.5 (float in this range)

# Generate a random number between 1 and 100 inclusive
random_number = random.randint(1, 100)
print(random_number)