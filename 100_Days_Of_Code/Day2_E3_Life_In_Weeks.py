# Day 2 Exercise 3, Life In Weeks:

""" Create a program using maths and f-Strings that tells us how many days,
    weeks, months we have left if we live until 90 years old. It will take
    your current age as the input and output a message with our time left in
    this format:

    You have x days, y weeks, and z months left. Where x, y and z are replaced
    with the actual calculated numbers."""

age = input("\nWhat is your current age?: ")

resting_life = 90 - int(age)
days = resting_life * 365
weeks = resting_life * 52
months = resting_life * 12

print(f"You have {days} days, {weeks} weeks and {months} months left.")
