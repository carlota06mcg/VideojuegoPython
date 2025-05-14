from jugador import Jugador
class Inventario:
    def __init__(self):
        self.objetos = {}

    def añadir_objeto(self, nombre, cantidad):
        if nombre in self.objetos:
            self.objetos[nombre] = self.objetos[nombre] + cantidad

        else:
            self.objetos[nombre] = cantidad
    
    def usar_objeto(self, nombre):
        if nombre in self.objetos:
            self.objeto[self.nombre] - 1
        elif self.cantidad >= 0:
                self.objetos[nombre] = self.cantidad[nombre] - 1
        else:
                print("No tienes este objeto")