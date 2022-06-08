# Exercise 2.5 (Eggs per Box):

""" Typically 6 eggs fit in one box. Write a script to calculate the number of
    boxes a farmer needs to store 28 eggs. The script will also determine how
    many eggs are placed in the last uncompleted box, and how many additional
    eggs are needed to fill this last box."""

box = 6
eggs = 28

last_box = eggs % box
eggs_to_fill = box - last_box

print(f"\nEggs in the las uncompleted box: {last_box}")
print(f"Eggs needed to fill the last box: {eggs_to_fill}")
