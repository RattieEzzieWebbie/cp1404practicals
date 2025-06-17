"""
CP1404/CP5632 - Practical 01
Shop Calculator
"""

DISCOUNT_THRESHOLD = 100  # dollars
DISCOUNT_RATE = 0.10      # 10%

def main():
    """Calculate total price with discount for multiple items."""
    number_of_items = get_valid_item_count()
    total_price = 0

    for i in range(number_of_items):
        item_price = float(input("Price of item: "))
        total_price += item_price

    if total_price > DISCOUNT_THRESHOLD:
        total_price *= (1 - DISCOUNT_RATE)

    print(f"Total price for {number_of_items} items is ${total_price:.2f}")


def get_valid_item_count():
    """Prompt user for a valid number of items (0 or more)."""
    number_of_items = int(input("Number of items: "))
    while number_of_items < 0:
        print("Invalid number of items!")
        number_of_items = int(input("Number of items: "))
    return number_of_items


if __name__ == "__main__":
    main()