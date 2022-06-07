# Day 5 Final Project, Password Generator v2:

""" Password generator project v2, without changing the order of the letters"""

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '-', '^', '~', '_']

print("Welcome To The PyPassword Generator!\n")
n_letters = int(input("How many letters would you like in your password?: "))
n_symbols = int(input(f"How many symbols would you like?: "))
n_numbers = int(input(f"How many numbers would you like?: "))

password = ""

for letter in range(0, n_letters):
    password += random.choice(letters)

for symbol in range(0, n_symbols):
    password += random.choice(symbols)

for number in range(0, n_numbers):
    password += random.choice(numbers)

print(f"\nHere is your password: {password}")
