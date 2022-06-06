# Potencia de un Número:

"""
    Elabore un programa que permita imprimir todas las potencias de un número
    menores de 100. Utilizar funciones para optimizar el programa junto con
    el ciclo For.
"""


def potencia(base):
    for potencia_numero in range(0, 101):
        pot = base ** potencia_numero
        if pot <= 1000:
            print(f"{base} ^ {potencia_numero} = {pot}")


def main():
    base = int(input("\nFavor introduzca la base: "))
    potencia(base)


if __name__ == "__main__":
    main()
