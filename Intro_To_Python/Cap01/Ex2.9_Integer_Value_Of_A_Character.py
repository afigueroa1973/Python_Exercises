# Exercise 2.9 (Integer value of a character):

""" In this chapter, you learned about strings. Each of a string’s characters
    has an integer representation. The set of characters a computer uses
    together with the characters’ integer representations is called that
    computer’s character set. You can indicate a character value in a program
    by enclosing that character in quotes, as in "A" To determine a character’s
    integer value, call the built-in function ord. Tom and Jim want to play a
    game but are unable to choose who goes first. They decide that the person
    with the highest sum of the integer values of the characters of their name
    gets to play first. Write a script to determine who goes first."""

tom = ord("T") + ord("o") + ord("m")
jim = ord("J") + ord("i") + ord("m")

print("\nTom's value:", tom)
print("Jim's value:", jim)

highest = max(tom, jim)

if highest == tom:
    print("Tom goes first")
else:
    print("Jim goes first")
