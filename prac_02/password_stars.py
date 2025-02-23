def get_password(min_length):
    while True:
        password = input("Enter password: ")
        if len(password) >= min_length:
            return password
        print("Error: Password too short. Try again.")

def print_asterisks(password):
    print("*" * len(password))

def main():
    min_length = 8  # Set minimum password length
    password = get_password(min_length)
    print_asterisks(password)

if __name__ == "__main__":
    main()
