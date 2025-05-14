import time
import random
from listaNombres import ListaNombres
from digipymon import Digipymon
from enemigo import Enemigo
from jugador import Jugador
from inventario import Inventario


def menu():
    print("----------Menu----------")
    print("Introduce 1 si quieres buscar un digipymon")
    print("Introduce 2 si quieres luchar contra un entrenador")
    print("Introduce 3 si quieres ir a la tienda")
    print("Introduce 4 si quieres usar objetos")
    print("Introduce 5 si quieres consultar el inventario")
    print("Introduce 6 si quieres consultar digipymon")
    print("Introduce 7 si quieres salir")


def buscar_digipymon_aleatorio():
    lista = ListaNombres()
    lista_tipos = ["aire", "fuego", "agua"]
    nombre = lista.obtener_nombre_digipymon()
    vida = random.randint(10, 20)
    ataque = random.randint(1, 10)
    nivel = random.randint(1, 3)
    tipo = random.choice(lista_tipos)
    digipymon1 = Digipymon(nombre, vida, ataque, tipo, nivel)
    return digipymon1


def buscar_digipymon(jugador1 : Jugador, inventario1 : Inventario):
    digipymon = buscar_digipymon_aleatorio()
    print(f"Has encontrado un {digipymon.nombre} salvaje")
    prob = 100 - digipymon * 10
    print(f"Tu probabilidad de captura: {prob}%")

    opcion = input("Quieres capturar un digipymon??")
    print("Pulsa 's' para capturarlo")
    print("Pulsa 'n' para continuar sin capturarlo")

    if opcion == "s":
        time.sleep(2)
        print("Capturando...")
        if inventario1.objetos["digipyball"] > 0 and jugador1.cantidad_digipymon < 6:
            digipymon_capturado = random.randint(1, 100)
            if digipymon_capturado > prob:
                print("No has capturado digipymon!")
                inventario1.usar_objeto("digipyball") 

        else:
            print("Has capturado un digipymon!! :3")
            jugador1.añadir_digipymon(digipymon)
            print(f"El digipymon que has capturado es {digipymon.nombre}")
            inventario1.usar_objeto("digipyball")
    else:
        time.sleep(2)
        print("Has elegido no capturar el digipyball!")
        print("Decides huir sin nada")
        

def usar_item(inventario : Inventario, jugador : Jugador):
    for nombre, cantidad in inventario.objetos.items():
        print(nombre, cantidad)

    


def digishop(jugador1: Jugador, inventario1: Inventario): 
    print("Bienvenido a la DigiShop " + jugador1.nombre)
    print("Tienes " + str(jugador1.digicoins) + "monedas")  
    time.sleep(3)
    salir = False
    while salir == False:
        print("----------Tienda----------")
        print("Pulse 1 si quieres comprar digipyballs: 5 digicoins  ")
        print("Pulse 2 si quieres comprar pocion: 3 digicoins  ")
        print("Pulse 3 si quieres comprar anabolizantes: 4 digicoins  ")
        print("Pulse 4 si quieres salir")
        opcion_digishop = int (input("Elige una opcion"))
        if opcion_digishop == 1:
            if jugador1.digicoins >= 5:
                jugador1.digicoins = jugador1.digicoins - 5
                inventario1.añadir_objeto("Digiball", 1)
                print("Has comprado una Digiball")
            else:
                print("No tienes suficientes monedas")

        if opcion_digishop == 2:
            if jugador1.digicoins >= 3:
                jugador1.digicoins = jugador1.digicoins - 3
                inventario1.añadir_objeto("Pocion", 1)
                print("Has comprado una pocion")
            else:
                print("No tienes suficiente dinero")

        if opcion_digishop == 3:
            if jugador1.digicoins >= 4:
                jugador1.digicoins -= 4
                inventario1.añadir_objeto("Anabolizantes")
                print("Has comprado un anabolizante")
            else:
                print("No tienes suficiente dinero")
        if opcion_digishop == 4:
            print("Saliendo de la tienda... ")
            time.sleep(3)
            salir = True


def combate(jugador1: Jugador):
    listaNombres1 = ListaNombres()
    enemigo1 = Enemigo()
    digipymon1 = buscar_digipymon_aleatorio()
    print("Tu enemigo es " + listaNombres1.nombre)
    for jugador1.cantidad_digipymon in range:
        enemigo1.añadir_digipymon
    abandonar = input("Quieres abandonar el combate s/n")
    if abandonar == "s":
        jugador1.digicoins -= 1
    elif abandonar == "n":
         for i in range(0, jugador1.cantidad_digipymon - 1):
             victoria = 0
             derrota = 0
             
             if jugador1.lista_digipymon[i].ataque > enemigo1.lista_digipymons[i].ataque:
                jugador1.lista_digipymon[i].vida - enemigo1.lista_digipymons[i].ataque 
                victoria = victoria + 1
                print("Has gando este combate")
             else:
                diferencia = enemigo1.lista_digipymons[i].ataque - jugador1.lista_digipymon[i].ataque
                jugador1.lista_digipymon[i].vida - diferencia
                derrota = derrota + 1
                print("Has perdido este combate")
         if victoria > derrota:
             resultado_victoria = victoria - derrota

             print("Has ganado el combate ")
             print("Has ganado " + resultado_victoria + ("digicoins"))
             jugador1.digicoins + resultado_victoria
             victoria = 0
             derrota = 0
        
    else:
        print("Introduzca una opcion valida")


        



def main():
    print("Bievenido a Digipymon! ")
    nombre = input("Como te lamas? ")
    print("Bienvenido entrando al menu... ")
    inventario1 = Inventario()
    jugador1 = Jugador(nombre)
    digipymon1 = buscar_digipymon_aleatorio()
    salir = False
    while salir == False:
        menu()
        opcion_menu = int(input("Escoge una opcion"))
        if opcion_menu == 1:
            buscar_digipymon(jugador1, inventario1)
        elif opcion_menu == 2:
            combate(jugador1)
        elif opcion_menu == 3:
            digishop(jugador1, inventario1)
        elif(opcion_menu == 4):
            inventario1.usar_objetos
        elif opcion_menu == 5:
            for nombre, cantidad in inventario1.objetos.items():
                print(f"{nombre} : {cantidad}")
        elif(opcion_menu == 6):
            print(digipymon1)
        elif(opcion_menu == 7):
            salir = True
        else:
            print("Escoge una opcion correcta")


main()








