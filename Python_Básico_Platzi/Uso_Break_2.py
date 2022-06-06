# Uso de Break:

""" Elabore un programa que encuentre una letra determinada en una palabra o
    frase y luego de encontrarla, detenga la ejecución...
"""


def main():
    palabra = input("Favor ingrese una palabra o frase: ")
    for i in palabra:
        if i == "e":
            break
        print(i.upper(), end="  ")


if __name__ == "__main__":
    main()
