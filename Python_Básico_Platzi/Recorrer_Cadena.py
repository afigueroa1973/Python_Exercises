# Recorrer Cadena:

"""
    Elabore un programa que permita recorrer una cadena y separe cada letra
    con un espacio.
"""


def main():
    palabra = input("\nFavor introduzca una palabra o frase: ")

    for i in palabra:
        print(i.upper(), end="  ")


if __name__ == "__main__":
    main()
