# Day 8 Exercise 1, Print Area Calculator:

""" You are painting a wall. The instructions on the paint can say that one can
    of paint can cover 5 square meters of wall. Given a random height and width
    of wall, calculate how many cans of paint you'll need to buy.

    number of cans = (wall height x wall width) ÷ coverage per can.
    e.g. Height = 2, Width = 4, Coverage = 5
    number of cans = (2 x️ 4) ÷ 5 = 1.6

    But because you can't buy 0.6 of a can of paint, the result should be
    rounded up to 2 cans."""

import math
# Important note:
# "from math import ceil" -- We can use this instead of "import math" and then
# eliminate math before ceil.


def paint_calc(height, width, cover):
    number_of_cans = math.ceil((height * width) / cover)
    print(f"You'll need {number_of_cans} cans of paint.")


input_height = int(input("Height of wall: "))
input_weight = int(input("Width of wall: "))
coverage = 5

paint_calc(height=input_height, width=input_weight, cover=coverage)
