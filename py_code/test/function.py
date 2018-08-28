
# -*- coding: UTF-8 -*-

def ArrayConcatenate(a, b):
	"把两个数组合并到一起"
	for i in range(0,len(b)):
		a.append(b[i])
	return

a = [0,1,2]
b = [3,4,5]

ArrayConcatenate(a, b)
print(a)
print(b)