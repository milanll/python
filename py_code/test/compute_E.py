# -*- coding: UTF-8 -*-

import sys
import math
def factorial_(n):
	a = 1
	for n in range(1, n + 1):
		a *= n
	return a
	
for n in range(1, int(sys.argv[1])):
	a = 1/n
	b = 1 + a
	c = b ** n
	print (c)

m = int(sys.argv[2])
print(m," factorial is ",factorial_(m))

la = [1, 2, 3]
la[1] = 1
print(la)

