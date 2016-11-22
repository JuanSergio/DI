"""Escribe una función iterativa ​ iterPower (base, exp) ​  que calcula el exponencial 
base​ exp​  simplemente usando multiplicación sucesiva.  
Por   ejemplo,   iterPower   (base,   exp)   debe   calcular   b
ase​ exp   multiplicando   base   por   sí   mismo  exp​  veces. 
Esta   función   debe   tomar   dos   valores   ­   base   puede   ser   un   float   o   un   número   entero;   exp   será  
un   número   entero≥   0.   Debe   devolver   un   valor   numérico.   El   código   debe   ser   iterativo   ­   el   uso  
del operador ** no está permitido."""

#!/usr/bin/env python

print ("Dime la base")
base = int(input())
print ("Dime el exponente")
exponente = int(input())

def iterPower(b, exp):
	aux = 1
	while (exp>0):
		aux = aux*b
		exp -= 1
	print (str(aux))

iterPower (base, exponente)