# Assignment 5.2:

""" Write a program that repeatedly prompts a user for integer numbers until
    the user enters 'done'. Once 'done' is entered, print out the largest and
    smallest of the numbers. If the user enters anything other than a valid
    number catch it with a try/except and put out an appropriate message and
    ignore the number.
    Enter 7, 2, bob, 10, and 4 and match the output below.
"""

smallest = None
largest = None

while True:
    numString = input('\nEnter a number: ')
    if numString.lower() == 'done':
        break
    try:
        numInt = int(numString)
        if smallest is None:
            smallest = numInt
        elif numInt < smallest:
            smallest = numInt
        if largest is None:
            largest = numInt
        elif numInt > largest:
            largest = numInt
    except ValueError:
        print("Invalid input")

print("Maximum is", largest)
print("Minimum is", smallest)

# Desired Outputs:
# Invalid input
# Maximum is 10
# Minimum is 2
