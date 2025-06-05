
""" variables con nombre, edad, altura y si eres estudiante (booleano).

    Imprime su tipo con type().

    Prueba la función str() para convertir tu edad en texto y concatenarla:

    print("Tengo " + str(edad) + " años") 
    
    Uso de F"" para llamar variables con "{}"""
    

# Tipos de datos
nombre = "Devilwertor"
edad = 18
altura = 1.75
es_estudiante = True

print(type(nombre))
print(type(edad))
print(type(altura))
print(type(es_estudiante))

print(type(f"{str(edad)}"))


"""Pide al usuario: nombre, edad y ciudad.

    Imprime una presentación como:

Hola, me llamo [nombre], tengo [edad] años y soy de [pais]."""


nombre_1 = input("Nombre\n")
edad_1 = int(input("Edad\n"))
pais_1= input("Pais\n")

print(f"Hola, Me llamo {nombre_1}, tengo {edad_1} años y soy de {pais_1}")


#Suma 5 años a la edad introducida:

print(f"En 5 años tendras {edad_1 + 5}")

#Entender cómo hacer operaciones y comparaciones.

a = 10
b = 20

print("Suma:", a + b)
print("Resta:", a - b)
print("Multiplicación:", a * b)
print("División:", a / b)
print("División entera:", a // b)
print("Módulo:", a % b)
print("Potencia:", a ** b)

print("¿a es mayor que b?", a > b)


"""Crear un programa que pida dos números y muestre:

        Suma, resta, multiplicación, división y módulo.

    Hacer una comparación:

        ¿El primer numero es mayor?

        ¿Son iguales?

        ¿La diferencia es mayor que 5?
        
        ¿Si una Salchipapa es mas grande que mi cabeza, sera malo si lo intento comer todo?
"""
a_1 = int(input(f"Un numero parcero"))
a_2 = int(input(f"otro numero papanatas"))


suma = a_1 + a_2
resta = a_1 - a_2
multiplicacion = a_1 * a_2
division = a_1 / a_2
modulo = a_1 % a_2



print(f"El resultado es:\nSuma= {suma}\nResta = {resta}\nMultiplicacion = {multiplicacion}\nDivision = {division}\nModulo = {modulo}")

#Tomar decisiones con condiciones.

fifa_es_una_cagada = input("Deci si o no pete: ¿Tu mama te ama?\n")
if fifa_es_una_cagada == "si":
	print("Que bien. No fumes droga que es mala, mejor una pepsi y pan bimbo")
elif fifa_es_una_cagada == "no":
	print("Agarra la pala que vamos pa la mina")

"""Me fume 8 horas de clases para aprender lo de las condiciones, vamos que podemos, Aguante la salchipapa!!!!!!!!!!!!!"""


#agrega un valor a la variable "peso" y agrega "float" para poder mostrar decimales en el codigo. ↓

peso = float(input("Ingresa tu peso en kg: "))

#agrega un valor a la varible "altura" ↓

altura = float(input("Ingresa tu altura en metros: "))

#agrega un valor a la varible "imc" el cual es dividir el peso por la altura elevada al cuadrado (creo XD) ↓
 
imc = peso / (altura**2)

if imc >= 40: 
	print (f"tu IMC es {imc:.2f} (Obesidad III)ve un especilista urgentemente!") #si el imc es mayor a 40 esta linea se mostrara

elif imc >= 35.0 and imc <= 39.9:
	print (f"tu IMC es {imc:.2f} (Obesidad II)ve a un especialista") #si el imc es menor 39.9 pero mayor a 35.0 esta linea se mostrara

elif imc >= 30.0 and imc <= 34.9:
	print (f"tu IMC es {imc:.2f} (Obesidad I)las salchipapas estan muy ricas, pero son malas si comes muchas!")  #si el imc es menor 34.9 pero mayor a 30.0 esta linea se mostrara

elif  imc >= 25.0 and imc <= 29.9:
	print (f"tu IMC es {imc:.2f} (Sobrepeso) come menos salchipapas") #si el imc es maoyor a 25.0 pero menor a 29.9 esta linea se mostrara

elif imc >= 18.6 and imc <= 24.9:
	print (f"tu IMC es {imc:.2f} (peso normal), estas bien!") #si el imc es menor 24.9 pero mayor a 18.6 esta linea se mostrara

elif imc <= 18.15:
	print (f"tu IMC es {imc:.2f} (Bajo Peso),comete una salchipapa") #si el imc es menor 18.15




