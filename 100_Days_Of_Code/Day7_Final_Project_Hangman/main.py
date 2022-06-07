# Day 7 Final Project, Hangman:

""" Write a program for the Hangman game."""

import random
from hangman_art import stages, logo
from hangman_words import word_list
from replit import clear

print(logo)

end_of_game = False
lives = len(stages) - 1

# Python selects one random word from the list
random_word = random.choice(word_list)

# We create a list with n elements, like n letters in the random word
word = []
for element in range(len(random_word)):
    word.append("_")

print(f"Guess the next word: {'_ ' * len(random_word)}")

# This variable records every letter that you chose
letter_check_list = []
while not end_of_game:
    chosen_letter = input("Guess a letter: ").lower()
    letter_check_list.append(chosen_letter)

    # Use the clear() function imported to clear the output between guesses
    clear()

    # Print every letter that you already chose before
    print(f"Letters used...{', '.join(letter_check_list)}")

    # This code avoid repeat letters
    if chosen_letter in word:
        print(f"You've already guessed {chosen_letter}")

    # If letter is found, replace that letter in every location where was found
    for element in range(len(random_word)):
        letter = random_word[element]
        if letter == chosen_letter:
            word[element] = chosen_letter

    print(f"{' '.join(word)}")

    if chosen_letter not in random_word:
        print(f"\nThat letter is not in the word... You lose a life")
        lives -= 1

        if lives == 0:
            end_of_game = True
            print(f"Sorry, you lose! The word was... {random_word}")

    if "_" not in word:
        end_of_game = True
        print(f"Congratulations, you guessed the word... {random_word}")

    print(stages[lives])
