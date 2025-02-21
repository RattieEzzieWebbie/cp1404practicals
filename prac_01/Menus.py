"""
CP1404/CP5632 - Practical 01
Menu Program
"""

# Get user's name
name = input("Enter name: ")


# Display menu options
def display_menu():
    print("(H)ello")
    print("(G)oodbye")
    print("(Q)uit")


# Display menu and get initial choice
display_menu()
choice = input(">>> ").upper()

# Process menu choices
while choice != "Q":
    if choice == "H":
        print(f"Hello {name}")
    elif choice == "G":
        print(f"Goodbye {name}")
    else:
        print("Invalid choice")

    display_menu()
    choice = input(">>> ").upper()

print("Finished.")
