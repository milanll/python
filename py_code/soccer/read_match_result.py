import os
import json
import time

import sys;
sys.path.append("../time_chenll")
import time_manage
from time_manage import get_time_stamp		#get_time_stamp()

from get_match_data import get_id			#get_id(url)
from soccer_comm import print_help, print_match_result
		
def read_match_result(choice):
	
	time_now = time.strftime("%Y-%m-%d",time.localtime())
	match_result_file_name = time_now + '_match_result_' + choice + '.json'
	match_odds_file_name = time_now + '_match_odds_' + choice + '.json'
	print('File Name:\n', match_result_file_name, '\n', match_odds_file_name, '\n')
	
	file_list = os.listdir(r'E:\7_python\code\soccer\match_data') #返回文件名
	#print(file_list)
	
	if file_list is None:
		print('no such file')
		return
		
	if (match_result_file_name not in file_list):
		#print('No match result file!')
		return
	
	with open(f'./match_data/{match_result_file_name}', 'r') as f:
		match_data = json.load(f)
		match_data_dict = json.loads(match_data)
		f.close()
	
	with open(f'./match_data/{match_odds_file_name}', 'r') as f:
		odds_data = json.load(f)
		match_odds_list = json.loads(odds_data)
		f.close()
		
	print('read dict len: ', len(match_data_dict))
	
	return match_data_dict, match_odds_list
	
if __name__ == '__main__':
	print_help()
	choice = input('please choice url:')
	
	match_result_dict, odds = read_match_result(choice)
	if match_result_dict is None:
		print('No match result file!')
		sys.exit()

	print_match_result(match_result_dict)
	
	
	
	