"""
Escriba un programa que pida un número y a continuación escriba la lista de todos los divisores
del número (incluidos el uno y él mismo).
Dígame un número: 36
36 tiene 9 divisores: [1, 2, 3, 4, 6, 9, 12, 18, 36]
Dígame un número: 125
125 tiene 4 divisores: [1, 5, 25, 125]
"""
#!/usr/bin/env python
numero = int(input("Dime un numero: "))
# +1 añade ser divisible por sí mismo 
for i in range (1, numero + 1): 
	if (numero%i == 0): 
		print (i)
