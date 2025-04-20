class Ave:
    def volar(self):
        return "Puede volar"

class Pinguino(Ave):
    def volar(self):
        return "No puede volar, pero nada muy bien"

def mostrar_vuelo(ave):
    print(ave.volar())

aguila = Ave()
pinguino = Pinguino()

mostrar_vuelo(aguila)   # Puede volar
mostrar_vuelo(pinguino) # No puede volar, pero nada muy bien

exit(0)