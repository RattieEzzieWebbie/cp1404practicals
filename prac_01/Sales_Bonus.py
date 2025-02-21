"""
CP1404/CP5632 - Practical 01
Program to calculate and display a user's bonus based on sales.
"""

# Get the number of items with input validation
num_items = int(input("Number of items: "))
while num_items < 0:
    print("Invalid number of items!")
    num_items = int(input("Number of items: "))

# Collect prices and calculate total
total_price = 0
for i in range(num_items):
    price = float(input("Price of item: "))
    total_price += price

# Apply discount if total is over $100
if total_price > 100:
    total_price *= 0.9  # Apply 10% discount

# Display total price
print(f"Total price for {num_items} items is ${total_price:.2f}")

