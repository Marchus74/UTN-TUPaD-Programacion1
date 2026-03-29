print ("TRABAJO PRACTICO N° 3 ")


while True:
    print("""
Listado de Ejercicios:
Ejercicio 1: Caja del Kiosco
Ejercicio 2: Acceso al Campus y Menú Seguro
Ejercicio 3: Agenda de Turnos con Nombres (sin listas)
Ejercicio 4: Escape Room: La Bóveda
Ejercicio 5: Escape Room:"La Arena del Gladiador"
""")

    option = input("Elija un ejercicio del 1 al 10, o 0 para salir: ")

    match option:
        case "1":

            # 1.
            #Pedir nombre del cliente 
            nombre_cliente = input("Ingrese su nombre: ")

            while not nombre_cliente.isalpha():
                print("Error: el nombre solo debe contener solo letras")
                nombre_cliente = input("Ingrese su nombre: ")
            
            # 2. 
            # Pedir cantidad de productos 
            cantidad = input("Ingrese la cantidad de productos a comprar: ")

            while not cantidad.isdigit() or int(cantidad) <= 0:
                print("Error: debe ingresar un número entero positivo mayor que 0.")
                cantidad = input("Ingrese la cantidad de productos a comprar: ")

            cantidad = int (cantidad)

            # Acumuladoras de Totales
            total_sin_descuento = 0
            total_con_descuento = 0

            # Lista de los productos

            lista_productos = []


            # 3.
            # Procesar cada producto
            
            for prod in range(1, cantidad + 1):

                # Precio validado
                precio = input(f"Producto {prod} - Ingrese el precio: ")

                while not precio.isdigit():
                    
                    print("Error: el precio debe ser un número ")
                    precio = input(f"Producto {prod} - Ingrese el precio: ")
                
                precio = int(precio)

                total_sin_descuento += precio

                # Descuento validado
                descuento = input("¿Tiene descuento? (S/N): ").lower()

                while descuento not in ("s", "n"):
                    print("Error: debe ingresar S o N.")
                    descuento = input("¿Tiene descuento? (S/N): ").lower()

                # Aplicar descuento si corresponde
                if descuento == "s":
                
                    precio_final = precio * 0.90   # 10% de descuento
                    
                
                else:
                    precio_final = precio
                    
                lista_productos.append({
                    "num": prod,
                    "precio": precio,
                    "descuento": descuento
                })


                
                total_con_descuento += precio_final
            
            # Ingreso el numero del articulo

            # 4. Resultados finales
            ahorro = total_sin_descuento - total_con_descuento
            promedio = total_con_descuento / cantidad

            # Totales
            print()
            print("############################## \n " \
            "Lista Total \n" \
            "#############################")
            print(f"Cliente: {nombre_cliente}")
            print(f"Cantidad de productos: {cantidad}")

            for item in lista_productos:
                print(f"Producto {item['num']} - Precio: {item['precio']}  Descuento (S/N): {item['descuento']}")

            print(f"Total sin descuentos: ${total_sin_descuento}")
            print(f"Total con descuentos: ${total_con_descuento:.2f}")
            print(f"Ahorro: ${ahorro:.2f}")
            print(f"Promedio por producto: ${promedio:.2f}")
            


        case "2":
            
            # Credenciales fijas
            usuario_correcto = "alumno"
            clave_correcta = "python123"

            # -----------------------------
            # 1) LOGIN CON 3 INTENTOS
            # -----------------------------
            
            intentos = 3

            for inten in range(1,intentos+1): #Sera mas legible intentos+1 ???
                
                print(f"Intento {inten}")
                
                usuario = input("Usuario: ")
                clave = input("Clave: ")

                if usuario == usuario_correcto and clave == clave_correcta:
                    print("Acceso concedido.\n")
                    break
                else:
                    print("Error: credenciales inválidas.\n")

            # Esto ocurre despues del for pero si pasa el break se evalua pero dara siempre false    
            
            if usuario != usuario_correcto or clave != clave_correcta:
                print("Cuenta bloqueada.")
        

            # Otra posibilidad con while recordar averiguar que es mas eficiente ???            
            """
            
            intentos = 0
            max_intentos = 3

            while intentos < max_intentos:
                intentos += 1
                print(f"Intento {intentos}/{max_intentos}")
                
                usuario = input("Usuario: ")
                clave = input("Clave: ")

                if usuario == usuario_correcto and clave == clave_correcta:
                    print("Acceso concedido.\n")
                    break
                else:
                    print("Error: credenciales inválidas.\n")

            if intentos == max_intentos and (usuario != usuario_correcto or clave != clave_correcta):
                print("Cuenta bloqueada.")
                exit()  # Termina el programa
            
            """

            # -----------------------------
            # 2 MENÚ PRINCIPAL
            # -----------------------------

            
            
            while True:
                print("1- Estado")
                print("2- Cambiar clave")
                print("3- Mensaje motivacional")
                print("4- Salir")

                # Esto se podia hacer con case tmb!! 

                opcion = input("Opción: ")

                # Validación estricta
                if not opcion.isdigit():
                    print("Error: ingrese un número válido.\n")
                    continue

                opcion = int(opcion)

                if opcion < 1 or opcion > 4:
                    print("Error: opción fuera de rango.\n")
                    continue

                # -----------------------------
                # OPCIONES DEL MENÚ
                # -----------------------------
                
                if opcion == 1:
                    print("Estado de inscripción: Inscripto\n")

                elif opcion == 2:
                    # Cambiar clave
                    nueva = input("Ingrese nueva clave: ")
                    confirm = input("Confirme la nueva clave: ")

                    if len(nueva) < 6:
                        print("Error: la clave debe tener al menos 6 caracteres.\n")
                    elif nueva != confirm:
                        print("Error: las claves no coinciden.\n")
                    else:
                        clave_correcta = nueva
                        print("Clave cambiada con éxito.\n")

                elif opcion == 3:
                    print("Mensaje motivacional: ¡Vamos que faltan 3 no'ma!\n")

                elif opcion == 4:
                    print("Saliendo del sistema...")
                    break

        case "3":



            # -----------------------------
            # 1) Nombre del operador
            # -----------------------------
            operador = input("Ingrese nombre del operador: ")

            while not operador.isalpha():
                print("Error: el nombre solo debe contener letras.")
                operador = input("Ingrese nombre del operador: ")


            # -----------------------------
            # 2) Variables de turnos (sin listas)
            # -----------------------------
            # Se podria hacer con lista, y un for ??? recordar probar si queda tiempo!!
            
            lunes1 = ""
            lunes2 = ""
            lunes3 = ""
            lunes4 = ""

            martes1 = ""
            martes2 = ""
            martes3 = ""

            # -----------------------------
            # 3) MENÚ PRINCIPAL
            # -----------------------------
            while True:
                print("\n--- MENÚ PRINCIPAL ---")
                print("1- Reservar turno")
                print("2- Cancelar turno")
                print("3- Ver agenda del día")
                print("4- Ver resumen general")
                print("5- Cerrar sistema")

                opcion = input("Opción: ")

                if not opcion.isdigit():
                    print("Error: ingrese un número válido.")
                    continue

                opcion = int(opcion)

                if opcion < 1 or opcion > 5:
                    print("Error: opción fuera de rango.")
                    continue


                # -----------------------------
                # 1 RESERVAR TURNO
                # -----------------------------
                

                if opcion == 1:
                    
                    dia = input("Elegir día (1=Lunes, 2=Martes): ")

                    while dia not in ("1", "2"):
                        print("Error: día inválido.")
                        dia = input("Elegir día (1=Lunes, 2=Martes): ")

                    paciente = input("Nombre del paciente: ").strip()

                    while not paciente.isalpha():
                        print("Error: solo letras.")
                        paciente = input("Nombre del paciente: ").strip()

                    # LUNES
                    
                    if dia == "1":
                    
                        if paciente in (lunes1, lunes2, lunes3, lunes4):
                            print("Error: ese paciente ya tiene turno el lunes.")
                        elif lunes1 == "":
                            lunes1 = paciente
                        elif lunes2 == "":
                            lunes2 = paciente
                        elif lunes3 == "":
                            lunes3 = paciente
                        elif lunes4 == "":
                            lunes4 = paciente
                        else:
                            print("No hay más turnos disponibles el lunes.")

                    # MARTES
                    else:
                    
                        if paciente in (martes1, martes2, martes3):
                            print("Error: ese paciente ya tiene turno el martes.")
                        elif martes1 == "":
                            martes1 = paciente
                        elif martes2 == "":
                            martes2 = paciente
                        elif martes3 == "":
                            martes3 = paciente
                        else:
                            print("No hay más turnos disponibles el martes.")


                # -----------------------------
                # 2 CANCELAR TURNO
                # -----------------------------
                
                
                elif opcion == 2:
                    dia = input("Elegir día (1=Lunes, 2=Martes): ")

                    while dia not in ("1", "2"):
                        print("Error: día inválido.")
                        dia = input("Elegir día (1=Lunes, 2=Martes): ")

                    paciente = input("Nombre del paciente a cancelar: ")

                    while not paciente.isalpha():
                        print("Error: solo letras.")
                        paciente = input("Nombre del paciente a cancelar: ")

                    # LUNES
                    
                    if dia == "1":
                        if paciente == lunes1:
                            lunes1 = ""
                        elif paciente == lunes2:
                            lunes2 = ""
                        elif paciente == lunes3:
                            lunes3 = ""
                        elif paciente == lunes4:
                            lunes4 = ""
                        else:
                            print("Ese paciente no tiene turno el lunes.")

                    # MARTES
                    
                    else:
                        if paciente == martes1:
                            martes1 = ""
                        elif paciente == martes2:
                            martes2 = ""
                        elif paciente == martes3:
                            martes3 = ""
                        else:
                            print("Ese paciente no tiene turno el martes.")


                # -----------------------------
                # 3 VER AGENDA DEL DÍA
                # -----------------------------
                
                elif opcion == 3:
                    dia = input("Elegir día (1=Lunes, 2=Martes): ")

                    while dia not in ("1", "2"):
                        print("Error: día inválido.")
                        dia = input("Elegir día (1=Lunes, 2=Martes): ")

                    if dia == "1":
                        print("")
                        print("AGENDA DIA LUNES")
                        print("Primer Turno:", "Libre" if lunes1 == "" else "Asignado")
                        print("Segundo Turno:", "Libre" if lunes2 == "" else "Asignado")
                        print("Tercer Turno:", "Libre" if lunes3 == "" else "Asignado")
                        print("Cuarto Turno:", "Libre" if lunes4 == "" else "Asignado")
                        
                    else:
                        print("")
                        print("AGENDA DIA MARTES")
                        print("Primer Turno:", "Libre" if martes1 == "" else "Asignado")
                        print("Segundo Turno:", "Libre" if martes2 == "" else "Asignado")
                        print("Tercer Turno:", "Libre" if martes3 == "" else "Asignado") 

                # -----------------------------
                # 4) RESUMEN GENERAL
                # -----------------------------
                
                elif opcion == 4:
                    
                    # Partiendo de todos Ocupados hace que cualqier modificacion en la variable cuente
                    ocupados_lunes = (lunes1 != "") + (lunes2 != "") + (lunes3 != "") + (lunes4 != "")
                    ocupados_martes = (martes1 != "") + (martes2 != "") + (martes3 != "")

                    print("\n--- RESUMEN GENERAL ---")
                    print(f"Lunes: {ocupados_lunes} ocupados / {4 - ocupados_lunes} libres")
                    print(f"Martes: {ocupados_martes} ocupados / {3 - ocupados_martes} libres")

                    if ocupados_lunes > ocupados_martes:
                        print("Día con más turnos: Lunes")
                    elif ocupados_martes > ocupados_lunes:
                        print("Día con más turnos: Martes")
                    else:
                        print("Hay un empate en cantidad de turnos.")

                # -----------------------------
                # 5) SALIR
                # -----------------------------
                elif opcion == 5:
                    print("Sistema cerrado.")
                    break


        case "4":

            # -----------------------------
            # VARIABLES INICIALES
            # -----------------------------
            energia = 100
            tiempo = 12
            cerraduras_abiertas = 0
            alarma = False
            codigo_parcial = ""
            cantidad_intentos = 0   # Para la regla anti-spam arranca con 1?
            
            # -----------------------------
            # VALIDAR NOMBRE DEL AGENTE
            # -----------------------------
            agente = input("Ingrese su nombre agente: ")

            while not agente.isalpha():
                print("Error: el nombre solo debe contener letras.")
                agente = input("Ingrese nombre del agente: ")

            print(f"\nBienvenido agente {agente}. Comienza la misión.\n")

            # -----------------------------
            # MENU PRINCIPAL DEL JUEGO
            # -----------------------------
            # Condicion para seguir jugando 
            while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not (alarma and tiempo <= 3):

                print("\n--- ESTADO ACTUAL ---")
                print(f"Energía: {energia}")
                print(f"Tiempo: {tiempo}")
                print(f"Cerraduras abiertas: {cerraduras_abiertas}")
                print(f"Alarma: {'ACTIVA' if alarma else 'Desactivada'}")
                print("----------------------")

                print("1. Forzar cerradura (-20 energía, -2 tiempo)")
                print("2. Hackear panel (-10 energía, -3 tiempo)")
                print("3. Descansar (+15 energía, -1 tiempo)")
                
                opcion = input("Elija opción: ")

                # Validación del menú
                if not opcion.isdigit():
                    print("Error: ingrese un número válido.")
                    continue

                opcion = int(opcion) #RECORDAR: Pasa a Int despues de isdigit!!!

                if opcion < 1 or opcion > 3:
                    print("Error: opción fuera de rango.")
                    continue

                # -----------------------------
                # OPCIÓN 1: FORZAR CERRADURA
                # -----------------------------
                
                if opcion == 1:
                    print("\n Eligio forzar cerradura\n")
                    
                    energia = energia - 20
                    tiempo  = tiempo - 2
                    cantidad_intentos = cantidad_intentos + 1

                    # Regla anti-spam
                    if cantidad_intentos == 3:
                        print("¡La cerradura se trabó por forzarla 3 veces seguidas!")
                        alarma = True
                        cantidad_intentos = 0 # No olvidar Reset!!!
                        continue

                    # Riesgo de alarma si energía < 40
                    if energia < 40:
                        print("Energía baja: riesgo de activar alarma.")
                        num = input("Ingrese un número del 1 al 3: ")

                        while not num.isdigit() or int(num) not in (1, 2, 3):
                            print("Error: debe ingresar un número entre 1 y 3.")
                            num = input("Ingrese un número del 1 al 3: ")

                        if int(num) == 3:
                            print("¡La alarma se activó!")
                            alarma = True

                    # Si no hay alarma, se abre la cerradura
                    if not alarma:
                        cerraduras_abiertas += 1
                        print("Cerradura forzada con éxito.")

                # -----------------------------
                # OPCIÓN 2: HACKEAR PANEL
                # -----------------------------
                
                elif opcion == 2:

                    energia = energia -10
                    tiempo = tiempo -3
                    cantidad_intentos = 0  # Se corta la racha

                    print("Hackeando panel...")
                    for i in range(1,3+1):
                        print(f"Progreso {i}")
                        codigo_parcial += "A"

                    print(f"Código parcial: {codigo_parcial}")

                    if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
                        cerraduras_abiertas += 1
                        print("¡Hackeo exitoso! Se abrió una cerradura.")

                # -----------------------------
                # OPCIÓN 3: DESCANSAR
                # -----------------------------
                elif opcion == 3:
                    tiempo = tiempo - 1
                    cantidad_intentos = 0  # Se corta la racha

                    energia += 15
                    if energia > 100:
                        energia = 100

                    if alarma:
                        energia = energia - 10
                        print("La alarma está activa: pierdes 10 energía extra.")

                    print("Descansaste y recuperaste energía.")


            # -----------------------------
            # CONDICIONES DE FIN
            # -----------------------------
            print("\n--- FIN DE LA MISIÓN ---")

            if cerraduras_abiertas == 3:
                print("¡VICTORIA! Abriste la bóveda a tiempo.")
            elif energia <= 0:
                print("DERROTA: Te quedaste sin energía.")
            elif tiempo <= 0:
                print("DERROTA: Se acabó el tiempo.")
            elif alarma and tiempo <= 3:
                print("DERROTA: El sistema se bloqueó por alarma.")
            else:
                print("DERROTA: Condición desconocida.")

        case "5":
            
            print("--- BIENVENIDO A LA ARENA ---")

            # ============================
            # 1. VALIDAR NOMBRE DEL GLADIADOR
            # ============================
            nombre = input("Nombre del Gladiador: ")

            while not nombre.isalpha():
                print("Error: Solo se permiten letras.")
                nombre = input("Nombre del Gladiador: ")

            print(f"\n=== INICIO DEL COMBATE, {nombre.upper()} ===")

            # ============================
            # 2. VARIABLES INICIALES
            # ============================
            vida_jugador = 100
            vida_enemigo = 100
            pociones = 3
            ataque_pesado = 15
            ataque_enemigo = 12
            turno_jugador = True   # booleano 

            # ============================
            # 3. CICLO DE COMBATE
            # ============================
            while vida_jugador > 0 and vida_enemigo > 0: #vida de los dos jugadores

                print(f"\n{nombre} (HP: {vida_jugador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")
                print("Elige acción:")
                print("1. Ataque Pesado")
                print("2. Ráfaga Veloz")
                print("3. Curar")

                opcion = input("Opción: ")

                # Validación estricta del menú
                while not opcion.isdigit():
                    print("Error: Ingrese un número válido.")
                    opcion = input("Opción: ")

                opcion = int(opcion)

                while opcion not in (1, 2, 3):
                    print("Error: Opción fuera de rango.")
                    opcion = input("Opción: ")
                    while not opcion.isdigit():
                        print("Error: Ingrese un número válido.")
                        opcion = input("Opción: ")
                    opcion = int(opcion)

                # ============================
                # ACCIÓN 1: ATAQUE PESADO
                # ============================
                if opcion == 1:
                    if vida_enemigo < 20:
                        daño = ataque_pesado * 1.5   # float crítico
                        print(f">> ¡GOLPE CRÍTICO! Daño aumentado a {daño:.1f}")
                    else:
                        daño = ataque_pesado

                    vida_enemigo -= daño
                    print(f"¡Atacaste al enemigo por {daño:.1f} puntos de daño!")

                # ============================
                # ACCIÓN 2: RÁFAGA VELOZ (for obligatorio)
                # ============================
                elif opcion == 2:
                    print(">> ¡Inicias una ráfaga de golpes!")
                    for i in range(3):
                        vida_enemigo -= 5
                        print("> Golpe conectado por 5 de daño")

                # ============================
                # ACCIÓN 3: CURAR
                # ============================
                elif opcion == 3:
                    if pociones > 0:
                        vida_jugador += 30
                        pociones -= 1
                        print(">> ¡Te curaste 30 puntos de vida!")
                        if vida_jugador > 100:
                            vida_jugador = 100
                    else:
                        print("¡No quedan pociones!")

                # ============================
                # ATAQUE AUTOMÁTICO DEL ENEMIGO
                # ============================
                if vida_enemigo > 0:  # Solo ataca si sigue vivo
                    vida_jugador -= ataque_enemigo
                    print(f">> ¡El enemigo te atacó por {ataque_enemigo} puntos!")

                print("=== NUEVO TURNO ===")

            # ============================
            # 4. FIN DEL JUEGO
            # ============================
            print("\n--- FIN DEL COMBATE ---")

            if vida_jugador > 0:
                print(f"¡VICTORIA! {nombre} ha ganado la batalla.")
            else:
                print("DERROTA. Has caído en combate.")

            
        case "0":
            break
        case _:
            print("Ingreso un numero invalido")


