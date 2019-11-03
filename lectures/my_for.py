lista = [1,2,3,4,5,6,7,8,9,10]
indice = 0
for valor in lista:
	print(valor," Tiene el indice ",indice)
	indice +=1

rango_1 = range(10,21)

for valor in rango_1:
	print(valor)

rango_1 = range(0,20,2)

for valor in rango_1:
	print(valor)

for valor in range(0,20,2):
	print(valor)

for valor,indice in enumerate(lista):
	print(valor,"Tiene el indice",indice)	

for valor in range(0, len(lista)):
	print(valor)

for valor in "johan":
	print(valor)	

diccionario = {'a': 10,'b': 20,'c': 'to'}
for llave, valor in diccionario.items():
	print("la llave",llave,"tiene el valor de",valor)	