# Day 5 Exercise 2, High Score:

""" You are going to write a program that calculates the highest score from a
    List of scores. e.g. student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

    Important you are not allowed to use the max or min functions. The output
    words must match the example. i.e - The highest score in the class is: x

    Example Input:
    78 65 89 86 55 91 64 89
    Example Output:
    The highest score in the class is: 91"""

score = input("\nInput a list of student scores ")
score_list = score.split()

max_score = 0

for score in score_list:
    score = int(score)

    if max_score < score:
        max_score = score

print(f"The highest score in the class is: {max_score}")