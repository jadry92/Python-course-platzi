contador = 0
while contador < 10:
	print(contador)
	contador +=1
	if contador == 5:
		continue
	if contador == 6:
		break	
else:	
	print("The while it's done")

contador = 0
bandera = True
while bandera:
	print(contador)
	contador +=1
	if contador == 5:
		continue
	if contador == 6:
		bandera = False	
else:	
	print("The while it's done")	