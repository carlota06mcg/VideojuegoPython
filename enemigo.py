class Enemigo:
    def __init__(self, nombre, lista_digipymons = [], cantidad_digipymon = 0):
        self.nombre = nombre
        self.lista_digipymons = lista_digipymons
        self.cantidad_digipymon = cantidad_digipymon


    def añadir_digipymon(self, digipymon):
        self.lista_digipymons.append(digipymon)
        self.cantidad_digipymon = self.cantidad_digipymon = 1 