# Assignment 7.1:

""" Write a program that prompt for a file name, then opens that file and
    reads through the file, and print the contents of the file in upper case.
    Use the file words.txt to produce the output desired.
    You can download the sample file at http:/www.py4e.com/code3/words.txt"""

file_name = input("\nEnter file name: ")
file_handle = open(file_name)

text = file_handle.read()
text_strip = text.rstrip()

print("\n" + text_strip.upper())
