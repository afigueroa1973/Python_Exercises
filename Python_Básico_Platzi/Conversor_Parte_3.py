# Conversor de monedas:

""" Conversor de moneda que convierte pesos mexicanos, argentinos y colombianos
    a dólares, utilizar condicionales if - elif - else, funciones y f-string.
"""


def conversor(tipo_pesos, cambio_dolar):
    pesos = input(f"¿Cuántos pesos {tipo_pesos} tienes?: ")
    pesos = float(pesos)
    dolares = pesos / cambio_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print(f"Tienes ${dolares} dólares")


opcion = int(input("""
Bienvenido al conversor de monedas 💰
1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opción: """))

if opcion == 1:
    conversor("colombianos", 3875)
elif opcion == 2:
    conversor("argentinos", 65)
elif opcion == 3:
    conversor("mexicanos", 24)
else:
    print('Ingresa una opción correcta por favor')
