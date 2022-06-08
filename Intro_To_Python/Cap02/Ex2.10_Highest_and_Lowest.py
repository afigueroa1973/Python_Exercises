# Exercise 2.10 (Arithmetic, Highest and Lowest):

""" Write a script that inputs the grades (in integers) of 3 courses from the
    user. First display the average grade of the three courses, and then the
    names and the grades of the courses with the highest and the lowest grades.
    """

grade1 = int(input("\nPlease, enter grade 1: "))
grade2 = int(input("Please, enter grade 2: "))
grade3 = int(input("Please, enter grade 3: "))

average = (grade1 + grade2 + grade3) / 3
print("\nAverage: ", average)

if grade1 > grade2 > grade3:
    print("Highest:", grade1, "for Grade 1")
    print("Lowest:", grade3, "for Grade 3")

if grade1 > grade3 > grade2:
    print("Highest:", grade1, "for Grade 1")
    print("Lowest:", grade2, "for Grade 2")

if grade2 > grade1 > grade3:
    print("Highest:", grade2, "for Grade 2")
    print("Lowest:", grade3, "for Grade 3")

if grade2 > grade3 > grade1:
    print("Highest:", grade2, "for Grade 2")
    print("Lowest:", grade1, "for Grade 1")

if grade3 > grade1 > grade2:
    print("Highest:", grade3, "for Grade 3")
    print("Lowest:", grade2, "for Grade 2")

if grade3 > grade2 > grade1:
    print("Highest:", grade3, "for Grade 3")
    print("Lowest:", grade1, "for Grade 1")
