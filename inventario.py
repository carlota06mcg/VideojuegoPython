from jugador import Jugador
class Inventario:
    def __init__(self):
        self.objetos = {}

    def añadir_objeto(self, nombre, cantidad):
        if nombre in self.objetos:
            self.objetos = self. + 1
        else:
            self.objetos = self.nombre
    
    def usar_objeto(self, nombre)
        if nombre in self.objetos:
            if cantidad >= 0:
                cantidad.remove[self.nombre]
            elif:
                self.objeto[self.nombre] - 1
            else:
                print("No tienes este objeto")