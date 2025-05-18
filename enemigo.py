"""
    Clase "Enemigo".
"""
class Enemigo:
    """
    Función "__init__".
    Definimos los atributos de nombre, lista_digipymons = [], cantidad_digipymon = 0.
    """
    def __init__(self, nombre, lista_digipymons = [], cantidad_digipymon = 0):
        self.nombre = nombre
        self.lista_digipymons = lista_digipymons
        self.cantidad_digipymon = cantidad_digipymon

    """
    Función "añadir_digipymon".
    "lista_digipymon.append(digipymon)" Utilizamos append para añadir el digipymon a la lista.
    """
    def añadir_digipymon(self, digipymon):
        self.lista_digipymons.append(digipymon)
        self.cantidad_digipymon = self.cantidad_digipymon + 1 
        