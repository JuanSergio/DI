
"""
Escriba un programa que calcule términos de la sucesión U​ n+1​ = 3 U​ n​ + 1 si U​ n​ es impar y U ​ n+1​ =
U​ n​ / 2 si U​ n​ es par. El programa tiene que pedir el término U​ 0​ y el número de términos a calcular.
Cálculo de términos de la sucesión U(n+1)=3.U(n)+1 si n es impar y U(n)=U(n)/2 si n es par.
Dígame el valor de U(0): 7
Dígame cuántos términos quieres: 20
Los términos de la sucesión son: [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1, 4, 2,
1]
Nota: La​ ​ conjetura de Collatz​ establece que esta sucesión alcanza el valor 1 para cualquier
valor inicial. Desde 1937, esta conjetura permanece sin demostrar
"""
#!/usr/bin/env python
print("Introduce el primer termino de sucesion: ")
termino1 = int(input())

print("Di cuantos terminos de la sucesion quieres: ")
termino2 = int(input())

#Se crea la lista
lista = []
#Se agrega la cantidad de terminos
lista.append(termino2)
for i in range(termino2):
	#Si el numero es impar lo añade
	if termino1%2!=0:
		termino1=int(3*termino1+1)
		lista.append(termino1)
	elif termino2%2==0:
		#Si es par añade el anterior
		termino1=int(termino1/2)
		lista.append(termino1)
print("Los terminos de sucesion son: ", lista)	
