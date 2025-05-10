import time

def menu():
    print("Introduce 1 si quieres buscar un digipymon")
    print("Introduce 2 si quieres luchar contra un entrenador")
    print("Introduce 3 si quieres ir a la tienda")
    print("Introduce 4 si quieres usar objetos")
    print("Introduce 5 si quieres consultar el inventario")
    print("Introduce 4 si quieres consultar digipymon")
    print("Introduce 5 si quieres salir")

def digishop(jugador, inventario): 
    print("Bienvenido a la DigiShop {jugador.nombre}")
    print("Tienes {jugador.monedas} monedas")  
    time.sleep(3)

    print("Pulse 1 si quieres comprar digipyballs: 5 digicoins  ")
    print("Pulse 1 si quieres comprar pocion: 3 digicoins  ")
    print("Pulse 1 si quieres comprar anabolizantes: 4 digicoins  ")



