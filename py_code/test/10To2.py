
# -*- coding: UTF-8 -*-

denum_str = input("请输入十进制数: ")

denum = int(denum_str)
binnum = []

while denum > 0:
	binnum.append(str(denum%2))
	denum //= 2						# //:取整除 - 返回商的整数部分
	
print(denum_str,"(10)", ' = ')
while len(binnum)>0:
    import sys
    sys.stdout.write(binnum.pop()) 	# 无空格输出print ' (2)'

a = ord('a')
ua = chr(a)

print(),
print(a, ua)
