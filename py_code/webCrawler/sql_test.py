# -*- coding: UTF-8 -*-

import sqlite3

conn = sqlite3.connect('test.db') 

cur = conn.cursor()

'''
for row in cur.execute("select score from table_1;"):

	print(row)
'''

cur.execute("select count(*) from table_1 where match_result_finnal = '胜';")

print(cur.fetchone())

conn.commit()

cur.close()  
 
conn.close()