"""
Escriba un programa que pida un número y a continuación escriba la lista de todos los números
primos hasta él..
Dígame un número: 100
Primos hasta 100: 1 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97
"""
print("Introduce un numero")
numero = int(input())
lista = []

for i in range (numero+1):
	acumulador=0
	#calcular los divisores que introducimos
	num=1
	
	while (num <=i):
		#Se agrega si es divisible por si mismo
		if (i%num==0):
			acumulador+=1
			num+=1
		else:
			num+=1
	if(i != 0):
		if(acumulador <= 2):
			lista.append(i)
print("Los numeros primos de ", numero, " son: ", lista)	
	
