import os
import json
import time

import sys;
sys.path.append("../py_comm")
from py_time import get_time_stamp		#get_time_stamp()
from get_match_data import get_id			#get_id(url)
from soccer_comm import print_help, print_match_result, print_odds
from soccer_comm import GIT_HOME
from save_match_data import save_match_data

#[input] 	choice(str)
#[output]	match_data_dict(dict)	{'736775': {'match_sequence': '周五003', 'match_type': '俄超', 'match_round': '第14轮', 'match_date': '11-10', 'match_time': '00:30', 'match_status': '0', 
#												'match_result_finnal': '\xa0 ', 'team_one': '[12]图兵工厂', 'score': '-', 'team_two': '安郅[14]', 'match_result_half': ' - ', 'home_team_odds': 1.46, 
#												'draw_odds': 3.99, 'visiting_team_odds': 6.95, 'lid': '67', 'fid': '736775', 'sid': '4849', 'infoid': '126811'}
def read_match_data(choice):
	time_now = time.strftime("%Y-%m-%d",time.localtime())
	match_data_file_name = time_now + '_match_data_' + choice + '.json'
	
	file_list = os.listdir(f'{GIT_HOME}/match_data/') #返回文件名
	#print(file_list)
	
	match_data_dict = {}
	
	if file_list is None:
		print('No file!!')
		return None
		
	if (match_data_file_name not in file_list):
		print('No match data file!')
		print('Getting match data .......')
		if save_match_data(choice):
			pass
		else:
			print('Save match data fail!!')
			return None
	
	with open(f'{GIT_HOME}/match_data/{match_data_file_name}', 'r') as f:
		match_data = json.load(f)
		match_data_dict = json.loads(match_data)
		f.close()
	
	print('match_data_dict: ', len(match_data_dict))
	
	#for item in match_data_dict.items():
	#	print(item)
	
	return match_data_dict
	
#[input] 	choice(str)
#[output]	match_odds_dict(dict)	{'736775': {'0': [1.46, 3.99, 6.95], '3': [1.5, 3.8, 7.5], '5': [1.45, 3.85, 6.3], 'rqsp': [2.49, 3.15, 2.44], 'sp': [1.43, 3.6, 6.55], '280': [1.47, 4.0, 6.6], '1055': [1.49, 4.35, 7.21], '293': [1.44, 4.2, 7.0]}	
def read_match_odds(choice):
	time_now = time.strftime("%Y-%m-%d",time.localtime())

	match_odds_file_name = time_now + '_match_odds_' + choice + '.json'
	
	file_list = os.listdir(f'{GIT_HOME}/match_data/') #返回文件名
	#print(file_list)

	match_odds_dict = {}
	
	if file_list is None:
		print('No file!!')
		return None
		
	if (match_odds_file_name not in file_list):
		print('No match data file!')
		print('Getting match data .......')
		if save_match_data(choice):
			pass
		else:
			print('Save match odds fail!!')
			return None
	
	with open(f'{GIT_HOME}/match_data/{match_odds_file_name}', 'r') as f:
		odds_data = json.load(f)
		match_odds_dict = json.loads(odds_data)
		f.close()

	print('match_odds_dict: %d\n' % len(match_odds_dict))
	
	return match_odds_dict

#[input]	match_info(dict)
def print_items(match_info):
	
	i = 0
	for (k,v) in match_info.items():
		'''
		print(	v['lid'],
				v['fid'],
				v['sid'],
				v['infoid'],
				v['match_sequence'],
				v['match_status'],
				v['team_one'],
				v['score'],
				v['team_two'],
				v['match_result_half'],
				v['match_result_finnal'],
				v['home_team_odds'],
				v['draw_odds'],
				v['visiting_team_odds'])
		'''
		if '4' == v['match_status']:
			print(v['match_date'].ljust(5),v['match_status'].ljust(2),v['match_result_half'].ljust(2), v['match_result_finnal'].ljust(2), v['team_one'].ljust(16))
			i += 1
	print('Count of match finished:', i)
	return
	
if __name__ == '__main__':
	print_help()
	choice = input('please choice url:')
	
	match_info = read_match_data(choice)
	odds_dict = read_match_odds(choice)
	
	print_items(match_info)
	#print_match_data(match_data_dict)
	#print_match_result(match_data_dict, odds_dict)
	
	




