numeros = [1, 2, 3, 4, 5, 6]
print(numeros)
doble = list(map(lambda x: x * 2, numeros))
print(doble)  # [2, 4, 6, 8, 10, 12]

def cuadrado(n):
    return n ** 2

resultado = list(map(cuadrado, numeros))
print(resultado)  # [1, 4, 9, 16, 25, 36]

pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # [2, 4, 6]

def es_par(n):
    return n % 2 == 0

pares = list(filter(es_par, numeros))
print(pares)  # [2, 4, 6]

from functools import reduce
suma_total = reduce(lambda x, y: x + y, numeros)
print(suma_total)  # 21

ordenados = sorted(numeros)  # Ordena en orden ascendente
print(ordenados)  # [1, 2, 5, 7, 9]

ordenados_desc = sorted(numeros, reverse=True)
print(ordenados_desc)  # [9, 7, 5, 2, 1]

personas = [{"nombre": "Ana", "edad": 25}, {"nombre": "Luis", "edad": 30}, {"nombre": "Carlos", "edad": 22}]
ordenados_por_edad = sorted(personas, key=lambda x: x["edad"])
print(ordenados_por_edad)

nombres = list(map(lambda persona: persona["nombre"], personas))
print(nombres)  # ['Ana', 'Luis', 'Carlos']

exit(0)