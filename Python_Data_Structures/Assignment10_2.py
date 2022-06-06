# Assignment 10.2:

""" Write a program to read through the mbox-short.txt and figure out the
    distribution by hour of the day for each of the messages. You can pull the
    hour out from the 'From ' line by finding the time and then splitting the
    string a second time using a colon.
        From stephen.marquard@uct.ac.za Sat Jan  5 09: 14: 16 2008
    Once you have accumulated the counts for each hour, print out the counts,
    sorted by hour as shown below. You can download the sample file at:
    http:/www.py4e.com/code3/mbox-short.txt
"""

file_name = input("\nEnter file: ")
file_handle = open(file_name)

lst = list()
dictionary = dict()

for line in file_handle:
    if line.startswith("From "):
        pos = line.find(":")
        lst.append(line[pos-2:pos])

for word in lst:
    dictionary[word] = dictionary.get(word, 0) + 1
new_list = list()

for key, value in dictionary.items():
    new_dict = (key, value)
    new_list.append(new_dict)
new_list = sorted(new_list)

for key, value in new_list:
    print(key, value)

# Desired output
# 04 3
# 06 1
# 07 1
# 09 2
# 10 3
# 11 6
# 14 1
# 15 2
# 16 4
# 17 2
# 18 1
# 19 1
