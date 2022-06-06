# Conversor de monedas:

""" Conversor de moneda que convierte pesos mexicanos, argentinos y colombianos
    a dólares, utilizar condicionales if - elif - else y funciones.
"""


def conversor(tipo_pesos, cambio_dolar):
    pesos = input("¿Cuántos pesos " + tipo_pesos + " tienes?: ")
    pesos = float(pesos)
    dolares = pesos / cambio_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")


menu = """
Bienvenido al Conversor de Monedas 💰 Multi País

1- Pesos colombianos
2- Pesos argentinos
3- Pesos mexicanos

Elige una opción: """

opcion = int(input(menu))

if opcion == 1:
    conversor("colombianos", 3875)
elif opcion == 2:
    conversor("argentinos", 65)
elif opcion == 3:
    conversor("mexicanos", 24)
else:
    print('Ingresa una opción correcta por favor')
