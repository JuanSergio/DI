"""
Escriba un programa que permita crear una lista de palabras y que, a continuación, elimine los
elementos repetidos (dejando únicamente el primero de los elementos repetidos).
Dígame cuántas palabras tiene la lista: 4
Dígame la palabra 1: Alberto
Dígame la palabra 2: Carmen
Dígame la palabra 3: Benito
Dígame la palabra 4: Carmen
La lista creada es: ['Alberto', 'Carmen', 'Benito', 'Carmen']
La lista sin repeticiones es: ['Alberto', 'Carmen', 'Benito']
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
numero = int(input("Introduce el numero de elementos en la lista1: "))

lista = []
#For con el rango del numero
for i in range (numero):
	#Se solicita la palabra con un contador str(i+1)
	print("Dime la palabra ", str(i+1) + " :", end="")
	palabra = input()
	#Se añade la palabra al array de la lista
	lista += [palabra]
print("La lista es: ", lista)

for i in range(len(lista)-1,-1,-1):
	#Si existe una coincidencia de palabras se borrara una
	if(lista[i] in lista[:i]):
		del(lista[i])	
print ("La nueva lista es: ", lista)
