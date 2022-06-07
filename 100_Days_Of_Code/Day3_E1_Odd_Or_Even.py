# Day 3 Exercise 1, Odd or Even:

""" Write a program that works out whether if a given number is an odd or even
    number."""

number = int(input("\nWhich number do you want to check?: "))

if number % 2 == 0:
    print("This is an even number")
else:
    print("This is an odd number")
