"""
CP1404/CP5632 - Practical
Program to determine score status
"""

import random

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

def main():
    score = float(input("Enter score: "))
    result = determine_score_status(score)
    print(result)

    # Generate and evaluate a random score
    random_score = random.uniform(0, 100)
    random_result = determine_score_status(random_score)
    print(f"\nRandom score: {random_score:.2f}")
    print(random_result)

main()