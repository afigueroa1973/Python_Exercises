# Uso de Continue:

"""
    Elabore un programa que imprima solamente los números pares en un rango
    de 0 a 20 utilizando continue para evitar los números impares."""


def main():
    for i in range(21):
        if i % 2 != 0:
            continue
        print(i)


if __name__ == "__main__":
    main()
