def fatorial_funtion(number):
	fatorial = 1
	while number > 0:
		fatorial = number * fatorial
		number -= 1
	return fatorial	
	
fatorial = fatorial_funtion(4)	
print(fatorial)
fatorial = fatorial_funtion(200)	
print(fatorial)
fatorial = fatorial_funtion(2)
print(fatorial)	