# Assignment 7.2:

""" Write a program that prompts for a file name, then opens that file and
    reads through the file, looking for lines of the form:
        X-DSPAM-Confidence: 0.8475

    Count these lines and extract the floating-point values from each of the
    lines and compute the average of those values and produce an output as
    shown below. Do not use the sum() function or a variable named sum in your
    solution. Use mbox-short.txt as the file name. You can download the sample
    file at https://www.py4e.com/code3/mbox-short.txt"""

total = 0
count = 0

file_name = input("\nEnter file name: ")
file_handle = open(file_name)

for line in file_handle:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count += 1
    position = line.find(":")
    value = float(line[position + 1:])
    total = total + value

average = total / count

print("Average spam confidence:", average)

# Output desired:
# Average spam confidence: 0.750718518519
