class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.lista_digipymon = []
        self.cantidad_digipymon = 0
        self.digicoins = 10

    def añadir_digipymon(self, nombre):
        self.lista_digipymon.append(nombre)
        self.cantidad_digipymon += 1
        return nombre

    def consultar_digipymon(self, nombre):
       print("Tu digipymon se llama " + self.lista_digipymon)

    def mostrar_digicoins(self):
        print("Tienes " + str(self.digicoins) + " digicoins")
                 