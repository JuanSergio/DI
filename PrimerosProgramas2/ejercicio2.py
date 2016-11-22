"""El   máximo   común   divisor   de   dos   números   enteros   positivos   
es   el   número   entero   más  
grande que divide cada uno de ellos sin resto. Por ejemplo, 
 
gcd (2, 12) = 2 
 
gcd (6, 12) = 6 
 
gcd (9, 12) = 3 
 
gcd (17, 12) = 1 
 
Escribe   una   función   iterativa,   ​ gcdIter   (a,   b) ​ ,   que   implementa
   esta   idea.   Una   forma   fácil  
de   hacer   esto   es   comenzar   con   un   valor   de   prueba   igual   
al   menor   de   los   dos   argumentos   de  
entrada,   y   de   forma   iterativa   reducir   este   valor   de   
la   prueba   en   1   hasta   llegar   al   caso   en   el  
que la prueba divide ​ a ​  y ​ b ​  sin resto, o llegar a 1.  """

#!/usr/bin/env python
def gcdIter(a,b):
	if b==0: 
		return a
#Cambio de valores hasta que la división es 0 y b sea común divisor		
	else: 
		return gcdIter(b, a % b)

#Se introducen los parametros
n1 = int(input("Dime el primer numero: "))
n2 = int(input("Dime el segundo numero: "))
print ("El máximo común divisor es ", gcdIter(n1, n2))

	





