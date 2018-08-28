# -*- coding: UTF-8 -*-

def sql_get_conn():
	import sqlite3
	conn = sqlite3.connect('test.db')  
	return conn

def sql_get_cursor(conn):
	cur = conn.cursor()
	return cur
	
def sql_commit(conn):
	conn.commit()
	return

def sql_close(cur, conn):	
	cur.close()   
	conn.close()  
	return
''' 
cur.execute('create table t(id int,v varchar(20));');  
  
cur.execute("insert into t values(%d,'%s')" % (1,'xxx'))  
cur.execute("insert into t values(%d,'%s')" % (2,'yyy'))  
  
cur.execute("update t set v = '%s' where id = %d" % ('zzz',2))  
  
cur.execute("select * from t;")  
'''

def sql_create_tabel(sql_cmd):

	conn = sql_get_conn()  
	cur = sql_get_cursor(conn)
	
	cur.execute(sql_cmd)
	
	sql_commit(conn) 
	sql_close(cur,conn)
	
	return

def sql_insert_into_table(table_name,dict_item):
	conn = sql_get_conn()  
	cur = sql_get_cursor(conn)
	
	for i in range(0,len(dict_item)):
		try:
			cur.execute("insert into '%s' values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s',%1.2f,%1.2f,%1.2f,'%s','%s','%s','%s');" 
				  %(table_name,
					dict_item[i]['match_sequence'],
					dict_item[i]['match_type'],
					dict_item[i]['match_round'],
					dict_item[i]['match_date'],
					dict_item[i]['match_time'],
					dict_item[i]['match_status'],
					dict_item[i]['match_result_finnal'],
					dict_item[i]['team_one'],
					dict_item[i]['score'],
					dict_item[i]['team_two'],
					dict_item[i]['match_result_half'],
					dict_item[i]['home_team_odds'],
					dict_item[i]['draw_odds'],
					dict_item[i]['visiting_team_odds'],
					dict_item[i]['lid'],
					dict_item[i]['fid'],
					dict_item[i]['sid'],
					dict_item[i]['infoid']))
		except:
			print(dict_item[i]['lid'])
			continue
	
	for row in cur.execute("select * from '%s';" % (table_name)):
		print(row)
		
	sql_commit(conn) 
	sql_close(cur,conn) 
 
	return

def sql_update_table(table_name,dict_item):

	conn = sql_get_conn()  
	cur = sql_get_cursor(conn)
	
	for i in range(0,len(dict_item)):
		try:
			cur.execute("update '%s' set match_status = '%s', score = '%s', match_result_half = '%s', match_result_finnal = '%s' where match_sequence = '%s';" 
					  %(table_name,
						dict_item[i]['match_status'],
						dict_item[i]['score'],
						dict_item[i]['match_result_half'],
						dict_item[i]['match_result_finnal'],
						dict_item[i]['match_sequence']))
		except:
			continue
	
	sql_commit(conn) 
	sql_close(cur,conn)  
	
	return
	
def sql_select_all_from_table(table_name):
	conn = sql_get_conn()  
	cur = sql_get_cursor(conn)
	
	cur.execute("select * from '%s' order by match_sequence;" % (table_name))
	
	for row in cur.fetchall():
		print(row)
	
	sql_commit(conn) 
	sql_close(cur,conn) 
	
	return
	
def sql_select_item_from_table(table_name, item):
	conn = sql_get_conn()  
	cur = sql_get_cursor(conn)
	
	cur.execute("select '%s' from '%s';" % (item, table_name))
	
	for row in cur.fetchall():
		print(row)	
		
	sql_commit(conn) 
	sql_close(cur,conn) 
	
	return

def sql_exec(sql_cmd):
	conn = sql_get_conn()  
	cur = sql_get_cursor(conn)
	
	cur.execute(sql_cmd)
	
	for row in cur.fetchall():
		print(row)	
		
	sql_commit(conn) 
	sql_close(cur,conn) 
	
	return

	
# create_tabel('table_1')
#insert_into_table('table_1')
#select_from_table('table_1')

#sql_select_item_from_table()


