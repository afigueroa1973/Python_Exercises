# Exercise 2.12 (Hourly Wage Calculator):

""" Every year, if an employee receives a good job performance review, they get
    a raise of 3% on their wages. In turn, if they receive a suboptimal
    performance review, their wages are deducted by 3%. Consider an employee
    starting with an hourly wage of $10. Calculate how much this employee is
    earning after 5 years of consistent good reviews and after 2 years of bad
    reviews. Use the following formula to calculate these wages:
    w = o(1 + p)n
    where:
    w is the new hourly wage,
    o is the original hourly wage,
    p is the percentage increase or decrease, and
    n is the number of years with an increase or decrease in hourly wage."""

original_wage = 10
y_good_reviews = 5
y_bad_reviews = 2
percentage_increase = 0.03
percentage_decrease = -0.03

wage_increase = original_wage * (1 + percentage_increase) ** y_good_reviews
wage_decrease = wage_increase * (1 + percentage_decrease) ** y_bad_reviews

actual_wage = wage_decrease

print("\nActual Hourly Wage: ", actual_wage)
