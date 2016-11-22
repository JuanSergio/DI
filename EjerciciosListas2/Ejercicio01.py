"""
Escriba un programa que permita crear una lista de palabras y que, a continuación, ordene la
lista por orden alfabético.
Dígame cuántas palabras tiene la lista: 4
Dígame la palabra 1: Carmen
Dígame la palabra 2: Alberto
Dígame la palabra 3: Daniel
Dígame la palabra 4: Benito
La lista creada es: ['Carmen', Alberto', 'Daniel', 'Benito']
La lista odenada es: ['Alberto', 'Benito', 'Carmen', 'Daniel']
"""
#!/usr/bin/env python
numero = int(input("Digame cuántas palabras tiene la lista: "))

lista = []
for i in range(numero):
	# str transforma los datos en una cadena, traduciendo 
	# traduciendo lo que hay en la posicion
	print("Di la palabra", str(i+1)+ ": ", end="")
	# Se introduce la palabra
	palabra = input()
	# La palabra entra en el array
	lista += [palabra]
	lista.sort()
print("La lista creada es: ", lista)
