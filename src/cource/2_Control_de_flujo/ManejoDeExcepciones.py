try:
    numero = int(input("Ingresa un número: "))
    print("El doble del número es:", numero * 2)
except ValueError:
    print("Error: Debes ingresar un número válido.")

try:
    lista = [1, 2, 3]
    print(lista[5])  # Intentando acceder a un índice inexistente
except IndexError:
    print("Error: Índice fuera de rango.")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")

try:
    resultado = 10 / 2
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero.")
else:
    print("La operación fue exitosa:", resultado)
finally:
    print("Fin del programa.")

exit(0)