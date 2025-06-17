"""
CP1404/CP5632 - Practical
Password Check Program with Functions
"""

def main():
    min_length = 8  # Set minimum password length
    password = get_password(min_length)
    print_asterisks(password)


def get_password(min_length):
    """Prompt user for a password of at least min_length characters."""
    while True:
        password = input("Enter password: ")
        if len(password) >= min_length:
            return password
        print("Error: Password too short. Try again.")


def print_asterisks(password):
    """Print asterisks equal to the length of the password."""
    print("*" * len(password))


if __name__ == "__main__":
    main()