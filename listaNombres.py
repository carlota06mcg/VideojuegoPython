import random
class listaNombres:
    def __init__(self):
        self.lista_nombres_digipymon = ["charmander", "squirtle", "bulbasaur", "chicorita", "cindaquil", "totodile", "treecko", "totus", "mudkip", "jigglypuff", "kirby", "sylveon", "chansey", "espeon", "eevee", "krookodile", "grookey", "piplup", "skitty"]
        self.lista_nombres_entrenadores = ["Ash", "Mitsy", "Taylor", "Cynthia", "Serena", "Dawn", "Iris", "Erika","Skyla","Roxanne","Sabrina","Serena", "Clair", "Valerie", "Gardenia","Wiona","Flannery", "Synthia", "Nyara", "Yurika"]

    def obtener_nombre_digipymon(lista_nombres_digipymon):
        aleatorio_nombre = random.choice(lista_nombres_digipymon)
        return aleatorio_nombre

    def obtener_nombre_entrenador(lista_nombres_entrenadores):
        aleatorio_entrenador = random.choice(lista_nombres_entrenadores)
        return aleatorio_entrenador