class Auto:
    color = "Rojo"
    puertas = 4

    def arrancar(self):
        print("Estoy arrancando.")

miAuto = Auto()
print(miAuto.color)
print(miAuto.puertas)

miAuto.arrancar()

class Person:
    #id_person = int
    #name = str

    def __init__(self, id_person, name, age):
        self.id_person = id_person
        self.name = name
        self.age = age

    def es_mayor_de_edad(self):
        if (self.age >= 18):
            print(f"{self.name} es mayor de edad.")
        else:
            print(f"{self.name} es menor de edad.")

    def to_string(self):
        print(f"Person -> id ={self.id_person}, name = {self.name}")


if __name__ == "__main__":

    people = []

    option = input("Deseas agregar a la persona [SI o NO] ")

    while option == "SI":

        idPerson = int(input("Ingresar identificador: "))
        namePerson = input("Ingresar nombre: ")
        agePerson = int(input("Ingresar la edad: "))

        person = Person(idPerson, namePerson, agePerson)
        person.es_mayor_de_edad()
        person.to_string()

        people.append(person)

        option = input("Deseas agregar a otra persona [SI o NO] ")

    print(len(people))

exit(0)