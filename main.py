import time
import random
from listaNombres import ListaNombres
from digipymon import Digipymon
from enemigo import Enemigo
from jugador import Jugador
from inventario import Inventario

"""
    Función de "menú" creada con prints, el cual usamos en el main para imrpimir las opciones.
"""
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


"""
    Funcion de "buscar digipymon aleatorio" para poder generar aleatoriamente un digipymon.
    Utilizamos random.randint para generar un numero aleatorio entre los parámetros que hayamos puesto.
"""
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

"""
    Funcion de "buscar digipymon", utilizada para buscar un digipymon aleatorio con la funcion de "buscar digipymon aleatorio".
    Pasamos por parámetros: jugador1 : Jugador, inventario1 : Inventario para acceder a los atributos.
    La variable 'prob = 100 - digipymon.nivel * 10' es utilizada para calcular la probabilidad de capturar al digipymon de forma aleatoria.
    Creamos una sentencia condicional if, en la cual si pulsamos "s" (y las condiciones se cumplen), se captura el digipymon y lo imprime tras almacenarlo en el inventario.
"""
def buscar_digipymon(jugador1 : Jugador, inventario1 : Inventario):
    digipymon = buscar_digipymon_aleatorio()
    print(f"Has encontrado un {digipymon.nombre} salvaje")
    prob = 100 - digipymon.nivel * 10
    print(f"Tu probabilidad de captura: {prob}%")
    print("Pulsa 's' para capturarlo")
    print("Pulsa 'n' para continuar sin capturarlo")
    opcion = input("Quieres capturar un digipymon??")

    if opcion == "s":
        print("Capturando...")
        if inventario1.objetos["digipyball"] > 0 and jugador1.cantidad_digipymon < 6:
            digipymon_capturado = random.randint(1, 100)
            if digipymon_capturado > prob:
                print("No has capturado digipymon!")
                inventario1.usar_objeto("digipyball") 

            else:
                print("Has capturado un digipymon!! :3")
                jugador1.añadir_digipymon(digipymon)
                print(f"El digipymon que has capturado es...")
                print(digipymon)

    else:
        print("Has elegido no capturar el digipyball!")
        time.sleep(1)
        print("Decides huir sin nada")
        
"""
    Función "usar item" en la cual accedemos al inventario y podemos usar los objetos que hayamos comprado en la tienda en el digipymon que queramos.
    Una vez escribamos el nombre del item que queramos usar, si está en nuestro inventario nos preguntará en que digipymon queremos usarlo.
    Si usamos un item, dependiendo de la mejora que aporte se le suma al digipymon de nuestra elección.
"""
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

    if objeto == "digipyball":
        print("No puedes utilizar las digipyballs! Elige otra opcion")

    if objeto == "pocion":
        if inventario.objetos.get("pocion", 0) > 0:
            jugador.consultar_digipymon()
            usarEnDigipymon = input("¿En qué digipymon quieres aplicar la pocion??")
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


"""
    Función de "digishop", la cual utilizamos para comprar objetos que se almacenarán en nuestro inventario.
    Para poder comprar items debemos trener digicoins, sino no podremos comprar items.
    Cuando compramos un item, este se almacena en nuestro inventario y nos quita digicoins dependiendo del coste.
"""
def digishop(jugador1: Jugador, inventario1: Inventario): 
    print("Bienvenido a la DigiShop " + jugador1.nombre)
    print("Tienes " + str(jugador1.digicoins) + " monedas")  
    time.sleep(3)
    salir = False
    while salir == False:
        print("----------Tienda----------")
        print("1. ---> Digipyballs:   ")
        print("        Precio: 5 digicoins")
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

"""
    Funcion que devuelve la variable multiplicador para que 
    al tener ventaja de tipo el Digipymon tenga mas ataque
    y por lo tanto haga mas daño
"""

def tipos_digipymon(tipo_digiJugador, tipo_digiEnemigo):
    
    if tipo_digiJugador == "planta" and tipo_digiEnemigo == "agua":
        return  2
    elif tipo_digiJugador == "agua" and tipo_digiEnemigo == "fuego":
        return 2
    elif tipo_digiJugador == "fuego" and tipo_digiEnemigo == "planta":
        return 2
    elif tipo_digiJugador == "agua" and tipo_digiEnemigo == "planta":
        return 0.5
    elif tipo_digiJugador == "fuego" and tipo_digiEnemigo == "agua":
        return 0.5
    elif tipo_digiJugador == "planta" and tipo_digiEnemigo == "fuego":
        return 0.5
    else:
        return 1

    

"""
    Función de "Combate", en la cual lucharemos contra un enemigo. 
    Nos da opción de abandonar el combate o de luchar contra el enemigo.
    El combate podemos ganarlo, perderlo o empatar.
"""
def combate(jugador1: Jugador):
    # Se obtiene el nombre del entrenador enemigo y se crea el objeto Enemigo
    listaNombres1 = ListaNombres()
    nombre_enemigo = listaNombres1.obtener_nombre_entrenador()
    enemigo1 = Enemigo(nombre_enemigo)
    print(f"Tu enemigo es {nombre_enemigo}")
    
    # Inicializamos contadores de victoria y derrota
    victoria = 0
    derrota = 0
    
    # Creamos la lista de Digipymon del enemigo según la cantidad que tiene el jugador
    enemigo1.lista_digipymons = []
    for _ in range(jugador1.cantidad_digipymon):
        digipymon1 = buscar_digipymon_aleatorio()
        enemigo1.añadir_digipymon(digipymon1)
    
    abandonar = input("¿Quieres abandonar el combate? (s/n): ")
    
    if abandonar.lower() == "s":
        jugador1.digicoins -= 1
        print("Has huido del combate. Pierdes 1 digicoin.")
        return  # Termina la función

    elif abandonar.lower() == "n":
        for i in range(jugador1.cantidad_digipymon):
            # Referenciamos el Digipymon del jugador y el enemigo para cada ronda ronda
            jugador_digi = jugador1.lista_digipymon[i]
            enemigo_digi = enemigo1.lista_digipymons[i]
            
            # Obtenemos los tipos de cada uno
            tipo_jugador = jugador_digi.tipo
            tipo_enemigo = enemigo_digi.tipo

            print(f"\nCombate {i + 1}:")
            print(f"{jugador_digi.nombre} (tipo: {tipo_jugador}, ataque base: {jugador_digi.ataque}) vs {enemigo_digi.nombre} (tipo: {tipo_enemigo}, ataque base: {enemigo_digi.ataque})")
            
            # Calculamos el multiplicador de cada uno usando la función de tipos
            jugador_multiplicador = tipos_digipymon(tipo_jugador, tipo_enemigo)
            enemigo_multiplicador = tipos_digipymon(tipo_enemigo, tipo_jugador)
            
            # Calculamos el ataque final (aumento de ataque) de cada uno
            aumento_ataque_jugador = jugador_digi.ataque * jugador_multiplicador
            aumento_ataque_enemigo = enemigo_digi.ataque * enemigo_multiplicador
            
            print(f"Ataque final: {jugador_digi.nombre}: {aumento_ataque_jugador:.1f}  |  {enemigo_digi.nombre}: {aumento_ataque_enemigo:.1f}")
            
            # Comparamos los ataques finales y aplicamos daño (se resta la cantidad correspondiente de la vida)
            if aumento_ataque_jugador > aumento_ataque_enemigo:
                enemigo_digi.vida -= aumento_ataque_jugador
                victoria += 1
                print("¡Has ganado este combate!")
            elif aumento_ataque_jugador < aumento_ataque_enemigo:
                jugador_digi.vida -= aumento_ataque_enemigo
                derrota += 1
                print("Has perdido este combate.")
            else:
                print("Empate en este combate.")
        
        # Resultado final del combate
        print("\nResultado Final:")
        if victoria > derrota:
            print(f"¡Has ganado el combate total! Ganas {victoria} digicoins.")
            jugador1.digicoins += victoria
        elif derrota > victoria:
            print(f"Has perdido el combate total. Pierdes {derrota} digicoins.")
            jugador1.digicoins -= derrota
        else:
            print("El combate ha terminado en empate. No ganas ni pierdes digicoins.")
    else:
        print("Opción inválida.")




"""
    Función "Main", en la cual implementamos todas las funciones creadas anteriormente.
    Llamamos a nuestro "Menú" para que el usuario introduzca por pantalla la opción que quiera.
"""
def main():
    print("Bievenido a Digipymon! ")
    nombre = input("Como te llamas? ")
    inventario1 = Inventario()
    inventario1.añadir_objeto("digipyball", 2)
    jugador1 = Jugador(nombre)
    digipymon1 = buscar_digipymon_aleatorio()
    jugador1.añadir_digipymon(digipymon1)
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
            jugador1.consultar_digipymon()
            
            
        elif(opcion_menu == 7):
            print("Saliendo del juego..")
            time.sleep(3)
            salir = True
        else:
            print("Escoge una opcion correcta")


if __name__ == "__main__":
    main()