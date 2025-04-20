personas = ["Luis", "Pedro", "Lucia", "Maria", "Elena", "Juan"]

print(type(personas))

print(personas[0])
print(personas[1])
print(personas[-2])

#Ordenar lista
personas.sort()
print(personas)

#Ordenar lista a la inversa
personas.reverse()
print(personas)

#Listar cantidad de items de la lista
print(len(personas))

#Elimina el primer valor de la lista
personas.pop(0)
print(personas)

#Elimina el valor con el nombre Maria
personas.remove("Maria")
print(personas)

#Inserta un valor al final de la lista
personas.append("Enrique")
print(personas)

#Inserta un valor en la posicion que se le indica
personas.insert(0, "Angie")
print(personas)

personas2 = ["Julia", "Anthony"]
print(personas2)

#Inserla la lista(valores) en otra lista
personas.extend(personas2)
print(personas)

#Elimina todos los valores de la lista
personas.clear()
print(personas)

numeros = [10, 20, 30, 40, 50]
numeros.reverse()
print(numeros)
print(len(numeros))
print(max(numeros))
print(min(numeros))
print(sum(numeros))

exit(0)