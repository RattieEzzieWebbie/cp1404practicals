def celsius_to_fahrenheit(celsius):
    return celsius * 9.0 / 5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def main():
    MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            print(f"Result: {celsius_to_fahrenheit(celsius):.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            print(f"Result: {fahrenheit_to_celsius(fahrenheit):.2f} C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")

if __name__ == "__main__":
    main()
