"""
    Clase "ListaNombres".
    Importamos el "random" para poder escoger de forma aleatoria un nombre de digipymon y un entrenador aleatorios.
"""
import random
class ListaNombres:
    """
    Función "__init__".
    Inicializamos 'lista_nombres_digipymon' y 'lista_nombres_entrenadores'
    """
    def __init__(self):
        self.lista_nombres_digipymon = ["charmander", "squirtle", "bulbasaur", "chicorita", "cindaquil", "totodile", "treecko", "totus", "mudkip", "jigglypuff", "kirby", "sylveon", "chansey", "espeon", "eevee", "krookodile", "grookey", "piplup", "skitty"]
        self.lista_nombres_entrenadores = ["Ash", "Mitsy", "Taylor", "Cynthia", "Serena", "Dawn", "Iris", "Erika","Skyla","Roxanne","Sabrina","Serena", "Clair", "Valerie", "Gardenia","Wiona","Flannery", "Synthia", "Nyara", "Yurika"]
    
    """
    Función "obtener_nombre_digipymon".
    Obtener de forma aleatoria un nombre de digipymon de la lista_nombres_digipymon.
    """
    def obtener_nombre_digipymon(self):
        aleatorio_nombre = random.choice(self.lista_nombres_digipymon)
        return aleatorio_nombre

    """
    Función "obtener_nombre_entrenador"
    Obtener de forma aleatoria un nombre de entrenador de la lista_nombres_entrenadores.
    """
    def obtener_nombre_entrenador(self):
        aleatorio_entrenador = random.choice(self.lista_nombres_entrenadores)
        return aleatorio_entrenador