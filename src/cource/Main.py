class Person:
    id_person = int
    name = str

    def __init__(self, id_person, name):
        self.id_person = id_person
        self.name = name

    def print(self):
        print("Person ->", "id =", self.id_person, "name =", self.name)


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
