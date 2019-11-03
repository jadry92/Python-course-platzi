
## Lists
my_list = ["string",15,15.6,True]

my_list.append(6)
my_list.insert(1,"insert")

my_list.remove(15)
last_value = my_list.pop()

print(my_list)
print(last_value)

##

my_list = [1,2,5,78,65,22,44,66,44,113,23,59,79]
my_list_two = [22,23]

#my_list.sort(reverse = True)
#my_list.sort()

#my_list.extend(my_list_two)
my_list.append(my_list_two)
print(my_list)