"""
CP1404/CP5632 - Practical 03
Random Numbers
"""

import random

# Line 1: Generates a random integer between 5 and 20 (inclusive)
print(random.randint(5, 20))  # Example output: 12

# Smallest possible number: 5
# Largest possible number: 20

# Line 2: Generates a random number from the range 3 to 10 with a step of 2 (3, 5, 7, 9)
print(random.randrange(3, 10, 2))  # Example output: 7

# Smallest possible number: 3
# Largest possible number: 9
# Could line 2 have produced a 4? No, because the step of 2 means only 3, 5, 7, or 9 can be chosen.

# Line 3: Generates a random floating-point number between 2.5 and 5.5
print(random.uniform(2.5, 5.5))  # Example output: 4.23

# Smallest possible number: 2.5
# Largest possible number: 5.5

# Code to generate a random number between 1 and 100 inclusive
random_number = random.randint(1, 100)
print(random_number)  # Example output: 87