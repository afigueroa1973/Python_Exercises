# Generador de Passwords:

"""
    Elabore un programa que pueda generar aleatoriamente un clave de acceso
    utilizando multiples letras y caracteres."""

import random


def generar_password():
    mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                  'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
                  'Y', 'Z']
    minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                  'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
                  'y', 'z', ]
    simbolos = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '-', '^', '~',
                '_']
    numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    caracteres = mayusculas + minusculas + simbolos + numeros
    password = []

    for i in range(12):
        caracter_aleatorio = random.choice(caracteres)
        password.append(caracter_aleatorio)

    password = ''.join(password)  # Convierte la lista a un String
    return password


def main():
    password = generar_password()
    print(f'\nLa contraseña es: {password}')


if __name__ == '__main__':
    main()
