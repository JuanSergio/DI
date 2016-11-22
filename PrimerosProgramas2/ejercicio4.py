"""Una   empresa   de   catering   que   ha   contratado   para   ayudar   con   
la   organización   y   preparación  
de   los   pedidos   del   cliente.   Se   le   da   una   lista   de   los   
artículos   deseados   de   cada   cliente,   y  
debe   escribir   un   programa   que   va   a   contar   el   número   de   
cada   uno   de   los   artículos  
necesarios   para   los   cocineros   para   preparar.   Los   artículos   que   
un   cliente   puede   pedir   son:  
ensalada, hamburguesa, y agua. 
 
Escribir   una   función   llamada   ​ item_order   que   toma   como   entrada   
una   cadena   denominada  
orden ​ .   La   cadena   contiene   sólo   palabras   de   los   artículos   
que   el   cliente   puede   pedir  
separadas   por   un   espacio.   La   función   devuelve   una   cadena   
que   cuenta   el   número   de   cada  
elemento y las consolida en el siguiente orden:  
ensalada: [# ensalada] hamburguesa: [# hambruger] agua: [# agua] 
 
Si   un   pedido   no   contiene   un   elemento,   entonces   el   recuento   
de   ese   elemento   es   0.   Tenga  
en   cuenta   que   cada   elemento   tiene   el   formato   de   [nombre   
del   elemento]   [un   símbolo   de   :]  
[recuento de Artículo] y todos los grupos de artículos están separadas por una espacio. 
 
Por ejemplo: 
 
Si   ​ orden   =   "ensalada   hamburguesa   agua   ensalada   hamburguesa" ​ ,   
entonces   la  
función devuelve ​ "ensalada: 2 hamburguesa: 2 agua: 1" 
Si   ​ orden   =   "hamburguesa   hamburguesa   agua" ​ ,   entonces   la   
función   devuelve  
"ensalada: 0 hamburguesa: 2 agua: 1"""

#!usr/bin/env python
def Item_order(pedido):
	#Se crea un bucle de recorrido
	for i in lista:
		if "ensalada" :
			i.count("ensalada")
		if "hamburguesa" :
			i.count("hamburguesa")
		if "agua" :
			i.count("agua")
		pedido=print("ensalada: ",i.count("ensalada"),"hamburguesa: ",i.count("hamburguesa"),"agua: ",i.count("agua"))
		

lista=[]
cadenas=input("Introduce pedido ")

lista.append(cadenas)
#resultado
print(Item_order(lista))