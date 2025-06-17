"""
CP1404/CP5632 - Practical 01
Menu Program
"""

def display_menu():
    """Display the menu options."""
    print("(H)ello")
    print("(G)oodbye")
    print("(Q)uit")

def main():
    """Run the menu program."""
    name = input("Enter name: ")
    display_menu()
    choice = input(">>> ").strip().upper()

    while choice != "Q":
        if choice == "H":
            print(f"Hello {name}")
        elif choice == "G":
            print(f"Goodbye {name}")
        else:
            print("Invalid choice")
        display_menu()
        choice = input(">>> ").strip().upper()

    print("Finished.")

# Call the main function to start the program
if __name__ == "__main__":
    main()
