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
    ("-----------------------------")


def buscar_digipymon_aleatorio():
    lista = ListaNombres()
    lista_tipos = ["planta", "fuego", "agua"]
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
    prob = 100 - digipymon.nivel * 10
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
    print("----------Usar Items----------")
    print(" · digipyballs")
    print(" · pocion")
    print(" · anabolizantes")
    print("------------------------------")
    objeto = input("Escribe el nombre del objeto que quieras utilizar: ").lower()
    print(".")
    time.sleep(1)
    print(". .")
    time.sleep(1)
    print(". . .")
    time.sleep(1)

    if objeto == "pocion":
        if inventario.objetos.get("pocion", 0) > 0:
            #inventario.usar_objeto("pocion")
            jugador.consultar_digipymon()
            usarEnDigipymon = input("¿En qué digipymon quieres aplicar las pocion??")
            for digipymon in jugador.lista_digipymon:
                if digipymon.nombre == usarEnDigipymon:
                    digipymon.vida += 20
                    print(f"{digipymon.nombre} tiene ahora +20 de vida")
                else:
                    print("No existe el digipymon")       
        else:
            print("No tienes pociones")

    if objeto == "anabolizantes":
        if inventario.objetos.get("anabolizantes", 0) > 0:
            #inventario.usar_objeto("anabolizantes")
            jugador.consultar_digipymon()
            usarEnDigipymon = input("¿En qué digipymon quieres aplicar los anabolizantes??")
            for digipymon in jugador.lista_digipymon:
                if digipymon.nombre == usarEnDigipymon:
                    digipymon.ataque += 10
                    print(f"{digipymon.nombre} tiene ahora +10 de ataque")
                else:
                    print("No existe el digipymon") 
        else:
            print("No tienes anabolizantes")

    


def digishop(jugador1: Jugador, inventario1: Inventario): 
    print("Bienvenido a la DigiShop " + jugador1.nombre)
    print("Tienes " + str(jugador1.digicoins) + " monedas")  
    time.sleep(3)
    salir = False
    while salir == False:
        print("----------Tienda----------")
        print("1. ---> Digipyballs:   ")
        print("        Precio: 5 digicoins")
        print("        Bonus: +20 de vida")
        print(" ")
        print("2. ---> Poción:   ")
        print("        Precio: 3 digicoins")
        print("        Bonus: +20 de vida")
        print(" ")
        print("3. ---> Anabolizantes:   ")
        print("        Precio: 4 digicoins")
        print("        Bonus: +10 de ataque")
        print(" ")
        print("4. ---> EXIT")
        print("---------------------------")
        opcion_digishop = int (input("Elige una opcion "))
        if opcion_digishop == 1:
            if jugador1.digicoins >= 5:
                jugador1.digicoins = jugador1.digicoins - 5
                inventario1.añadir_objeto("digipyball", 1)
                print("Has comprado una Digipyball")
            else:
                print("No tienes suficientes monedas")

        if opcion_digishop == 2:
            if jugador1.digicoins >= 3:
                jugador1.digicoins = jugador1.digicoins - 3
                inventario1.añadir_objeto("pocion", 1)
                print("Has comprado una pocion")
            else:
                print("No tienes suficiente dinero")

        if opcion_digishop == 3:
            if jugador1.digicoins >= 4:
                jugador1.digicoins = jugador1.digicoins - 4
                inventario1.añadir_objeto("anabolizantes", 1)
                print("Has comprado un anabolizante")
            else:
                print("No tienes suficiente dinero")
        if opcion_digishop == 4:
            print("Saliendo de la tienda... ")
            time.sleep(3)
            salir = True


def combate(jugador1: Jugador):
    listaNombres1 = ListaNombres()
    nombre_enemigo = listaNombres1.obtener_nombre_entrenador()
    enemigo1 = Enemigo(nombre_enemigo)
    print(f"Tu enmigo es  {nombre_enemigo} ")
    victoria = 0
    derrota = 0
    enemigo1.lista_digipymons = []
    for _ in range(0, jugador1.cantidad_digipymon):
        digipymon1 = buscar_digipymon_aleatorio()
        enemigo1.añadir_digipymon(digipymon1)

    abandonar = input("Quieres abandonar el combate s/n ")
    
    if abandonar == "s":
        jugador1.digicoins = jugador1.digicoins - 1
        print("Has huido del combate. Pierdes 1 digicoin.")

    elif abandonar == "n":

        for i in range(jugador1.cantidad_digipymon):
            if jugador1.lista_digipymon[i].ataque > enemigo1.lista_digipymons[i].ataque:
                perder_vida = jugador1.lista_digipymon[i].vida - enemigo1.lista_digipymons[i].ataque 
                jugador1.lista_digipymon[i].vida = perder_vida
                victoria = victoria + 1
                print("Has ganado este combate")
            elif jugador1.lista_digipymon[i].ataque < enemigo1.lista_digipymons[i].ataque:
                diferencia = enemigo1.lista_digipymons[i].ataque - jugador1.lista_digipymon[i].ataque
                jugador1.lista_digipymon[i].vida = jugador1.lista_digipymon[i].vida - diferencia
                derrota = derrota + 1
                print("Has perdido este combate")
            else:
                print("Empate. ")

        if victoria > derrota:
            print("Has ganado el combate")
            print("Has ganado " + str(victoria) + " digicoins")
            jugador1.digicoins = jugador1.digicoins + victoria
        elif derrota > victoria:
            print("Has perdido el combate")
            print("Has perdido " + str(derrota) + " digicoins")
            jugador1.digicoins = jugador1.digicoins - derrota
        else:
            print("Empate. No ganas ni pierdes digicoins.")
    else:
        print("Introduzca una opción válida")

    
def main():
    print("Bievenido a Digipymon! ")
    nombre = input("Como te llamas? ")
    inventario1 = Inventario()
    jugador1 = Jugador(nombre)
    digipymon1 = buscar_digipymon_aleatorio()
    print(f"Has recibido un incial  {digipymon1}")
    print("Bienvenido entrando al menu... ")
    salir = False
    while salir == False:
        menu()
        opcion_menu = int(input("Escoge una opcion "))
        if opcion_menu == 1:
            buscar_digipymon(jugador1, inventario1)

        elif opcion_menu == 2:
            combate(jugador1)

        elif opcion_menu == 3:
            digishop(jugador1, inventario1)

        elif(opcion_menu == 4):
            usar_item(inventario1, jugador1)

        elif opcion_menu == 5:
            print(inventario1)

        elif(opcion_menu == 6):
            print(digipymon1)
            
        elif(opcion_menu == 7):
            print("Saliendo del juego..")
            time.sleep(3)
            salir = True
        else:
            print("Escoge una opcion correcta")


if __name__ == "__main__":
    main()









