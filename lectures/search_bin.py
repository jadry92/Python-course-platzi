import numpy as np
import random

number_random = [random.randint(0,100) for i in range(10)]
uids = [i for i in range(10)]
number_random.sort()
print(number_random)
print(uids)
numb = int(input('What number would you like to find ?'))
flag_find = False
id_b = 0
id_l = len(number_random)-1
id_mid = 0

while id_b <= id_l and not flag_find:
    id_mid = int(np.floor((id_b + id_l)/2))
    if numb == number_random[id_mid]:
        flag_find = True
    elif numb > number_random[id_mid]:
        id_b = id_mid+1
    else:
        id_l = id_mid-1

if flag_find:
    print('done = ',id_mid)
else:
    print('the number is not in the list')
