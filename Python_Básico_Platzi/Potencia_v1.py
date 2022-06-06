# Potencia de un Número:

"""
    Elabore un programa que permita imprimir todas las potencias de un número
    desde 0 a 100.
"""

base = int(input("\n¿De que número quier sacar la potencia?: "))

# Con bucle for...
for i in range(0, 101):
    potencia = base ** i
    print(f"{base} ^ {i} = {potencia}")

# Imprimir una linea divisoria entre ambos ciclos...
print("-----------------------------------------------")

# Con bucle while...
contador = 0

while contador <= 100:
    potencia = base ** contador
    print(f"{base} ^ {contador} = {potencia}")
    contador += 1
