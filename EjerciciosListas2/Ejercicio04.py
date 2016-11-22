"""
Escriba un programa que calcule términos de una sucesión del tipo U​ n+1​ = a U​ n​ + b. El programa
tiene que pedir el valor de a, de b y del término U​ 0​ y el número de términos a calcular.
Cálculo de términos de una sucesión U(n+1)=a.U(n)+b.
Dígame el valor de a: 2
Dígame el valor de b: -1
Dígame el valor de U(0): 3
Dígame cuántos términos quieres: 8
Los términos de la sucesión son: [3, 5, 9, 17, 33, 65, 129, 257]
"""
#!/usr/bin/env python
print("Introduce el valor de a: ")
a = int(input())
print("Introduce el valor de b: ")
b = int(input())
print("Introduce el primer termino de la sucesion: ")
termino1=int(input())
print("Di cunatos terminos de sucesion: ")
termino2=int(input())

lista=[]
#Se agregan a la lista el termino1
lista.append(termino1)
#Bucle que lo recorra
for i in range(termino2):
	#El termino cambia de valor y se va agregando hasta el fin de termino2
	termino1=a*termino1-b
	lista.append(termino1)
print("Los terminos de la sucesion son: ", lista)

