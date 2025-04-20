suma = 0
continuar = True

while continuar:

    input_usuario = input("Ingrese un numero ('exit' para terminar): ")

    if input_usuario == 'exit':
        continuar = False
    else:
        numero = int(input_usuario)
        suma = suma + numero
        print(f'La suma es {suma}')

exit(0)