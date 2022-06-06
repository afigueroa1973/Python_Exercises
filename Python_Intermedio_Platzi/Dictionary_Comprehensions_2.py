# Dictionary Comprehensions:

""" Write a program that print the numbers between 1 and 100 raised to the
    power of 3 if number is not divisible by 3."""


def main():
    # Traditional way to do it:
    # list_numbers = {}
    # for i in range(1, 101):
    #     if i % 3 != 0:
    #         list_numbers[i] = i ** 3

    list_numbers = {i: i ** 3 for i in range(1, 101) if i % 3 != 0}

    print("\n", list_numbers)


if __name__ == '__main__':
    main()
