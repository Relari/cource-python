
for i in "Numero":
    print(i)

nombres = ["Pepe","Juan", "Maria", "Ana"]
for nombre in nombres:
    print(nombre)

personas = [{"nombre": "Ana", "edad": 25}, {"nombre": "Luis", "edad": 30}, {"nombre": "Carlos", "edad": 22}]

for persona in personas:
    print(persona["nombre"])
    #print(persona.get("nombre"))


nombres = [persona["nombre"] for persona in personas]
print(nombres)  # ['Ana', 'Luis', 'Carlos']


exit(0)