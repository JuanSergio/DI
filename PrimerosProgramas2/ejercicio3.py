"""Supongamos ​ s ​  es una cadena de caracteres en minúscula. 
 Escribir   un   programa   que   imprime   el   número   de   
 veces   que   la   cadena   ​ 'bob'   se   produce   en  s ​ .  
 
Por ejemplo, si ​ s='azcbobobegghakl' ​ , entonces su programa debe imprimir 
 
Número de veces que ocurre es: 2  """

#!/usr/bin/env python
print("Dime la frase");
frase=input();

#Dentro de Count añadir la cadena "contar"
print(frase.count('bob'));
