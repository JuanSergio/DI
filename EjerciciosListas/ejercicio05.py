"""
Escriba un programa que permita crear dos listas de palabras y que, a continuación, elimine de
la primera lista los nombres de la segunda lista.
Dígame cuántas palabras tiene la lista: 5
Dígame la palabra 1: Carmen
Dígame la palabra 2: Carmen
Dígame la palabra 3: Alberto
Dígame la palabra 4: Benito
Dígame la palabra 5: David
La lista creada es: ['Carmen', 'Carmen', 'Alberto', 'Benito', 'David']
Dígame cuántas palabras tiene la lista de palabras a eliminar: 3
Dígame la palabra 1: Benito
Dígame la palabra 2: Juan
Dígame la palabra 3: Carmen
La lista de palabras a eliminar es: ['Benito', 'Juan', 'Carmen']
La lista es ahora: ['Alberto', 'David']
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

#Se crea una lista nueva de elementos a borrar
numero2 = int(input("Introduce el numero de elementos a borrar: "))
#Se recorre el nuevo array
borrar = []
for i in range(numero2):
	print("Dígame la palabra", str(i + 1) + ": ", end="")
palabra2 = input()
borrar += [palabra2]
print("La lista de palabras a eliminar es:", borrar)
#Se borra la posicion final    
for i in borrar:
    for j in range(len(lista)-1, -1, -1):
    	if lista[j] == i:
        	del(lista[j])
print("La lista es ahora:", lista)
