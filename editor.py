# Lista de opciones del menú
opciones = ["a) Introducir nueva línea", "b) Eliminar última línea introducida", "c) Imprimir líneas editadas y salir", "d) Mostrar el texto en hexadecimal"]

# Variable para almacenar la línea editada y la posicion inicial, que es 0 al empezar
linea_editada = ""
posicion_final = 0

# Lista para almacenar las cadenas que podemos añadir
lineas_editadas = []

# Bucle principal del menú
while True:

    # Mostrar el menú de la lista opciones
    for opcion in opciones:
        print(opcion)

    # Solicitar la opción del usuario que tiene que ser a,b,c,d
    opcion_usuario = input("Introduzca su opción: ") # Solicita al usuario que introduzca una opción con el input

    # hacemos un condicional para las diferentes opciones
    if opcion_usuario == "a":

        # Solicitar el texto a añadir 
        nuevo_texto = input("Texto a añadir: ")

        # Agregar el nuevo texto a la línea editada y hacemos que se apilen una sobre otra
        linea_editada += nuevo_texto + "\n"
        posicion_final += len(nuevo_texto) + 1 # Devuelve la longitud del nuevo texto para poder guardarla en la posicion final

        # Agregar la nueva línea a la lista
        lineas_editadas.append(linea_editada)
        linea_editada = ""  # Reiniciar la variable despues de agregarla a lineas_editadas para que no nos la muestre dos veces

    elif opcion_usuario == "b":
        # Eliminar la última línea introducida
        if len(lineas_editadas) > 0:
            # Eliminar la última línea de lineas_editadas
            lineas_editadas.pop()
            # Si aún hay líneas editadas, actualiza linea_editada con la última línea
            if lineas_editadas:
                linea_editada = lineas_editadas[-1]
            else:
                linea_editada = ""

    elif opcion_usuario == "c":

        # Imprimir la línea editada y salir del bucle
        print("Las líneas que escribió fueron:")
        for linea in lineas_editadas:
            print("{0}".format(linea))
        break

    elif opcion_usuario == "d":

        # Mostrar el texto en hexadecimal
        print("Texto en hexadecimal:")
        for i in range(len(linea_editada)):
            print("{0:04} ".format(int(hex(ord(linea_editada[i]))[2:], 16)), end='')  # Modificación aquí
        print() # Imprime el texto en hexadecimal

    else:

        # Mensaje de error por opción no válida
        print("Por favor, introduzca una opción válida.")

    # Mostrar las cadenas anteriores (excepto si se elige la opción "c")
    if opcion_usuario != "c" and opcion_usuario != "d":  # Agregamos que no muestre las líneas si la opción es "d"
        print("Las líneas que escribió fueron:")
        for linea in lineas_editadas:
            print("{0}".format(linea))
