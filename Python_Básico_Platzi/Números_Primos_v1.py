# Encontrar Números Primos:

"""
    Elabore un programa que permita decirnos si un número ingresado mediante
    teclado, es primo."""


def main():
    numero = int(input("\nFavor ingrese un número: "))

    contador = 0

    for i in range(2, numero + 1):
        if i == 1 or i == numero:
            continue

        if numero % i == 0:
            contador += 1

    if contador == 0 and numero > 1:
        print(f"El número {numero} es primo")
    else:
        print(f"El número {numero} no es primo")


if __name__ == "__main__":
    main()
