"""
CP1404/CP5632 - Practical 03
Capitalist Conrad wants a stock price simulator for a volatile stock.
"""

import random

MAX_INCREASE = 0.175  # 17.5%
MAX_DECREASE = 0.05   # 5%
MIN_PRICE = 1.0
MAX_PRICE = 100.0
INITIAL_PRICE = 10.0
FILENAME = "output.txt"

price = INITIAL_PRICE
number_of_days = 0

out_file = open(FILENAME, 'w')

print(f"Starting price: ${price:,.2f}", file=out_file)

while MIN_PRICE <= price <= MAX_PRICE:
    number_of_days += 1
    price_change = 0

    if random.randint(1, 2) == 1:
        # Price increases
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        # Price decreases
        price_change = random.uniform(-MAX_DECREASE, 0)

    price *= (1 + price_change)
    print(f"On day {number_of_days} price is: ${price:,.2f}", file=out_file)

out_file.close()