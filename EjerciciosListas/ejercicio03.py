"""Escriba un programa que permita crear una lista de palabras y que, a continuación, pida dos
palabras y sustituya la primera por la segunda en la lista.
Dígame cuántas palabras tiene la lista: 4
Dígame la palabra 1: Alberto
Dígame la palabra 2: Carmen
Dígame la palabra 3: Benito
Dígame la palabra 4: Carmen
La lista creada es: ['Alberto', 'Carmen', 'Benito', 'Carmen']
Sustituir la palabra: Carmen
por la palabra: David
La lista es ahora: ['Alberto', 'David', 'Benito', 'David']
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Se pide un numero de tamaño de la lista
numero = int(input("Introduce el numero de elementos en la lista: "))

#Se crea la lista	
lista = []
#For con el rango del numero
for i in range (numero):
	#Se solicita la palabra con un contador str(i+1)
	print("Dime la palabra ", str(i+1) + " :", end="")
	palabra = input()
	#Se añade la palabra al array de la lista
	lista += [palabra]
print("La lista es: ", lista)
	
cambiar = input("Dime la palabra a cambiar: ")
sustituir = input("Dime la palabra a sustituir: ")
#El comando index encuantra la posicion de la cambiar
num = lista.index(cambiar)
lista[num] = sustituir
print("La nueva lista es: "lista)		
		
