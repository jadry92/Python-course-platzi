# my strings
name = 'Johan Sebastia'
last_name = 'Suarez Largo'

""" Format """
result = '{a} -- {b}'.format(b = name, a = last_name)
#result = name + last_name
#result = result.lower()
#result = result.upper()
result = result.title()
print(result)
""" search """
pos = result.find('Sebas')
count = result.count('S')

""" sutitution """        
new_string = result.replace('a','x')

new_string = result.split(' daas')
print(pos)
print(count)
print(result)
print(new_string)