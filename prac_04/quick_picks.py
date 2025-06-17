"""""
Practical 04 Quick Picks
"""""
import random

# Constants for range of numbers
MIN_NUM = 1
MAX_NUM = 45
NUM_PICK = 6


# Function to generate quick picks
def generate_quick_picks(num_picks):
    picks = []
    for _ in range(num_picks):
        pick = random.sample(range(MIN_NUM, MAX_NUM + 1), NUM_PICK)  # Select 6 unique random numbers
        pick.sort()  # Sort the numbers in ascending order
        picks.append(pick)
    return picks


# Main program
def main():
    # Get the number of quick picks from the user
    try:
        num_picks = int(input("How many quick picks? "))
        if num_picks < 1:
            print("The number of picks must be at least 1.")
            return

        # Generate the quick picks
        quick_picks = generate_quick_picks(num_picks)

        # Display the picks with formatting
        for pick in quick_picks:
            print(" ".join(f"{num:2}" for num in pick))  # Format numbers to align properly
    except ValueError:
        print("Invalid input! Please enter an integer.")


# Run the program
if __name__ == "__main__":
    main()
