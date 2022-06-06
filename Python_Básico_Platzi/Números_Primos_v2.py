# Encontrar Números Primos:

"""
    Elabore un programa que permita decirnos si un número ingresado mediante
    teclado, es primo. Utilizar funciones para optimizar el programa."""


def es_primo(numero):
    contador = 0

    for i in range(2, numero + 1):
        if i == 1 or i == numero:
            continue

        if numero % i == 0:
            contador += 1

    if contador == 0 and numero > 1:
        return True
    else:
        return False


def main():
    numero = int(input("\nFavor ingrese un número: "))

    if es_primo(numero):
        print(f"El número {numero} es primo")
    else:
        print(f"El número {numero} no es primo")


if __name__ == "__main__":
    main()
