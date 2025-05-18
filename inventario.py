"""
    Clase "Inventario".
    Importamos la clase "Jugador".
"""

from jugador import Jugador
class Inventario:
    """
    Función "__init__".
    Inicializamos el diccionario de "Objetos" vacía.
    """
    def __init__(self):
        self.objetos = {}

    """
    Función "añadir_objeto".
    Utilizamos esta función para añadir el nombre al diccionario de "Objetos".
    """
    def añadir_objeto(self, nombre, cantidad):
        if nombre in self.objetos:
            self.objetos[nombre] += cantidad
        else:
            self.objetos[nombre] = cantidad
    
    """
    Función "usar_objeto".
    Cuando usamos un item que está en el array, se quita de la lista.
    """
    def usar_objeto(self, nombre):
        if nombre in self.objetos and self.objetos[nombre] > 0:
            self.objetos[nombre] -= 1
            print(f"Has usado {nombre}")

        elif nombre in self.objetos:
            self.objetos[nombre] -= 1
                
        else:
            print("No tienes este objeto")

    """
    Método "__str__" para imprimir el inventario.
    """
    def __str__(self):
         return f"Inventario: {self.objetos}"