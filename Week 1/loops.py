# CP1404/CP5632 - Practical
# loops.py

# Display all odd numbers between 1 and 20
print("Odd numbers from 1 to 20:")
for i in range(1, 21, 2):
    print(i, end=' ')
print()  # Odd numbers from 1 to 20: 1 3 5 7 9 11 13 15 17 19

# a. Count in 10s from 0 to 100
print("a. Count in 10s from 0 to 100:")
for i in range(0, 101, 10):
    print(i, end=' ')
print()  # a. Count in 10s from 0 to 100: 0 10 20 30 40 50 60 70 80 90 100

# b. Count down from 20 to 1
print("b. Count down from 20 to 1:")
for i in range(20, 0, -1):
    print(i, end=' ')
print()  # b. Count down from 20 to 1: 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1

# c. Print n stars on one line
print("c. Print n stars on one line:")
n = int(input("Number of stars: "))  # Example input: 5
for i in range(n):
    print('*', end='')
print()  # Example output for n = 5: *****

# d. Print n lines of increasing stars
print("d. Print n lines of increasing stars:")
for i in range(1, n + 1):
    print('*' * i)  # Example output for n = 5:
# *
# **
# ***
# ****
# *****
