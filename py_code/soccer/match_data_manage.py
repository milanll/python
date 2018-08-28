
import os
import json
import time

import sys;
sys.path.append("../time_chenll")
import time_manage
from time_manage import get_time_stamp		#get_time_stamp()

from get_match_data import get_id			#get_id(url)

#竞彩比分
url_jc = "https://live.500.com"
#单场比分
url_dch = "http://live.500.com/zqdc.php"

def print_help():
	print('精彩比分：jc')
	print('单场比分：dch')

def save_match_data():
	print_help()
	choice = input('please choice url:')
	
	url = url_jc
	#time_str = get_time_stamp()
	time_now = time.strftime("%Y-%m-%d",time.localtime())
	time_data_str = time_now + '_match_data_' + choice
	time_odds_str = time_now + '_match_odds_' + choice
	
	if choice == 'jc':
		url = url_jc
	elif choice == 'dch':
		url = url_dch
	else:
		print('your choice is wrong!')
		return
		
	dict_items, dict_odds = get_id(url)

	# r'input\n' # 非转义原生字符，经处理'\n'变成了'\\'和'n'。也就是\n表示的是两个字符，而不是换行。
	# u'input\n' # unicode编码字符，python3默认字符串编码方式。
	# 以f开头表示在字符串内支持大括号内的python 表达式
	
	#save match data
	if dict_items:
		with open(f'./match_data/{time_data_str}.json', 'w') as f:
			#f.truncate()
			#f.write(json.dumps(dict_items, ensure_ascii=False, indent=4).encode())
			data_dict = json.dumps(dict_items)

			json.dump(data_dict, f)
			f.close()

		print(f"Save atch data OK!!\nfile path: {os.getcwd()}\match_data/{time_data_str}.json")
	
	#save match odds
	if dict_odds:
		with open(f'./match_data/{time_odds_str}.json', 'w') as f:
			odds_dict = json.dumps(dict_odds)
			json.dump(odds_dict, f)
			
			f.close()

		print(f"Save atch odds OK!!\nfile path: {os.getcwd()}\match_data/{time_odds_str}.json")

def read_match_date():
	print_help()
	choice = input('please choice url:')
	
	time_now = time.strftime("%Y-%m-%d",time.localtime())
	match_data_file_name = time_now + '_match_data_' + choice + '.json'
	match_odds_file_name = time_now + '_match_odds_' + choice + '.json'
	
	path = 'E:/7_python/code/soccer/match_data/'
	file_list = os.listdir(r'E:\7_python\code\soccer\match_data') #返回文件名
	print(file_list)
	
	if file_list is None:
		print('no such file')
		return
		
	if match_data_file_name not in file_list:
		print('No data file!')
		return
	
	with open(f'./match_data/{match_data_file_name}', 'r') as f:
		match_data = json.load(f)
	
	match_data_dict = json.loads(match_data)
	#for (k,v) in data_dict.items():
	#	print(v['match_date'].ljust(8),v['match_status'].ljust(2),v['team_one'].ljust(16))
	return match_data_dict
	
if __name__ == '__main__':
	save_match_data()
	