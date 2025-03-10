"""""
CP1404/CP5632 Practical
State names in a dictionary
"""

CODE_TO_NAME = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria",
    "TAS": "Tasmania",
    "SA": "South Australia"
}

# Print all state abbreviations and their names
for state_code, state_name in CODE_TO_NAME.items():
    print(f"{state_code:<3} is {state_name}")

state_code = input("Enter short state: ").strip().upper()
while state_code:
    try:
        print(f"{state_code} is {CODE_TO_NAME[state_code]}")
    except KeyError:
        print("Invalid short state")
    state_code = input("Enter short state: ").strip().upper()
