# Imprimir los numeros enteros menores a 10

numero = 0

while numero < 10:

    numero = numero + 1

    if numero % 2 == 0:
        continue

    print(numero)

print(f'El numero final es {numero}.')