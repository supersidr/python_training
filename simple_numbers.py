# -*- coding: utf-8 -*-
import math

i = 0
while i < 100:
    if (i / 2 - math.floor(i / 2)) != 0 and (i / 3 - math.floor(i / 3)) != 0 and (i / 5 - math.floor(i / 5)) != 0:
        print (i)
    i = i + 1