import os
import json
import time

import sys;
sys.path.append("../py_comm")
from py_time import get_time_stamp		#get_time_stamp()

from get_match_data import get_id			#get_id(url)
from parse_item import get_items_from_500
from soccer_comm import print_help, print_match_result
from soccer_comm import GIT_HOME

#竞彩比分
url_jc = "https://live.500.com"
#单场比分
url_dch = "http://live.500.com/zqdc.php"

#[input] 	choice(str)
#[output]	True / False
def save_match_data(choice):
	
	url = url_jc

	time_now = time.strftime("%Y-%m-%d",time.localtime())
	
	if (len(sys.argv) > 1):
		if (sys.argv[1] == 'r'):
			time_data_str = time_now + '_match_result_' + choice
		else:
			print('your choice is wrong!')
			return False
	else:
		time_data_str = time_now + '_match_data_' + choice
		
	#time_data_str = time_now + '_match_data_' + choice
	time_odds_str = time_now + '_match_odds_' + choice
	
	print(time_now)
	
	if choice == 'jc':
		url = url_jc
	elif choice == 'dch':
		url = url_dch
	else:
		print('your choice is wrong!')
		return	False
		
	dict_items, dict_odds = get_items_from_500(url)

	# r'input\n' # 非转义原生字符，经处理'\n'变成了'\\'和'n'。也就是\n表示的是两个字符，而不是换行。
	# u'input\n' # unicode编码字符，python3默认字符串编码方式。
	# 以f开头表示在字符串内支持大括号内的python 表达式
	
	#save match data
	if dict_items:
		with open(f'{GIT_HOME}/match_data/{time_data_str}.json', 'w') as f:
			#f.truncate()
			#f.write(json.dumps(dict_items, ensure_ascii=False, indent=4).encode())
			data_dict = json.dumps(dict_items)

			json.dump(data_dict, f)
			f.close()

		print(f"Save match data OK!!\nfile path: {os.getcwd()}\match_data/{time_data_str}.json")
	else:
		print("Save match data OK!!\n")
		return False
	
	#不保存odds
	if len(sys.argv) > 1:
		if sys.argv[1] == 'r':
			pass
	else:
		#save match odds
		if dict_odds:
			with open(f'{GIT_HOME}/match_data/{time_odds_str}.json', 'w') as f:
				odds_dict = json.dumps(dict_odds)
				json.dump(odds_dict, f)
				
				f.close()

			print(f"Save match odds OK!!\nfile path: {os.getcwd()}\match_data/{time_odds_str}.json")
		else:
			print("Save match odds OK!!\n")
			return False
	
	return True
	
if __name__ == '__main__':
	print_help()
	choice = input('please choice url:')
	save_match_data(choice)
	