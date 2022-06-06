# Assignment 5.1:

""" Write a program which repeatedly reads numbers until the user enters
    “done”. Once “done” is entered, print out the total, count, and average of
    the numbers. If the user enters anything other than a number, detect their
    mistake using try and except and print an error message and skip to the
    next number."""

total = 0
count = 0

while True:
    numString = input('\nEnter a number: ')
    if numString.lower() == 'done':
        break

    try:
        numInt = int(numString)
        total += numInt
        count += 1

    except ValueError:
        print("Invalid input")

average = total / count
print("\nTotal: ", total, "\nCount:", count, "\nAverage:", average)
