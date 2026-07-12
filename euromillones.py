import random

# BLOQUE 1
# Función para generar las combinaciones de #'s del 1 al 50 y las estrellas
def generar_combinacion(n_combinaciones):
    todas_las_jugadas =  []
    
    # bucle para extraer cada valro inidvidual en varias vueltas
    for _ in range(n_combinaciones):
        num_5 = random.sample(range(1, 51), 5)
        star_2 = random.sample(range(1, 13), 2)
        # Creamos un diccionario para almacenar
        jugada = {"numeros": num_5, "estrellas": star_2}
        todas_las_jugadas.append(jugada)

    # retornamos el resultado almacenado en "todas_las_jugadas"
    return todas_las_jugadas


# BLOQUE 2
# Acá le pediremos al usuario ingresar qué cantidad de COMBINACIONES de EUROMILLION quiere producir.
while True:
    numero = input('¿Cuántas combinaciones de EUROMILLONES deseas imprimir?\nLetra "q" si deseas cancelar: ').lower()

    # Salida para cancelar el código
    if numero == 'q'.lower():
        break

    # Ahora crearemos el prueba-error con el valor que el usuario va a introducir arriba...
    try:
        numero2 = int(numero)
        # llamamos la función y atraparemos el resultado de la misma en una varible (resultado)
        resultado = generar_combinacion(numero2)

        # Imprimimos los resultados para cumplir el reto
        print('\n-----------------------Tus Combinaciones---------------------------')
        for i, juego in enumerate(resultado, start=1):
            print(f"Combinación {i}: Números: {juego['numeros']}  |  Estrellas: {juego['estrellas']}")
        print("===================================================================\n")


    except ValueError:
        print("No válido, inténtalo de nuevo... Introduce un # entero o 'q' para salir: \n")
        continue
