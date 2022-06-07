# Day 3 Exercise 0, Roller Coaster:

""" Write a program that tell us if we can ride in the Roller Coaster and print
    the bill. Use these statements:

    - Minimum height: 120 cm
    - Price tickets for age <= 12 years: $5
    - Price tickets for age <= 18 years: $7
    - Price tickets for age > 18 years: $12
    - Price tickets for people with "midlife crisis" with ages between 45 and
    55, inclusive: $0
    - Price for photo: $3"""

print("\nWelcome To The Roller Coaster!")
height = int(input("What is your height in centimeters?: "))
bill = 0

if height >= 120:
    print("You can ride the roller coaster!")
    age = int(input("What is your age?: "))
    if age <= 12:
        bill = 5
        print("Child tickets are $5")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7")
    elif 45 <= age <= 55:
        bill = 0
        print("Everything is going to be OK. Have a free ride on us!")
    else:
        bill = 12
        print("Adult tickets are $12")

    wants_photo = input("Do you want a photo taken? Please enter Y or N: ")
    if wants_photo == "Y":
        # Add $3 to their bill
        bill += 3
    print(f"Your final bill is ${bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")
