# Day 4 Exercise 1, Banker Roulette:

""" You are going to write a program that will select a random name from a list
    of names. The person selected will have to pay for everybody's food bill.
    Important: You are not allowed to use the choice() function. Splits the
    string "names_string" into individual names and puts them inside a list
    called "names". For this to work, you must enter all the names as names
    followed by comma then space, e.g. name, name, name

    When you run the code, just use a random number as the seed. e.g. 112211 it
    doesn't matter what you chose, it's only for our testing code to check your
    work.

    Example Input:
    Andy, Maria, Jesus, Pablo, David
    Note: notice that there is a space between the comma and the next name.

    Example Output:
    Jesus is going to buy the meal today!"""

import random

test_seed = int(input("\nCreate a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma: ")
names = names_string.split(", ")  # Removes the comma and space and separate
# all the other elements in the "string_names"

# Counts elements in the list
names_count = len(names)
# Gets the final element in random function
stop_element = names_count - 1
# Gets a random number from the list of names
random_number = random.randint(0, stop_element)

# From the random number, extract the element choice
random_name = names[random_number]

print(f"\n{random_name} is going to buy the meal today!")

# The choice() function extract a random element from the list, so, this code
# could be done like this:
#   random_name = random.choice(names)
