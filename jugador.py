"""
    Clase "Jugador".
"""
class Jugador:
    """
    Función "__init__".
    Inicializamos 'nombre', 'lista_digipymon' como una lista vacía, cantidad_digipymon y digicoins.
    """
    def __init__(self, nombre):
        self.nombre = nombre
        self.lista_digipymon = []
        self.cantidad_digipymon = 0
        self.digicoins = 10

    """
    Función "añadir_digipymon".
    "lista_digipymon.append(digipymon)" Utilizamos append para añadir el digipymon a la lista.
    "cantidad_digipymon" Es usado para sumar +1 a la cantidad dde digipymons que tenemos.
    """
    def añadir_digipymon(self, digipymon):
        self.lista_digipymon.append(digipymon)
        self.cantidad_digipymon = self.cantidad_digipymon + 1
        return digipymon

    """
    Función "consultar_digipymon".
    Utilizamos esta función para imprimir los digipymons que tenemos en la lista.
    """
    def consultar_digipymon(self):
        if not self.lista_digipymon:
            print("No tienes digipymons.")
        else:
            print("Tus digipymons son:")
            for digipymon in self.lista_digipymon:
                print(digipymon) 
        
    """
    Función "mostrar_digicoins".
    Utilizamos esta función para imprimir las digicoins que tenemos.
    """
    def mostrar_digicoins(self):
        print("Tienes " + str(self.digicoins) + " digicoins")
