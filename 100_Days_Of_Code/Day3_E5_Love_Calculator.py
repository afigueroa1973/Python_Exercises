# Day 3 Exercise 5, Love Calculator:

""" You are going to write a program that tests the compatibility between two
    people. To work out the love score between two people:

    Take both people's names and check for the number of times the letters in
    the word TRUE occurs. Then check for the number of times the letters in the
    word LOVE occurs. Then combine these numbers to make a two digits number.

    -For Love Scores less than 10 or greater than 90, the message should be:
        Your score is **x**, you go together like coke and mentos.

    - For Love Scores between 40 and 50, the message should be:
        Your score is **y**, you are alright together.

    - Otherwise, the message will just be their score. e.g.:
        Your score is **z**..."""

print("\nWelcome To The Love Calculator!")
name1 = input("What is your first and last name? \n")
name2 = input("What is their first and last name? \n")

name1_lower = name1.lower()
name2_lower = name2.lower()

T = name1_lower.count("t") + name2_lower.count("t")
r = name1_lower.count("r") + name2_lower.count("r")
u = name1_lower.count("u") + name2_lower.count("u")
e = name1_lower.count("e") + name2_lower.count("e")

sum_true = T + r + u + e

L = name1_lower.count("l") + name2_lower.count("l")
o = name1_lower.count("o") + name2_lower.count("o")
v = name1_lower.count("v") + name2_lower.count("v")
e = name1_lower.count("e") + name2_lower.count("e")

sum_love = L + o + v + e

love_score = int(str(sum_true) + str(sum_love))

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif 40 <= love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
