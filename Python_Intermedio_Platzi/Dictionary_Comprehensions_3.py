# Dictionary Comprehensions:

""" Write a program that print the square root of the numbers between 1 and
    100."""


def main():
    list_numbers = {i: i ** 0.5 for i in range(1, 101)}

    print("\n", list_numbers)


if __name__ == '__main__':
    main()
