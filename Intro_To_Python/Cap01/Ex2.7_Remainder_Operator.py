# Exercise 2.7 (The remainder operator):

""" Jonah wants to distribute 22 marbles among his four friends. All friends
    should receive an equal amount of marbles. Write a script that can
    determine if this is possible."""

marbles = 22
amount = marbles / 4

print("\nAmount:", amount)

if marbles % 4 == 0:
    print("It is possible")
else:
    print("It is not possible")
