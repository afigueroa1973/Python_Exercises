# Day 2 Final Project, Tip Calculator:

""" Create a program tha calculate the tip for a bill...If the bill was$150.0,
    split between five people, with 12% tip. Each person should pay:
    (150.00 / 5) * 1.12 = 33.6
    Format the result to two decimal places = 33.60"""

print("\nWelcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
persons = int(input("How many people to split the bill? "))

bill += bill * tip / 100
bill_to_pay = bill / persons

print(f"Each person should pay: ${bill_to_pay:,.2f}")
