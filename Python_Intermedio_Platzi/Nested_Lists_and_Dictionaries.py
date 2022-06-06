# Nested List and Dictionaries:

""" Write a program that shows how work nested dictionaries in lists and vice
    versa."""


def main():
    super_list = [
        {"firstname": "Eduardo", "lastname": "Figueroa"},
        {"firstname": "Daniel", "lastname": "Figueroa"}
    ]

    super_dict = {
        "positive_nums": [1, 2, 3, 4, 5],
        "negative_nums": [-1, -2, -3, -5],
        "floating_nums": [1.1, 4.5, 6.43]
    }

    print()
    for key, value in super_dict.items():
        print(key, ":", value)

    print()
    for values in super_list:
        for key, value in values.items():
            print(f'{key}: {value}')


if __name__ == "__main__":
    main()
