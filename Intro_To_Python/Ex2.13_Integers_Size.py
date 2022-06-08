# Exercise 2.13 (How Big Can Python Integers Be?):

""" Use the exponentiation operator ** with large and very large exponents to
    produce some huge integers and assign those to the variable number to see
    if Python accepts them. Did you find any integer value that Python won’t
    accept?"""

# "int" in Python 3 is equivalent to "long" in Python 2, and there is no limit
# on the maximum value. You can handle as large value as memory is available.

integer = 3345344532234 ** 98351
print("\n", integer)
