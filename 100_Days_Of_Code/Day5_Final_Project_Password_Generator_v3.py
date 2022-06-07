# Day 5 Final Project, Password Generator v3:

""" Password Generator Project v3, changing the order of the letters"""

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

for letter in range(0, n_letters):
    letters_in_pass += random.choice(letters)

for symbol in range(0, n_symbols):
    symbols_in_pass += random.choice(symbols)

for number in range(0, n_numbers):
    numbers_in_pass += random.choice(numbers)

password = letters_in_pass + symbols_in_pass + numbers_in_pass

final_password = random.sample(password, len(password))
print("\nHere is your password: ", end='')
print(*final_password, sep='', end='')
