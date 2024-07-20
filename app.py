from datos import *
import pokemon
from tirar_dado import tirar_dado
import time
from entrenador import obtener_datos_entrenador, elegir_pokemon

#Realizar un ciclo infinito para que cada vez que inicie el juego la vida vuelva a 100

while True:

    print("\n=== Bienvenido al juego de Pokemon ===\n")

    entrenador1 = obtener_datos_entrenador()
    entrenador2 = obtener_datos_entrenador()

    print(f"\nEl Entrenador {entrenador1.nombre} del Gimnasio {entrenador1.gimnasio} se enfrenta al...")
    print(f"Entrenador {entrenador2.nombre} del Gimnasio {entrenador2.gimnasio}!!!\n")
    time.sleep(2)

    # La seleccion del gimnasio se realiza al azar entre los 2 entrenadores
    elige_gimnasio = tirar_dado() 

    if elige_gimnasio == 1:
        entrenador_elige_gim = entrenador1.nombre
    else:
        entrenador_elige_gim = entrenador2.nombre

    def elegir_gimnasio():
        # Mostrar los gimnasios disponibles
        print("Estos son los gimnasios disponibles:")
        for i, gimnasio in enumerate(gimnasios_disponibles, start=1):
            print(f"{i} - {gimnasio.nombre} en {gimnasio.ciudad}, {gimnasio.region}")

        while True:
                opcion = int(input("Elige el número del gimnasio que deseas: "))
                if 1 <= opcion <= len(gimnasios_disponibles):
                    gimnasio_elegido = gimnasios_disponibles[opcion - 1]
                    print(f"{entrenador_elige_gim } eligio el {gimnasio_elegido.nombre} en {gimnasio_elegido.ciudad}, {gimnasio_elegido.region}.")
                    return gimnasio_elegido
                else:
                    print("Opción no válida. Inténtalo de nuevo.")


    print(f"El Entrenador {entrenador_elige_gim} elige el gimnasio...\n")
    time.sleep(2)
    elegir_gimnasio()

    time.sleep(2)

    #El jugador 1 elige su pokemon
    print(f"\n{entrenador1.nombre} elige su Pokémon:")
    pok1 = elegir_pokemon()
    #El jugador 2 elige su pokemon
    print(f"\n{entrenador2.nombre} elige su Pokémon:")
    pok2 = elegir_pokemon()

    # Inicia el primer turno eligiendo uno de los 2 jugadores al azar.
    turno = tirar_dado() 
    
    #Sistema de turnos
    print("\n == INICIO LA BATALLA ==")
    time.sleep(2)
    print(f"{pok1.nombre} se enfrentara a {pok2.nombre}\n")
    time.sleep(2)

    while pok1.vida > 0 and pok2.vida > 0:
        if turno == 1:
            pok2.vida -= pok1.ataque
            print(f"{pok1.nombre} ataco, ahora {pok2.nombre} tiene {int(pok2.vida)} puntos de vida")
            turno = 2        
        else: 
            pok1.vida -= pok2.ataque
            print(f"{pok2.nombre} ataco, ahora {pok1.nombre} tiene {int(pok1.vida)} puntos de vida")
            turno = 1

        time.sleep(2)

        # Valida el comentario dependiendo si hay otra ronda mas o no
        if pok1.vida > 0 and pok2.vida > 0:
            print("\n== PROXIMA RONDA ==")

        
    # Imprime "FIN DE LA BATALLA" una vez que sale del bucle
    print("\n== FIN DE LA BATALLA ==")

    #Consulta cual pokemon gano e imprime el mensaje
    if pok1.vida <= 0:
        pok2.gano()
    else:
        pok1.gano()
        
# Preguntar al jugador si quiere reiniciar o terminar el juego
    opcion = input("Ingrese 1 para reiniciar el juego o 2 para terminar: ")
    if opcion == '2':
        print("Fin del juego.")
        print("Hasta la proxima entrenador!!! ;)")
        break