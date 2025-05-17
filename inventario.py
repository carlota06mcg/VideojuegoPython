from jugador import Jugador
class Inventario:
    def __init__(self):
        self.objetos = {}

    def añadir_objeto(self, nombre, cantidad):
        if nombre in self.objetos:
            self.objetos[nombre] += cantidad
        else:
            self.objetos[nombre] = cantidad
    
    def usar_objeto(self, nombre):
        if nombre in self.objetos and self.objetos[nombre] > 0:
            self.objetos[self.nombre] -= 1
            print(f"Has usado {nombre}")

        elif nombre in self.objetos:
            self.cantidad[nombre] -= 1
                
        else:
            print("No tienes este objeto")

    def __str__(self):
         return f"Inventario: {self.objetos}"