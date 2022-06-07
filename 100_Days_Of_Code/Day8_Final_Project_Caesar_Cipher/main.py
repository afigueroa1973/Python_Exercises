# Day 8 Final Project, Caesar Cipher:

""" Write a program using the Caesar Cipher method. Go to Wikipedia for more
    information. https://en.wikipedia.org/wiki/Caesar_cipher"""

from Art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(plain_text, shift_amount, cipher_direction):
    final_text = ""

    if cipher_direction == "decode":
        shift_amount *= -1

    for char in plain_text:
        if char in alphabet:
            actual_position = alphabet.index(char)
            new_position = actual_position + shift_amount
            final_text += alphabet[new_position]
        else:
            final_text += char

    print(f"The {cipher_direction}d text is {final_text}")


print(logo)

should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt or 'decode' to decrypt: ")
    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))

    # Add some code so that the program continues to work even if the user
    # enters a shift number greater than 26.
    shift = shift % 26  # Because the english alphabet has 26 letters

    caesar(plain_text=text, shift_amount=shift, cipher_direction=direction)

    choice = input(
        "\nType 'yes' if you want to continue, otherwise type 'no': ")

    if choice == "no":
        should_continue = False
        print("\nIt's time to say... Goodbye")
