'''
import codecs
with codecs.open('bet_clause.txt', encoding = 'utf-8') as fp:
data = fp.read()
print data
'''

import re
pattern = re.compile(r'\d+(?!\w)')

fo = open('bet_clause.txt', 'r', encoding = 'utf-8')
print('file name: ', fo.name)

list = []
for line in fo.readlines():
	if line == '\n':
		pass
	else:
		#print(line.strip())
		list_temp = pattern.findall(line)
		for elem in list_temp:
			list.append(elem)
		
#print(list)
print(len(list))

list_num = []
for elem in list:
	number = int(elem)
	list_num.append(number)

print(list_num)

fo.close()
	
	
	
	
