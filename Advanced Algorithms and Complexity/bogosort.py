#only valid for list of size 5

import random
a = [5, 8, 7, 1, 2]
flag = 0

while flag != 1:
    random.shuffle(a)
    if a[0] < a[1] and a[1] < a[2] and a[2] < a[3] and a[3] < a[4]: 
        flag = 1
    else: 
        flag = 0
print(a)