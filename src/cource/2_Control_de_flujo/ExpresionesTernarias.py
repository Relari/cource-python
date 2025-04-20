edad = 18
mensaje = "Eres mayor de edad" if edad >= 18 else "Eres menor de edad"
print(mensaje)  # Eres mayor de edad

a, b = 10, 20
mayor = a if a > b else b
print("El número mayor es:", mayor)  # 20

lista = [1, 2, 3, 4, 5]
estado = "Lista vacía" if not lista else "Lista con elementos"
print(estado)  # Lista con elementos

lista2 = []
estado2 = "Lista vacía" if not lista2 else "Lista con elementos"
print(estado2)  # Lista con elementos

def es_par(numero):
    return "Par" if numero % 2 == 0 else "Impar"

print(es_par(2))  # Impar

exit(0)