# Exercise 2.8 (Table With Number of Bacteria):

""" Starting with 200 bacterias, the growth in the number of bacteria after "n"
    hours is calculated as follows: B = 200 × 2n. Print the number of bacteria
    after 0, 5, 10, and 15 hours in table format as shown below. Use the tab
    escape sequence to achieve the two-column output.
    Hour    Number of Bacteria
       0    200
       5    6400
      10    204800
      15    6553600"""

print("\nHour     Number of Bacteria")
print("0 \t\t", 200 * 2 ** 0)
print("5 \t\t", 200 * 2 ** 5)
print("10 \t\t", 200 * 2 ** 10)
print("15 \t\t", 200 * 2 ** 15)
