class Person:
    idPerson = int
    name = str

    def __init__(self, idPerson, name):
        self.idPerson = idPerson
        self.name = name

    def print(self):
        print("Person ->", "id =", self.idPerson, "name =", self.name)


if __name__ == "__main__":

    people = []

    option = input("Deseas agregar a la persona [SI o NO] ")

    while option == "SI":

        idPerson = input("Ingresar identificador: ")
        namePerson = input("Ingresar nombre: ")

        person = Person(idPerson, namePerson)

        people.append(person)

        option = input("Deseas agregar a otra persona [SI o NO] ")

    print(len(people))

    for person in people:
        person.print()
