"""
Escriba un programa que permita crear una lista de palabras. Para ello, el programa tiene que
pedir un número y luego solicitar ese número de palabras para crear la lista. Por último, el
programa tiene que escribir la lista.
Dígame cuántas palabras tiene la lista: 3
Dígame la palabra 1: Alberto
Dígame la palabra 2: Benito
Dígame la palabra 3: Carmen
La lista creada es: ['Alberto', 'Benito', 'Carmen']
Dígame cuántas palabras tiene la lista: 0
¡Imposible!
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
	#Se imprime la lista final
print("La lista es: ", lista)
	
	
	
	
