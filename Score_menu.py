import random

def determine_score_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def get_valid_score():
    score = -1
    while score < 0 or score > 100:
        try:
            score = float(input("Enter a valid score (0-100): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
    return score

def print_stars(score):
    print("*" * int(score))

def main():
    score = get_valid_score()
    menu = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""
    print(menu)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(determine_score_result(score))
        elif choice == "S":
            print_stars(score)
        else:
            print("Invalid choice. Please select from the menu.")
        print(menu)
        choice = input(">>> ").upper()
    print("Farewell!")

if __name__ == "__main__":
    main()