"""
CP1404/CP5632 - Practical
Score Menu Program
"""

def main():
    score = get_valid_score()
    # Display the score menu and handle user input choices
    MENU = "(G)et score\n(P)print result\n(S)how stars\n(Q)uit"
    print(MENU)
    choice = input(">>> ").upper()

    while choice != "Q":
        if "G" == choice:
            score = get_valid_score()
        elif choice == "P":
            result = determine_score_status(score)
            print(result)
        elif choice == "S":
            print_stars(score)
        else:
            print("Invalid choice")

        print(MENU)
        choice = input(">>> ").upper()

    print("Goodbye!")


def get_valid_score():
    """Prompt user for a valid score between 0 and 100 inclusive."""
    score = float(input("Enter score (0-100): "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score (0-100): "))
    return score


def determine_score_status(score):
    """Return the status of the score as a string."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def print_stars(score):
    """Print as many stars as the integer value of the score."""
    print("*" * int(score))


# Run the main function
main()