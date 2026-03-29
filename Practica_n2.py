print ("TRABAJO PRACTICO N° 2 ")


while True:
    


    option = input("Elija un ejercicio del 1 al 10, o 0 para salir: ")

    match option:
        
        case "1":
            print("""Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, 
deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.  """)
            edad = int(input("ingrese su edad: "))
            if edad > 18:
                print ("Usted es Mayor de Edad")
        
        case "2":
            print(""" Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá 
mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el 
mensaje “Desaprobado”.  """)
            nota = int(input(" Ingresa cual fue su nota: "))
            if nota >=6 :
                print ("Usted A Aprobado!!!")
            else:
                print ("Usted A Desaprobado")
        
        case "3":
            print("""Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un 
número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso 
contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del 
operador de módulo (%) en Python para evaluar si un número es par o impar. """)
            numero= int (input(" Ingrese un numero Par: "))
            if numero % 2 == 0:
                print ("Usted Ingreso un numero correcto")
            else:
                ("Usted ingreso un numero Impar")
            
        case "4":
            print (""" Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las 
siguientes categorías pertenece:  
• Niño/a: menor de 12 años.  
• Adolescente: mayor o igual que 12 años y menor que 18 años.  
• Adulto/a joven: mayor o igual que 18 años y menor que 30 años.  
• Adulto/a: mayor o igual que 30 años.  """)
            edad = int(input ("Por favor Ingrese su edad:"))
            if edad < 12:
                print (" Ustede es Niño/a")
            elif 12 >= edad < 18:
                print ("Ustede es adolecente")
            elif 18 >= edad < 30:
                print ("Ustede es adulto/a Joven")
            elif edad > 30:
                print ("Ustede es Mayor")
            else:
                print ("ingreso un valor invalido")
        
        case "5":
            print ("""Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres 
(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en 
pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por 
pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres".""")
            password = input("ingrese una contra seña de al menos 8 caracteres y no mas de 14 :")
            largo_pass = len (password)
            if 8 <= largo_pass <= 14 : 
                print ("Su contraseña se creo con exito")
            else:
                print ("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
        
        case "6":
            print ("""Escribir un programa que solicite al usuario el consumo mensual de energía eléctrica en 
kilovatios (kWh) e indique la categoría del consumo según el siguiente criterio: 
• Menor que 150 kWh: “Consumo bajo”. 
• Entre 150 y 300 kWh (inclusive): “Consumo medio”. 
• Mayor que 300 kWh: “Consumo alto”. 
Además, si el consumo supera los 500 kWh, mostrar un mensaje adicional que diga: 
“Considere medidas de ahorro energético”. 
El programa debe imprimir por pantalla la categoría correspondiente.""")
            consumo= int(input("ingrese su consumo mensual en Kwh:"))
            
            if consumo < 150:
                print ("Consumo Bajo")
            elif 150 <= consumo <= 300:
                print ("consumo Medio")
            elif consumo > 300:
                print("Consumo alto")
                if consumo > 500:
                    print("Considere medidas de ahorro energético")
            else:
                print ("ingreso un valor invalido")

        case "7":
            print("""Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado 
termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por 
pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por 
pantalla.""")
            print("""Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado 
termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por 
pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por 
pantalla.""")

            string_a_evaluar = input("Ingrese una frase o una palabra: ")
            ultima_letra = string_a_evaluar[-1]
            vocales = "aeiouAEIOU"

            if ultima_letra in vocales:
                print(f"{string_a_evaluar}!")
            else:
                print(string_a_evaluar)

        case "8":
            print("""Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 
dependiendo de la opción que desee:  
1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.  
2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.  
3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.  
El programa debe transformar el nombre ingresado de acuerdo con la opción seleccionada por 
el usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), 
lower() y title() de Python para convertir entre mayúsculas y minúsculas.""")
            
            nombre= input ("Por Favor Ingrese su nombre :")
            option = int(input(
            "Elija una opción:\n"
            "1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.\n"
            "2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.\n"
            "3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.\n"
            ))
            
            if option ==1:
                print (nombre.upper())
            elif option == 2 :
                print (nombre.lower())
            elif option == 3:
                print (nombre.capitalize())
            else: 
                print ("Ingreso  Invalido")                


        case "9":
            print ("""Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la 
magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado 
por pantalla:  
• Menor que 3: "Muy leve" (imperceptible).  
• Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).  
• Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero 
generalmente no causa daños).  
• Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras 
débiles).  
• Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).  
• Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).  """)
            
            magnitud = float (input("Ingrese el valor de la magnitud del terremoto: "))

            if magnitud < 3:
                print("Muy leve (imperceptible)")
            elif 3 <= magnitud < 4:
                print("Leve (ligeramente perceptible)")
            elif 4 <= magnitud < 5:
                print("Moderado (sentido por personas, pero generalmente no causa daños)")
            elif 5 <= magnitud < 6:
                print("Fuerte (puede causar daños en estructuras débiles)")
            elif 6 <= magnitud < 7:
                print("Muy fuerte (puede causar daños significativos)")
            elif magnitud >= 7:
                print("Extremo (puede causar graves daños a gran escala)")
            else:
                print("Valor inválido")

        case "10":
            print ("""Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes 
del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla 
si el usuario se encuentra en otoño, invierno, primavera o verano.""")
            hemisferio = input("¿En qué hemisferio se encuentra? (N/S): ").upper()
            mes = int(input("Ingrese el número del mes (1-12): "))
            dia = int(input("Ingrese el día del mes: "))

            if hemisferio not in ("N", "S"):
                print("Hemisferio inválido")
            else:
                # PRIMAVERA / VERANO / OTOÑO / INVIERNO según hemisferio
                if hemisferio == "N":  # HEMISFERIO NORTE
                    if (mes == 3 and dia >= 21) or (mes in (4, 5)) or (mes == 6 and dia <= 20):
                        estacion = "Primavera"
                    elif (mes == 6 and dia >= 21) or (mes in (7, 8)) or (mes == 9 and dia <= 20):
                        estacion = "Verano"
                    elif (mes == 9 and dia >= 21) or (mes in (10, 11)) or (mes == 12 and dia <= 20):
                        estacion = "Otoño"
                    else:
                        estacion = "Invierno"

                else:  # HEMISFERIO SUR
                    if (mes == 9 and dia >= 21) or (mes in (10, 11)) or (mes == 12 and dia <= 20):
                        estacion = "Primavera"
                    elif (mes == 12 and dia >= 21) or (mes in (1, 2)) or (mes == 3 and dia <= 20):
                        estacion = "Verano"
                    elif (mes == 3 and dia >= 21) or (mes in (4, 5)) or (mes == 6 and dia <= 20):
                        estacion = "Otoño"
                    else:
                        estacion = "Invierno"

                print(f"Usted se encuentra en {estacion}.")

        case _:
            print("Ingreso un numero invalido")

