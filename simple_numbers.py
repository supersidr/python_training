# -*- coding: utf-8 -*-
import math

i = 0
while i < 100:
    if (i / 2 - math.floor(i / 2)) != 0 and (i / 3 - math.floor(i / 3)) != 0 and (i / 5 - math.floor(i / 5)) != 0 and (i / 7 - math.floor(i / 7)) != 0:
        print (i)
    i = i + 1

n = 100
lst=[]
for i in range(2, n+1):
    # пробегаем по списку (lst) простых чисел
    for j in lst:
        if i % j == 0:
            break
    else:
        lst.append(i)
print (lst)