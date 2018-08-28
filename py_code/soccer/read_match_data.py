import os
import json
import time

import sys;
sys.path.append("../time_chenll")
import time_manage
from time_manage import get_time_stamp		#get_time_stamp()

from get_match_data import get_id			#get_id(url)
from soccer_comm import print_help, print_match_result
		
def read_match_data(choice):
	time_now = time.strftime("%Y-%m-%d",time.localtime())
	
	if (len(sys.argv) > 1):
		if (sys.argv[1] == 'r'):
			match_data_file_name = time_now + '_match_result_' + choice + '.json'
		else:
			print('your choice is wrong!')
			return
	else:
		match_data_file_name = time_now + '_match_data_' + choice + '.json'

	match_odds_file_name = time_now + '_match_odds_' + choice + '.json'
	
	file_list = os.listdir(r'E:\7_python\code\soccer\match_data') #返回文件名
	#print(file_list)
	
	if file_list is None:
		print('no such file')
		return
		
	if (match_data_file_name not in file_list):
		print('No match data file!')
		return
	
	if (match_odds_file_name not in file_list):
		print('No odds file!')
		return
	
	with open(f'./match_data/{match_data_file_name}', 'r') as f:
		match_data = json.load(f)
		match_data_dict = json.loads(match_data)
		f.close()
	
	with open(f'./match_data/{match_odds_file_name}', 'r') as f:
		odds_data = json.load(f)
		match_odds_dict = json.loads(odds_data)
		f.close()
	
	print('read dict len: ', len(match_data_dict))
	
	return match_data_dict, match_odds_dict
	
if __name__ == '__main__':
	print_help()
	choice = input('please choice url:')
	
	match_data_dict, odds_dict = read_match_data(choice)
	
	#print_odds(odds_dict)
	#print_match_data(match_data_dict)
	print_match_result(match_data_dict, odds_dict)
	
	




