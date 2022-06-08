# Exercise 2.11 (Calculating Time) :

""" Write a script that inputs a number of seconds from the user. Calculate the
    number of hours, minutes, and remaining seconds. Print them separated by
    “ - ”. For example, if the user types 3750 seconds as input, the script
    should print:
        1 - 2 - 30
    Assume that the user enters a number of seconds that is higher than 3600.
    Use both the floor division and the remainder operation to calculate the
    number of hours, minutes, and seconds."""

qty_seconds = int(input("\nPlease, enter the number of seconds: "))

hours = qty_seconds // 3600
minutes = (qty_seconds % 3600) // 60
seconds = qty_seconds % 3600 - minutes * 60

print(hours, "-", minutes, "-", seconds)
