# Day 4 Exercise 1, Heads or Tails:

""" You are going to write a virtual coin toss program. It will randomly tell
    the user "Heads" or "Tails". When you run the code, just use a random
    number as the seed. e.g. 67346...It doesn't matter what you chose, it's
    only for our testing code to check your work. There are many ways of doing
    this. But to practice what we learnt in the last lesson, you should
    generate a random number, either 0 or 1. Then use that number to print out
    Heads or Tails, e.g. 1 means Heads, 0 means Tails.

    We use random.seed() to implement a random number based process where it is
    necessary to be able to reproduce the results...No matter how many times we
    use the random number, once it is created and as long as the seed is the
    same, the generated random number will remain the same."""

import random

test_seed = int(input("\nCreate a seed number: "))
random.seed(test_seed)

random_integer = random.randint(0, 1)

if random_integer == 1:
    print("Heads")
else:
    print("Tails")

print(random_integer)
random.seed()
