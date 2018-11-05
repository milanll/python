# !/usr/bin/env python
# -*- coding:utf-8 -*-  

'''
基础读取配置文件
 
-read(filename)               直接读取文件内容
-sections()                      得到所有的section，并以列表的形式返回
-options(section)            得到该section的所有option
-items(section)                得到该section的所有键值对
-get(section,option)        得到section中option的值，返回为string类型
-getint(section,option)    得到section中option的值，返回为int类型，还有相应的getboolean()和getfloat() 函数。


基础写入配置文件
 
-write(fp)                              	将config对象写入至某个 .init 格式的文件  Write an .ini-format representation of the configuration state.
-add_section(section)                       添加一个新的section
-set( section, option, value                对section中的option进行设置，需要调用write将内容写入配置文件 ConfigParser2
-remove_section(section)                    删除某个 section
-remove_option(section, option)             删除某个 section 下的 option
'''

import configparser
import os

#[input]	db(str)	'soccer'
#[output]	home_team_odds_low(float)
#			home_team_odds_high(float)
#			visiting_team_odds_low(float)
#			visiting_team_odds_high(float)
def read_config(db):
	os.chdir("E:\\git\\python\\py_code\\py_comm")
	 
	cf = configparser.ConfigParser()
	 
	cf.read("config.conf")

	items = cf.items(db)
	#print(type(items))
	#print('db:', items)
	
	home_team_odds_low 		= cf.getfloat(db, 'home_team_odds_low')
	home_team_odds_high 	= cf.getfloat(db, 'home_team_odds_high')
	visiting_team_odds_low 	= cf.getfloat(db, 'visiting_team_odds_low')
	visiting_team_odds_high = cf.getfloat(db, 'visiting_team_odds_high')
	
	return home_team_odds_low, home_team_odds_high, visiting_team_odds_low, visiting_team_odds_high
	
if __name__ == '__main__':
	items = read_config('soccer')
	print(float(items[0][1]),float(items[1][1]),float(items[2][1]),float(items[3][1]))