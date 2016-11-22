"""
Escriba un programa que permita crear dos listas de palabras y que, a continuación, escriba las
siguientes listas (en las que no debe haber repeticiones):
● Lista de palabras que aparecen en las dos listas.
● Lista de palabras que aparecen en la primera lista, pero no en la segunda.
● Lista de palabras que aparecen en la segunda lista, pero no en la primera.
● Lista de palabras que aparecen en ambas listas.
Nota​: Para evitar las repeticiones, el programa deberá empezar eliminando los elementos
repetidos en cada lista.
Dígame cuántas palabras tiene la primera lista: 4
Dígame la palabra 1: Carmen
Dígame la palabra 2: Alberto
Dígame la palabra 3: Benito
Dígame la palabra 4: Carmen
La primera lista es: ['Carmen', 'Alberto', 'Benito', 'Carmen']
Dígame cuántas palabras tiene la segunda lista: 3
Dígame la palabra 1: Benito
Dígame la palabra 2: Juan
Dígame la palabra 3: Carmen
La segunda lista es: ['Benito', 'Juan', 'Carmen']
Palabras que aparecen en las dos listas: ['Carmen', 'Benito']
Palabras que sólo aparecen en la primera lista: ['Alberto']
Palabras que sólo aparecen en la segunda lista: ['Juan']
Todas las palabras: ['Carmen', 'Benito', 'Alberto', 'Juan']
"""


numero1 = int(input("Introduce el numero de elementos en la lista1: "))

lista1 = []
#For con el rango del numero
for i in range (numero1):
	#Se solicita la palabra con un contador str(i+1)
	print("Dime la palabra ", str(i+1) + " :", end="")
	palabra1 = input()
	#Se añade la palabra al array de la lista
	lista1 += [palabra1]
print("La primera lista es: ", lista1)
print("-----------------------------------------")

numero2 = int(input("Introduce el numero de elementos en la lista2: "))

lista2 = []
#For con el rango del numero
for i in range (numero2):
	#Se solicita la palabra con un contador str(i+1)
	print("Dime la palabra ", str(i+1) + " :", end="")
	palabra2 = input()
	#Se añade la palabra al array de la lista
	lista2 += [palabra2]
print("La segunda lista es: ", lista2)
print("-----------------------------------------")	

#Se crea la lista conjunta de ambas listas
lista3 = lista1 + lista2
print("La lista conjunta es: ", lista3)
print("-----------------------------------------")

#Lista que aparecen en lista1 pero no en lista2
lista4 = []
for i in lista1:
	if i not in lista2:
		lista4 = [i] + lista4
print("Lista que solo aparecen el al lista1: ", lista4)
print("-----------------------------------------")

#Lista que aparecen en lista2 pero no en lista1 
lista5 = []
for i in lista2:
	if i not in lista1:
		lista5 = [i] + lista5
print("Lista que solo aparecen el al lista2: ", lista5)
print("-----------------------------------------")

#Palabras que aparecen en ambas listas
lista6 = []
for i in lista1:
	if i in lista2:
		lista6 = [i] + lista6
print("Lista que solo aparecen en ambas listas: ", lista6)
print("-----------------------------------------")
