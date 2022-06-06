# Palindrome:

""" Write a program that tell us if a word or phrase is a palindrome.
    Examples:
        civic
        no lemon no melon."""


palindrome = lambda string: string.replace(" ", "").lower() == \
                            string[::-1].replace(" ", "").lower()

print(palindrome)


def main():
    string = input("\nPlease, enter a string: ")
    is_palindrome = palindrome(string)
    if is_palindrome:
        print("It's a palindrome")
    else:
        print("It's not a palindrome")


if __name__ == "__main__":
    main()
