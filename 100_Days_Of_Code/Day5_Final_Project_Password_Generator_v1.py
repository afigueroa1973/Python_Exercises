# Day 5 Final Project, Password Generator v1:

""" Password generator project v1, without changing the order of the letters"""

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

letters_in_pass = ""
symbols_in_pass = ""
numbers_in_pass = ""

print("\nHere is your password: ", end='')

for letter in range(0, len(letters) - 1):
    letters_in_pass = random.sample(letters, n_letters)
print(*letters_in_pass, sep='', end='')

for symbol in range(0, len(symbols) - 1):
    symbols_in_pass = random.sample(symbols, n_symbols)
print(*symbols_in_pass, sep='', end='')

for number in range(0, len(numbers) - 1):
    numbers_in_pass = random.sample(numbers, n_numbers)
print(*numbers_in_pass, sep='', end='')
