# Potencia de un Número:

"""
    Elabore un programa que permita imprimir todas las potencias de un número
    menores de 100. Utilizar funciones para optimizar el programa junto con
    el ciclo While.
"""


def potencia(base):
    contador = 0
    potencia_numero = base ** contador

    while potencia_numero <= 1000:
        print(f"{base} ^ {contador} = {potencia_numero}")
        contador += 1
        potencia_numero = base ** contador


def main():
    base = int(input("\nFavor introduzca la base: "))
    potencia(base)


if __name__ == "__main__":
    main()
