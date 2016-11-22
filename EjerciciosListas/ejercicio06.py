"""
Escriba un programa que permita crear una lista de palabras y que, a continuación, cree una
segunda lista igual a la primera, pero al revés (no se trata de escribir la lista al revés, sino de
crear una lista distinta).
Dígame cuántas palabras tiene la lista: 4
Dígame la palabra 1: Alberto
Dígame la palabra 2: Carmen
Dígame la palabra 3: Benito
Dígame la palabra 4: Daniel
La lista creada es: ['Alberto', 'Carmen', 'Benito', 'Daniel']
La lista inversa es: ['Daniel', 'Benito', 'Carmen', 'Alberto']
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
#Se crea nueva lista inversa
lista2 = []
j = 0
#Posicion final y dos indices que recorran ambas listas
for i in range(len(lista)-1,-1,-1):
	lista2[0:j] += [str(lista[i])]
	j += 1	
print ("La nueva lista inversa es: "lista2)
