# Assignment 9.4:

""" Write a program to read through the mbox-short.txt and figure out who has
    sent the greatest number of mail messages. The program looks for 'From '
    lines and takes the second word of those lines as the person who sent the
    mail. The program creates a Python dictionary that maps the sender's mail
    address to a count of the number of times they appear in the file. After
    the dictionary is produced, the program reads through the dictionary using
    a maximum loop to find the most prolific committer. You can download the
    sample file at https://www.py4e.com/code3/mbox-short.txt"""

file_name = input("\nEnter file: ")
file_handle = open(file_name)

count = dict()
for line in file_handle:
    if not line.startswith("From "):
        continue
    line = line.split()
    line = line[1]
    count[line] = count.get(line, 0) + 1

bigcount = None
bigCommiter = None

for key, value in count.items():
    if bigcount is None or value > bigcount:
        bigCommiter = key
        bigcount = value

print(bigCommiter, bigcount)

# Desired Output:
# cwen@iupui.edu 5
