from jugador import Jugador
class Inventario:
    def __init__(self):
        self.objetos = {}

    def añadir_objeto(self, nombre, cantidad):
        if nombre in self.objetos:
            self.objetos[self.nombre] + cantidad

        else:
            self.objetos[self.nombre]
    
    def usar_objeto(self, nombre):
        if nombre in self.objetos:
            self.objeto[self.nombre] - 1
        elif self.cantidad >= 0:
                self.cantidad.remove[self.nombre]
        else:
                print("No tienes este objeto")