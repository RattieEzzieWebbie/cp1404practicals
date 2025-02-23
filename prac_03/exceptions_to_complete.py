"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        is_finished = True  # Exit the loop if the conversion is successful
    except ValueError:  # Catch the error when the input cannot be converted to an integer
        print("Please enter a valid integer.")
print("Valid result is:", result)