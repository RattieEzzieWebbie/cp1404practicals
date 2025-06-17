# CP1404/CP5632 - Practical
# Exception handling with proper input validation

def main():
    numerator = get_valid_number("Enter the numerator: ")
    denominator = get_valid_denominator("Enter the denominator (non-zero): ")
    fraction = numerator / denominator
    print(fraction)
    print("Finished.")

def get_valid_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")

def get_valid_denominator(prompt):
    while True:
        try:
            denominator = int(input(prompt))
            if denominator == 0:
                print("Denominator cannot be zero.")
            else:
                return denominator
        except ValueError:
            print("Please enter a valid integer.")

main()