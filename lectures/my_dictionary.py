dictionary = { 'a' : 55, 'b' : 12 ,'5' : "this is a string", (1,2) : False , 'a' :100} # las claves deben de ser inmutables

dictionary['c'] = "nuevo string"# make or change value
dictionary['a'] = 12345 

#valor = dictionary['a'] # take value
valor = dictionary.get('z',546453)
del dictionary['5'] # del elimina

#print(dictionary)
#print(valor)

llaves = list( dictionary.keys()) #objeto iterable
valores = list( dictionary.values())

llaves = tuple( dictionary.keys()) #objeto iterable
valores = tuple( dictionary.values())

dictionary_two = {'z' : 12, 'w' : 65}
#dictionary['z'] = dictionary_two['z']
#dictionary['w'] = dictionary_two['w']

dictionary.update(dictionary_two)

#print(llaves)
#print(valores)
print(dictionary)