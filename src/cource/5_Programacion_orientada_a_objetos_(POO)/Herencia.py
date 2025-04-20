class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def sonido(self):
        return "Hace algún sonido"

# La clase Perro hereda de Animal
class Perro(Animal):
    def sonido(self):
        return "Ladra"

class Gato(Animal):
    def sonido(self):
        return super().sonido() + " pero maúlla"

# Creando instancias
animal = Animal("Animal genérico")
perro = Perro("Firulais")
gato = Gato("Mishi")

print(animal.sonido())  # Hace algún sonido
print(perro.sonido())   # Ladra
print(gato.sonido())  # Hace algún sonido pero maúlla

exit(0)