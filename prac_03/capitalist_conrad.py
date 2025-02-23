""""
CP1404/CP5632 - Practical
Capitalist Conrad
"""

import random

# Constants
MAX_INCREASE = 0.175  # 17.5%
MAX_DECREASE = 0.05   # 5%
MIN_PRICE = 1.00
MAX_PRICE = 100.00
INITIAL_PRICE = 10.00

# Starting price
price = INITIAL_PRICE
number_of_days = 0  # Variable to count days

# Print the starting price
print(f"Starting price: ${price:,.2f}")

# Simulate price changes until the price is out of the valid range
while MIN_PRICE <= price <= MAX_PRICE:
    number_of_days += 1  # Increment the day count
    price_change = 0

    # Randomly determine if the price will increase or decrease
    if random.randint(1, 2) == 1:
        # Increase the price by a random value between 0 and MAX_INCREASE
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        # Decrease the price by a random value between -MAX_DECREASE and 0
        price_change = random.uniform(-MAX_DECREASE, 0)

    price *= (1 + price_change)

    # Print the price for the day to the console
    print(f"On day {number_of_days} price is: ${price:,.2f}")