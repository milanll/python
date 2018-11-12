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
import os, sys
import traceback
import codecs

#[input]	dir(str)		"E:\\git\\python\\py_code\\soccer"
#			filename(str)	"config.conf"
#[output]	cf()
def init_config(dir, filename):
	os.chdir(dir)
	cf = configparser.ConfigParser()
	
	return cf

#[input]	dir(str)		"E:\\git\\python\\py_code\\soccer"
#			filename(str)	"config.conf"
#			section(str)	'league'

#[output]	home_team_odds_low(float)
#			home_team_odds_high(float)
#			visiting_team_odds_low(float)
#			visiting_team_odds_high(float)
def read_config(dir, filename, section):
	cf = init_config(dir, filename)
	cf.read(filename)
	
	home_team_odds_low 		= cf.getfloat(section, 'home_team_odds_low')
	home_team_odds_high 	= cf.getfloat(section, 'home_team_odds_high')
	visiting_team_odds_low 	= cf.getfloat(section, 'visiting_team_odds_low')
	visiting_team_odds_high = cf.getfloat(section, 'visiting_team_odds_high')
	
	return home_team_odds_low, home_team_odds_high, visiting_team_odds_low, visiting_team_odds_high

#[input]	section(str)	'odds'
#			dir(str)		"E:\\git\\python\\py_code\\soccer"
#			filename(str)	"config.conf"
#			option(dict)	{'63':'欧罗巴',......}
def update_option(dir, filename, section, option):
	cf = init_config(dir, filename)
	#read config content to cf first, otherwise, config file will be overided
	try:
		cf.read(filename)
	except:
		traceback.print_exc()
		sys.exit()
		
	if section not in cf.sections():
		cf.add_section(section)	
			
	for(k, v) in option.items():
		cf.set(section, k, v)
	
	with open(f'{dir}\\{filename}', 'w') as f:
		try:
			cf.write(f)
		except:
			 traceback.print_exc()
		
	#for (k, v) in cf.items('odds'):
	#	print(k,v)
	
	return
	
	
if __name__ == '__main__':
	dir = "E:\\git\\python\\py_code\\soccer"
	filename = "soccer.conf"
	#items = read_config(dir, filename, 'odds')
	option = {'123':'你好'}
	update_option(dir, filename, 'odds', option)

	
	
	
	
	
	
	
	