# Day 4 Exercise 3, Treasure Map:

""" You are going to write a program that will mark a spot with an X, this is
    to try and simulate the coordinates on a real map.

    ['⬜️', '⬜️', '⬜️']
    ['⬜️', '⬜️', '⬜️']
    ['⬜️', '⬜️', '⬜️']

    Your job is to write a program that allows you to mark a square on the map
    using a two-digit system. The first digit is the vertical column number and
    the second digit is the horizontal row number. e.g.: 23

    1   2   3  Column
    ⬜️ ⬜️ ⬜️  row 1
    ⬜️ ⬜️ ⬜️  row 2
    ⬜️  X ⬜️  row 3"""

row1 = ["⬜", "⬜", "⬜"]
row2 = ["⬜", "⬜", "⬜"]
row3 = ["⬜", "⬜", "⬜"]

treasure_map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

position = input("\nWhere do you want to put the treasure?: ")
column = int(position[0])
row = int(position[1])

# treasure_map[row - 1][column - 1] = "x"

# Alternate Method 2
# ------------------
# selected_row = treasure_map[row - 1]
# selected_row[column - 1] = "x"

# Alternate Method 3
# ------------------
# if column == 1 and row == 1:
#     row1 = ["x", "⬜", "⬜"]
#
# if column == 2 and row == 1:
#     row1 = ["⬜", "x", "⬜"]
#
# if column == 3 and row == 1:
#     row1 = ["⬜", "⬜", "x"]
#
# if column == 1 and row == 2:
#     row2 = ["x", "⬜", "⬜"]
#
# if column == 2 and row == 2:
#     row2 = ["⬜", "x", "⬜"]
#
# if column == 3 and row == 2:
#     row2 = ["⬜", "⬜", "x"]
#
# if column == 1 and row == 3:
#     row3 = ["x", "⬜", "⬜"]
#
# if column == 2 and row == 3:
#     row3 = ["⬜", "x", "⬜"]
#
# if column == 3 and row == 3:
#     row3 = ["⬜", "⬜", "x"]
# ----------------------------

print(f"{row1}\n{row2}\n{row3}")
