"""
Escriba un programa que permita crear una lista de palabras y que, a continuación, pida una
palabra y diga cuántas veces aparece esa palabra en la lista.
Dígame cuántas palabras tiene la lista: 4
Dígame la palabra 1: Carmen
Dígame la palabra 2: Alberto
Dígame la palabra 3: Benito
Dígame la palabra 4: Carmen
La lista creada es: ['Carmen', 'Alberto', 'Benito', 'Carmen']
Dígame la palabra a buscar: Carmen
La palabra 'Carmen' aparece 2 veces en la lista.
Dígame cuántas palabras tiene la lista: 4
Dígame la palabra 1: Carmen
Dígame la palabra 2: Alberto
Dígame la palabra 3: Benito
Dígame la palabra 4: Carmen
La lista creada es: ['Carmen', 'Alberto', 'Benito', 'Carmen']
Dígame la palabra a buscar: Alberto
La palabra 'Alberto' aparece una vez en la lista.
Dígame cuántas palabras tiene la lista: 4
Dígame la palabra 1: Carmen
Dígame la palabra 2: Alberto
Dígame la palabra 3: Benito
Dígame la palabra 4: Carmen
La lista creada es: ['Carmen', 'Alberto', 'Benito', 'Carmen']
Dígame la palabra a buscar: David
La palabra 'David' no aparece en la lista.
"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Se pide un numero de tamaño de la lista
numero = int(input("Introduce el numero de elementos en la lista: "))

lista = []
#For con el rango del numero
for i in range (numero):
	#Se solicita la palabra con un contador str(i+1)
	print("Dime la palabra ", str(i+1) + " :", end="")
	palabra = input()
	#Se añade la palabra al array de la lista
	lista += [palabra]
print("La lista es: ", lista)
	
#Se añade la funcion de buscar con un contador
buscar = input("Dígame la palabra a buscar: ")
contador = 0
#Bucle que recorra la lista con la funcion buscar
for i in lista:
	if i == buscar:
		contador +=1;
	#Resultado según el numero de coincidencias		
	if contador == 1:
		print("La palabra: " + buscar + " aparece una vez")
	elif contador == 0:
		print("La palabra: " + buscar + " no aparece")
	else:
		print("La palabra: " + buscar + ", " + "aparece " + contador + " veces")
		
		


