class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.lista_digipymon = []
        self.cantidad_digipymon = 0
        self.digicoins = 10

    def añadir_digipymon(self, digipymon):
        self.lista_digipymon.append(digipymon)
        self.cantidad_digipymon = self.cantidad_digipymon + 1
        return digipymon

    def consultar_digipymon(self):
        if not self.lista_digipymon:
            print("No tienes digipymons.")
        else:
            print("Tus digipymons son:")
            for digipymon in self.lista_digipymon:
                print(digipymon) 
        

    def mostrar_digicoins(self):
        print("Tienes " + str(self.digicoins) + " digicoins")
