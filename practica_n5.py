print ("TRABAJO PRACTICO N° 3 ")


while True:
    print("""
Listado de Ejercicios:
Ejercicio 1: Ejercicio de Promedio de Notas y Ordenamiento
Ejercicio 2: Lista de productos con orden y eliminación
Ejercicio 3: Lista de Pares e Impares
Ejercicio 4: Lista sin repetidos
Ejercicio 5: Lista de estudiantes"
Ejercicio 6: Invertir una lista
Ejercicio 7: Matriz de temperaturas
Ejercicio 8: Matriz de estudiantes y notas
Ejercicio 9: Tablero de Ta TE Ti
""")

    option = input("Elija un ejercicio del 1 al 10, o 0 para salir: ")

    match option:
        case "1":
            notas=[7,6,8,9,10,5,4,7,8,9]
            print (notas)
            promedio = 0
            for nota in notas:
                promedio += nota
            promedio = promedio / len(notas)
            print(f"El promedio es: {promedio}")
        
        # para este ejercicio eligo insertion sort, 
        # por se estable y eficiente para listas pequeñas, como la de notas.

            def insertion_sort(notas):
                for i in range(1, len(notas)):
                    actual = notas[i]
                    j = i - 1
                    while j >= 0 and notas[j] > actual:
                        notas[j + 1] = notas[j]
                        j -= 1
                    notas[j + 1] = actual
                
                return notas
            notas_ordenadas = insertion_sort(notas)
            print("Notas ordenadas de menor a mayor:")
            print(f"La nota mas baja fue: {notas_ordenadas[0]} y la las alt: {notas_ordenadas[9]}") 
            print(notas_ordenadas) 
            print("\n#######################################################\n")  
    
        case "2":
            lista_productos = []
            
            while len (lista_productos) < 5: #Cuanbdo ingrese el quinto termina el buble.
                
                print("\nIngrese hasta 5 productos \n")
                
                producto = input(f" Ingrese el Producto {len(lista_productos)+1} / 5:  ")
                
                while not producto.isalpha() or producto == "":
                    print("Error: Debe ingresar al menos un producto y solo debe usar letras")
                    producto = input("Ingrese hasta 5 productos: ")
                
                lista_productos.append(producto) #Aca Creo la lista y agrego el producto.
            
                print(f"Ingrese el Producto {len(lista_productos)+1} / 5: ")
            
            else:
                print("Se han ingresado los 5 productos correctamente")
                print(lista_productos)  

            print ("\n Lista ordenada alfabeticamente: \n")

            productos_ordenados = sorted(lista_productos) #Ordeno la lista alfabeticamente.
            print(productos_ordenados) 

            borrar_producto = input("\nIngrese el nombre del producto que desea eliminar: ")        

            #verifico si el producto a eliminar esta en la lista.
            
            while borrar_producto not in lista_productos:
                print("Error: El producto no se encuentra en la lista.")
                borrar_producto = input("Ingrese el nombre del producto que desea eliminar: ")

            #Elimino el producto de la lista.
            lista_productos.remove(borrar_producto) 
            

            print(f"Producto '{borrar_producto}' eliminado correctamente.") 
            print("\nLista actualizada:\n")
            print(lista_productos)
            print("\n#######################################################\n")        

        case "3":
            #Importo Rndom
            
            import random
            #creo la lista de numeros aleatorios del 1 al 100, con 15 numeros enteros.
            lista_numeros = [random.randint(1, 100) for _ in range(15)]
            print(lista_numeros)

            lista_pares = []
            lista_impares = []

            for numero in lista_numeros:
                if numero % 2 == 0:
                    lista_pares.append(numero)
                else:
                    lista_impares.append(numero)       

            print("\nNúmeros pares:")
            print(lista_pares)  
            print(f"cantidad de numeros pares: {len(lista_pares)}")        
            print("\nNúmeros impares:")
            print(lista_impares)    
            print(f"cantidad de numeros impares: {len(lista_impares)}")
            print("\n#######################################################\n")

        case "4":
            
            list_numeros= [1,3,5,3,7,1,9,5,3]
            list_numeros_sin_repetidos = []

            for nro in list_numeros:
                if nro in list_numeros_sin_repetidos:
                    continue
                list_numeros_sin_repetidos.append(nro) 
            
            print(list_numeros_sin_repetidos)
            print("\n#######################################################\n")

        case "5":
            
            
            estudiantes = ["Juan", "María", "Pedro", "Ana", "Luis"]
            
            # mejor con case, pero se respeta la temas del TP 
            
            modificar_lista = input("¿Desea modificar la lista de estudiantes? (s/n): ").lower()
            
            #verifico el dato
            while not modificar_lista == "s" and not modificar_lista == "n" or modificar_lista == "":
                print("Error: Ingrese 's' para sí o 'n' para no.")
                modificar_lista = input("¿Desea modificar la lista de estudiantes? (s/n): ").lower()
            
            if modificar_lista == "s":
                input ("quiere agregar un nuevo estudiante? (s/n): ").lower( )
                
                #verifico el dato
                while not modificar_lista == "s" and modificar_lista == "n" :
                    print("Error: Ingrese 's' para sí o 'n' para no.")
                    modificar_lista = input("¿Desea modificar la lista de estudiantes? (s/n): ").lower()
                
                # agrego el nuevo estudiante a la lista.

                nuevo_estudiante = input("Ingrese el nombre del nuevo estudiante: ")
                
                #verifico el dato
                
                while not nuevo_estudiante.isalpha() or nuevo_estudiante == "":
                    print("Error: Debe ingresar un nombre válido y solo debe usar letras.")
                    nuevo_estudiante = input("Ingrese el nombre del nuevo estudiante: ")
                
                estudiantes.append(nuevo_estudiante)
                print("Estudiante agregado correctamente.")
            
            borrar_estudiante_lista = input("¿Desea borrar un estudiante de la lista? (s/n): ").lower()

            #verifico el dato
            while  not borrar_estudiante_lista == "s" and not borrar_estudiante_lista == "n" or borrar_estudiante_lista == "":
                print("Error: Ingrese 's' para sí o 'n' para no.")
                borrar_estudiante_lista = input("¿Desea borrar un estudiante de la lista? (s/n): ").lower()


            if borrar_estudiante_lista == "s":
                estudiante_a_borrar = input("Ingrese el nombre del estudiante que desea borrar: ")
                
                #verifico el dato
                while estudiante_a_borrar not in estudiantes:
                    print("Error: El estudiante no se encuentra en la lista.")
                    estudiante_a_borrar = input("Ingrese el nombre del estudiante que desea borrar: ")
                
                estudiantes.remove(estudiante_a_borrar)
                print(f"Estudiante '{estudiante_a_borrar}' eliminado correctamente.")
            
            print("\nLista actualizada de estudiantes:\n")
            print(estudiantes)

            ## ATENCION SI DA EL TIEMPO MEJORAR EL CODIGO
            print("\n#######################################################\n")


        case "6":
            
            list_numeros= [4,8,9,7,5,3]
            print(list_numeros)
            
            # invierto la lista
            list_numeros.reverse() 
            print(list_numeros)
            print("\n#######################################################\n")
        
        case "7":
            #Una matriz es una lista de listas
            #Cada elemento de la matriz es una fila, y cada elemento de la fila es una columna.
            #Creo la matriz con las temperaturas minimas y maximas de una semana.
            
            matriz_temperaturas = [
                [10, 20], 
                [15, 25], 
                [12, 22], 
                [18, 28], 
                [14, 24], 
                [16, 26], 
                [13, 23]
            ]

            lista_nombres_dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"] 
            
            #creo las variables
            promedio_minima_temp= 0
            promedio_maxima_temp= 0
            mayor_amplitud_termica = 0
            
            
            #Recorro la fila

            for fila in matriz_temperaturas:
                promedio_minima_temp += fila[0] 
                promedio_maxima_temp += fila[1]

            promedio_minima_temp /= len(matriz_temperaturas)
            promedio_maxima_temp /= len(matriz_temperaturas)

            print(f"Promedio de temperaturas mínimas: {promedio_minima_temp}")
            print(f"Promedio de temperaturas máximas: {promedio_maxima_temp}")


            # Para obtener el numero de la fila no se puede usar fila porque fila devuelve una matriz
            # pero si se puede usar el indice i al for y usar la funcion enumerate, 
            # para contar las listas de fila en una matriz 
            
            for i,fila in enumerate(matriz_temperaturas):
                
                #Diferencia de Temperaturas Maximas y Minimas
                amplitud_termica = fila[1] - fila[0] 
                
                #Verifico si es la mayor amplitud
                if amplitud_termica > mayor_amplitud_termica:
                    mayor_amplitud_termica = amplitud_termica
                    dia_mayor_amplitud = lista_nombres_dias[i]

                    
            print(f"Mayor amplitud térmica: {mayor_amplitud_termica}")
            print(f"Mayor amplitud térmica fue el dia: {dia_mayor_amplitud}")
            print("\n#######################################################\n")

        case "8":

            matriz_estudiantes_notas = [
                ["Juan", 7, 8, 9],
                ["María", 6, 7, 8],
                ["Pedro", 5, 6, 7],
                ["Ana", 8, 9, 10],
                ["Luis", 4, 5, 6]
            ]

            promedio_estudiantes = []
            

            for fila in matriz_estudiantes_notas:
                nombre_estudiante = fila[0]
                promedio_estudiante = (fila[1] + fila[2] + fila[3]) / 3
                promedio_estudiantes.append([nombre_estudiante, promedio_estudiante])
            
            print("Promedio de cada estudiante:")
            print(promedio_estudiantes)
            
            #Tambien con For, pero como son pocos valores uso esta opcion, si escala es mejor con un for.
            promedio_materia_1= (matriz_estudiantes_notas[1][1] + matriz_estudiantes_notas[2][1] + matriz_estudiantes_notas[3][1]) / 5
            promedio_materia_2=(matriz_estudiantes_notas[1][2] + matriz_estudiantes_notas[2][2] + matriz_estudiantes_notas[3][2]) / 5
            promedio_materia_3= (matriz_estudiantes_notas[1][3] + matriz_estudiantes_notas[2][3] + matriz_estudiantes_notas[3][3]) / 5

            print(
                f"""
                Promedio de cada Materia es:
                ______________________________
                Materia 1: {promedio_materia_1}
                Materia 2: {promedio_materia_2}
                Materia_3: {promedio_materia_3}
                """)
        case "9":
            #Creo el tablero Basico
            tablero = [
                ["-", "-", "-"],
                ["-", "-", "-"],
                ["-", "-", "-"]
            ]
            
            #Solicito al usuario que ingrese la fila
            fila= int(input("Ingrese la fila (0, 1, 2): "))
            # Verifico el dato
            while fila < 0 or fila > 2:
                print("Error: Ingrese un número válido para la fila (0, 1, 2).")
                fila = int(input("Ingrese la fila (0, 1, 2): "))
            
            #solicito al usuario que ingrese la columna
            columna = int(input("Ingrese la columna (0, 1, 2): "))
            # Verifico el dato
            while columna < 0 or columna > 2:
                print("Error: Ingrese un número válido para la columna (0, 1, 2).")
                columna = int(input("Ingrese la columna (0, 1, 2): "))  
            
            #Solicito al usuario que ingrese el valor (X o O)   
            valor= input("Ingrese el valor (X o O): ").upper()
            
            #verifico el dato
            while valor != "X" and valor != "O":
                print("Error: Ingrese un valor válido (X o O).")
                valor = input("Ingrese el valor (X o O): ").upper() 
            
            #Actualizo el tablero con el valor ingresado por el usuario
            tablero[fila][columna] = valor
            
            #Imprimo el tablero actualizado
            print("\nTablero actualizado:\n")
            print("------------------------")
            print(tablero)
            print("")

            #Como no me gusta la representacion del tablero, en pantalla
            #Use esta otra forma
            # Donde el metodo .join() sirve para unir los elementos 
            # de la lista con un separador, en este caso " | " 
            
            for fila in tablero:
                
                print(" | ".join(fila))
            
            
        case "10":
            pass
        case "11":
            pass
        case "12":
            pass
        case "13":
            pass
        case "0":
            break
        case _:
            print("Ingreso un numero invalido")