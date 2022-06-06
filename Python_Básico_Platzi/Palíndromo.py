# Palíndromo:

"""
    Elabore un programa que nos diga si una palabra o frase es de tipo
    palindromo; ejemplos:
    ana
    yo dono rosas, oro no doy"""


def palindromo(palabra):
    palabra = palabra.replace(" ", "")
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]

    if palabra == palabra_invertida:
        return True
    else:
        return False


def main():
    palabra = input("\nFavor introduzca la palabra o frase: ")
    es_palindromo = palindromo(palabra)
    if es_palindromo:
        print("Es palíndromo")
    else:
        print("No es palíndromo")


if __name__ == "__main__":
    main()
