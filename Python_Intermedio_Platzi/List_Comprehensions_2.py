# List Comprehensions:

""" Write a program that print all numbers that are multiple of 4, 6 and 9 till
    5 digits."""


def main():
    # list_numbers = [i for i in range(1, 100000) if i % 4 == 0 and i % 6 == 0
    #                   and i % 9 == 0]

    # Another way is using the least common multiple (LCM) of 4, 6 y 9 that
    # is 36:
    list_numbers = [i for i in range(1, 100000) if i % 36 == 0]
    print(list_numbers)


if __name__ == '__main__':
    main()
