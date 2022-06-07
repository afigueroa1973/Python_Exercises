# Day 3 Exercise 2, Leap Year:

""" Write a program that works out whether if a given year is a leap year. A
    normal year has 365 days, leap years have 366, with an extra day in
    February. This is how you work out whether if a particular year is a leap
    year:

    - On every year that is evenly divisible by 4
    - **except** every year that is evenly divisible by 100
    - **unless** the year is also evenly divisible by 400

    Example 1, Year 2000:
        2000 ÷ 4 = 500 (Leap)
        2000 ÷ 100 = 20 (Not Leap)
        2000 ÷ 400 = 5 (Leap!)
        So the year 2000 is a leap year.

    Example 2, Year 2100:
        2100 ÷ 4 = 525 (Leap)
        2100 ÷ 100 = 21 (Not Leap)
        2100 ÷ 400 = 5.25 (Not Leap)
        So, the year 2100 is not a leap year."""

year = int(input("\nWhich year do you want to check?: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not a leap year.")
    else:
        print("Leap year.")
else:
    print("Not a leap year.")
