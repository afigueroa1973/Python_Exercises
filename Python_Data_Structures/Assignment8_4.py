# Assignment 8.4:

""" Open the file romeo.txt and read line by line. For each line, split the
    line into a list of words using the split() method. The program should
    build a list of words. For each word on each line check to see if the word
    is already in the list and if not append it to the list. When the program
    completes, sort and print the resulting words in alphabetical order.
    You can download the sample file at https://www.py4e.com/code3/romeo.txt"""

file_name = input("\nEnter file name: ")
file_handle = open(file_name)
word_list = list()

for line in file_handle:
    line = line.rstrip()
    line = line.split()
    for word in line:
        if word not in word_list:
            word_list.append(word)

word_list.sort()
print(word_list)

# Desired Output:
# ['Arise', 'But', 'It', 'Juliet', 'Who', 'already', 'and', 'breaks', 'east',
# 'envious', 'fair', 'grief', 'is', 'kill', 'light', 'moon', 'pale', 'sick',
# 'soft', 'sun', 'the', 'through', 'what', 'window', 'with', 'yonder']
