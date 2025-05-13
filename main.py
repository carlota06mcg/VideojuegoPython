import time
def menu():
    print("Introduce 1 si quieres buscar un digipymon")
    print("Introduce 2 si quieres luchar contra un entrenador")
    print("Introduce 3 si quieres ir a la tienda")
    print("Introduce 4 si quieres usar objetos")
    print("Introduce 5 si quieres consultar el inventario")
    print("Introduce 6 si quieres consultar digipymon")
    print("Introduce 7 si quieres salir")

def digishop(jugador, inventario): 
    print("Bienvenido a la DigiShop {jugador.nombre}")
    print("Tienes {jugador.monedas} monedas")  
    time.sleep(3)
    salir = False
    jugador1 = jugador()
    inventario1 = inventario()
    while salir == False:
        print("Pulse 1 si quieres comprar digipyballs: 5 digicoins  ")
        print("Pulse 2 si quieres comprar pocion: 3 digicoins  ")
        print("Pulse 3 si quieres comprar anabolizantes: 4 digicoins  ")
        print("Pulse 4 si quieres salir")
        opcion_digishop = input("Elige una opcion")
        if opcion_digishop == 1:
            if jugador1.digicoins >= 5:
                jugador1.digicoins - 5
                inventario1.añadir_objetos.append("Digiball", 1)
                print("Has comprado una Digiball")
            else:
                print("No tienes suficientes monedas")

        if opcion_digishop == 2:
            if jugador1.digicoins >= 3:
                jugador1.digicoins - 3
                inventario1.añadir_objetos.append("Pocion", 1)
                print("Has comprado una pocion")
            else:
                print("No tienes suficiente dinero")

        if opcion_digishop == 3:
            if jugador1.digicoins >= 4:
                jugador1.digicoins - 4
                inventario1.añadir_objetos.append("Anabolizantes")
                print("Has comprado un anabolizante")
            else:
                print("No tienes suficiente dinero")
        if opcion_digishop == 4:
            print("Saliendo del juego...")
            time.sleep(3)
            salir = True
 def main():
    salir = False
    while menu == False:
        menu()
        opcion_menu = input("Escoge una opcion")
    
        


 main()








