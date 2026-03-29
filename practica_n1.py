# Ejercicio 1
print("Hola Mundo!!!!!!")

# Ejercicio 2
"""
Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando 
el nombre ingresado.
"""

nombre = input("Por favor ingrese su nombre: ")
print(f"Hola {nombre}, ¿en qué te podemos ayudar hoy?")

# Ejercicio 3
"""
Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e 
imprima por pantalla una oración con los datos ingresados.
"""

nombre = input("Por favor ingrese su nombre: ")
apellido = input("Por favor ingrese su apellido: ")
edad = int(input("Por favor ingrese su edad: "))
pais = input("Por favor ingrese su país de residencia: ")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {pais}.")

# Ejercicio 4
"""
Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y 
su perímetro.
"""

radio = float(input("Por favor ingrese el radio del círculo: "))
pi = 3.14

area = pi * (radio ** 2)
perimetro = 2 * pi * radio

print(f"El área del círculo es {area}")
print(f"El perímetro del círculo es {perimetro}")

# Ejercicio 5
"""
Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a 
cuántas horas equivale.
"""

segundos = int(input("Por favor ingrese una cantidad entera de segundos: "))
hora_segundos = 3600

print(f"La cantidad de horas equivalentes es {segundos // hora_segundos}")

# Ejercicio 6
"""
Crear un programa que pida al usuario un número e imprima por pantalla la tabla de 
multiplicar de dicho número.
"""

numero = int(input("Por favor ingrese un número entero: "))
print("La tabla de multiplicar de ese número es:")

print(f"1 x {numero} = {1 * numero}")
print(f"2 x {numero} = {2 * numero}")
print(f"3 x {numero} = {3 * numero}")
print(f"4 x {numero} = {4 * numero}")
print(f"5 x {numero} = {5 * numero}")
print(f"6 x {numero} = {6 * numero}")
print(f"7 x {numero} = {7 * numero}")
print(f"8 x {numero} = {8 * numero}")
print(f"9 x {numero} = {9 * numero}")
print(f"10 x {numero} = {10 * numero}")

# Ejercicio 7
"""
Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por 
pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
"""

numero1 = int(input("Por favor ingrese un número entero distinto de 0: "))
numero2 = int(input("Por favor ingrese otro número entero distinto de 0: "))

print(f"La suma de {numero1} y {numero2} es {numero1 + numero2}")
print(f"La división de {numero1} y {numero2} es {numero1 / numero2}")
print(f"La multiplicación de {numero1} y {numero2} es {numero1 * numero2}")
print(f"La resta de {numero1} y {numero2} es {numero1 - numero2}")

# Ejercicio 8
"""
Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice 
de masa corporal.
"""

peso = float(input("Por favor ingrese su peso en kg: "))
altura = float(input("Por favor ingrese su altura en metros: "))

print(f"Su índice de masa corporal (IMC) es {peso / (altura ** 2)}")

# Ejercicio 9
"""
Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por 
pantalla su equivalente en grados Fahrenheit.
"""

temperatura = float(input("Por favor ingrese la temperatura en grados Celsius: "))
equivalente_fahrenheit = (9 / 5) * temperatura + 32

print(f"La temperatura equivalente en grados Fahrenheit es: {equivalente_fahrenheit}")

# Ejercicio 10
"""
Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de 
dichos números.
"""

numero1 = float(input("Por favor ingrese el primer número: "))
numero2 = float(input("Por favor ingrese el segundo número: "))
numero3 = float(input("Por favor ingrese el tercer número: "))

print(f"El promedio de los 3 números es: {(numero1 + numero2 + numero3) / 3}")

