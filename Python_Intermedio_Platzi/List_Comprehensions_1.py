# List Comprehensions:

""" Write a program that print the square numbers for all numbers between 1 and
    100 that are not divisible by 3."""


def main():
    # The traditional way to do it:
    # square_numbers = []
    # for i in range(1, 101):
    #     if i % 3 != 0:
    #         square_numbers.append(i ** 2)

    square_numbers = [i ** 2 for i in range(1, 101) if i % 3 != 0]

    print(square_numbers)


if __name__ == '__main__':
    main()
