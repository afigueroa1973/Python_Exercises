# Exercise 2.14 (Target Heart-Rate Calculator):

""" While exercising, you can use a heart-rate monitor to see that your heart
    rate stays within a safe range suggested by your doctors and trainers.
    According to the American Heart Association (AHA). The formula for
    calculating your maximum heart rate in beats per minute is 220 minus your
    age in years. Your target heart rate is 50–85% of your maximum heart rate.
    Write a script that prompts for and inputs the user’s age and calculates
    and displays the user’s maximum heart rate and the range of the user’s
    target heart rate. [These formulas are estimates provided by the AHA;
    maximum and target heart rates may vary based on the health, fitness and
    gender of the individual. Always consult a physician or qualified
    healthcare professional before beginning or modifying an exercise program.]
"""

age = int(input("\nPlease, enter your age: "))

max_heart_rate = 220 - age  # In beats per minute, ppm

low_target_hr = 0.5 * max_heart_rate
high_target_hr = 0.85 * max_heart_rate

print("\nMaximun Heart Rate: ", max_heart_rate)
print("Range of User's Target Rate: ", low_target_hr, "-", high_target_hr)
