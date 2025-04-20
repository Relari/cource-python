def evaluar_opcion(opcion):
    match opcion:
        case 1:
            return "Elegiste la opción 1"
        case 2:
            return "Elegiste la opción 2"
        case 3:
            return "Elegiste la opción 3"
        case _:
            return "Opción no válida"

print(evaluar_opcion(2))
print(evaluar_opcion(5))

exit(0)