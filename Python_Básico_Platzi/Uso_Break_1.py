# Uso de Break:

""" Elabore un programa que imprima los números pares en un rango de 0 a 100
    utilizando break para detener el programa al llegar al número 50...
"""


def main():
    for i in range(101):
        print(i)
        if i == 50:
            break


if __name__ == "__main__":
    main()
