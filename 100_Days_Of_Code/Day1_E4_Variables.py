# Day 1 Exercise 4, Variables:

""" Write a program that inputs two integers and then switches the values
    stored in the variables a and b; example:
    a: 1
    b: 2
    ----
    a: 2
    b: 1"""

print("\n   - SWITCH THE VALUE -   ")
print("--------------------------")

a = input("a: ")
b = input("b: ")

c = a
a = b
b = c

print("-----")
print("a: " + a)
print("b: " + b)
