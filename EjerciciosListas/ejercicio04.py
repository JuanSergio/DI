"""
Escriba un programa que permita crear una lista de palabras y que, a continuación, pida una
palabra y elimine esa palabra de la lista.
Dígame cuántas palabras tiene la lista: 4
Dígame la palabra 1: Alberto
Dígame la palabra 2: Carmen
Dígame la palabra 3: Carmen
Dígame la palabra 4: Benito
La lista creada es: ['Alberto', 'Carmen', 'Carmen', 'Benito']
Palabra a eliminar: Carmen
La lista es ahora: ['Alberto', 'Benito']
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
borrar = input("Dígame la palabra a borrar: ")
#Bucle que recorra la lista buscando la palbra a borrar
for i in range(len(lista) -1, -1, -1):
	if lista[i]==borrar:
		del (lista[i])
print ("La nueva lista: ", lista)
