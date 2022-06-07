# Day 2 Exercise 2, BMI Calculator:

""" Write a program that calculates the Body Mass Index (BMI) from a user's
    weight and height. The BMI is a measure of some weight taking into account
    their height. e.g. If a tall person and a short person both weigh the same
    amount, the short person is usually more overweight. The BMI is calculated
    by dividing a person's weight (in kg) by the square of their height (in m):
        BMI = weight / height^2;
        Where weight is in kilograms and height is in meters."""

height = input("\nEnter your height in meters: ")
weight = input("Enter your weight in kilograms: ")

bmi = float(weight) / float(height)**2
print(int(bmi))
