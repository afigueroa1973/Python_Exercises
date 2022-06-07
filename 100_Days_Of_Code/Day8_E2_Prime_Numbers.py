# Day 8 Exercise2, Prime Number:

""" A prime number is a number that is only divisible by 1 and itself...You
    need to write a function that checks whether if the number passed into it
    is a prime number or not.
    e.g. 2 is a prime number because it's only divisible by 1 and 2; but 4 is
    not a prime number because you can divide it by 1, 2 or 4."""


def prime_checker(number):
    is_prime = True

    for i in range(2, number):
        if number % i == 0:
            is_prime = False

    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


n = int(input("Check this number: "))
prime_checker(number=n)
