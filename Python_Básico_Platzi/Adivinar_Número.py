# Adivinar Número:

""" Elabore un programa que permita al usuario adivinar un número generado al
    azar por Python y que se encuentre entre 1 y 100.
"""

import random


def main():
    numero_aleatorio = random.randint(1, 100)
    numero = int(input("\nElige un número entre 1 y 100: "))

    while numero != numero_aleatorio:
        if numero > numero_aleatorio:
            print("Número incorrecto, favor ingresa un número mas bajo")
        elif numero < numero_aleatorio:
            print("Número incorrecto, favor ingresa un número mas alto")

        numero = int(input("Elige un número entre 1 y 100: "))

    print("Acertaste, felicidades!!!")


if __name__ == "__main__":
    main()
