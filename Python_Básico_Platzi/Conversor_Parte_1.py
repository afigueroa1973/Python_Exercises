# Conversor de monedas:

""" Conversor de moneda que convierte pesos mexicanos, argentinos y colombianos
    a dólares, utilizar solamente condicionales if-elif-else."""

menu = """
Bienvenido Al Conversor de Monedas Multi País

1- Pesos Mexicanos
2- Pesos Colombianos
3- Pesos Argentinos

Elige una opción: """

opcion = int(input(menu))

if opcion == 1:  # pesos mexicanos
    pesos = input('¿Cuántos pesos mexicanos tienes?: ')
    pesos = float(pesos)
    tipo_de_cambio = 24
    dolares = pesos / tipo_de_cambio
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares+ " dólares")
elif opcion == 2:  # pesos colombianos
    pesos = input('¿Cuántos pesos colombianos tienes?: ')
    pesos = float(pesos)
    tipo_de_cambio = 3875
    dolares = pesos / tipo_de_cambio
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares+ " dólares")
elif opcion == 3:  # pesos argentinos
    pesos = input('¿Cuántos pesos argentinos tienes?: ')
    pesos = float(pesos)
    tipo_de_cambio = 65
    dolares = pesos / tipo_de_cambio
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares+ " dólares")
else:
    print('Favor ingresa una opción correcta: ')
