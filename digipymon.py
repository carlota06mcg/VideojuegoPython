"""
    Clase "Digipymon".
"""
class Digipymon:
    """
    Función "__init__".
    Definimos los atributos de nombre, vida, ataque, tipo, nivel.
    """
    def __init__(self, nombre, vida, ataque, tipo, nivel):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.tipo = tipo
        self.nivel = nivel

    """
    Método "__str__" para imprimir el digipymon.
    """
    def __str__(self):
        return f"Nombre: {self.nombre}, vida: {self.vida}, ataque: {self.ataque}, tipo: {self.tipo}, nivel: {self.nivel}"