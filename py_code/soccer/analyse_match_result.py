# -*- coding:utf-8 -*- 

from read_match_data import read_match_data, read_match_odds
from soccer_comm import print_help, URL_JC, URL_DCH
import odds
import py_config

#[input]	match_info(dict)
#[output]	match_finished(dict)
def get_match_finished(match_info):
	match_finished = {}
	'''
	match status:
		0	Unplayed match
		3  	Ongoing match
		4   Finishied match
		6 	Delayed match
	'''
	for (k, v) in match_info.items():
		if '4' == v['match_status']:
			match_finished[k] = v
	
	return match_finished

#[input]	match_finished(dict)	{'736775': {'match_sequence': '周五003', 'match_type': '俄超', 'match_round': '第14轮', 'match_date': '11-10', 'match_time': '00:30', 'match_status': '0', 'match_result_finnal': '0 ', 'team_one': '[12]图兵工厂', 'score': '-', 'team_two': '安郅[14]', 'match_result_half': ' - ', 'home_team_odds': 1.46, 'draw_odds': 3.99, 'visiting_team_odds': 6.95, 'lid': '67', 'fid': '736775', 'sid': '4849', 'infoid': '126811'}
#			odds(dict)				{"753465":{"0":[4.18,3.68,1.72],"3":[4.33,3.75,1.75],"293":[4.2,3.8,1.73],"rqsp":[2.15,3.45,2.67],"sp":[4.70,3.80,1.53],"280":[4.2,3.9,1.74],"1055":[4.32,3.94,1.77]},}	
def match_result_parse(match_finished, odds):
	win_num = 0 
	loss_num = 0
	draw_num = 0
	total_num = 0
	fail_num = 0
	#read odds config
	#home_team_odds_low 		= 1.40
	#home_team_odds_high 		= 1.85
	#visiting_team_odds_low 	= 1.50
	#visiting_team_odds_high 	= 2.00
	home_team_odds_low, home_team_odds_high, visiting_team_odds_low, visiting_team_odds_high = py_config.read_config(dir, filename, section)
	
	for (key, v) in match_finished.items():
		#主队赔率
		if ((odds[key]['0'][0] < home_team_odds_high) and (odds[key]['0'][0] > home_team_odds_low)):
			total_num += 1
			if '3' == v['match_result_finnal']:
				win_num += 1
			elif '1' == v['match_result_finnal']:
				draw_num += 1
			else:
				fail_num += 1 
		#客队赔率	
		elif((odds[key]['0'][2] < visiting_team_odds_high) and (odds[key]['0'][2] > visiting_team_odds_low)):
			total_num += 1
			if '0' == v['match_result_finnal']:
				loss_num += 1
			elif '1' == v['match_result_finnal']:
				draw_num += 1
			else:
				fail_num += 1 
		else:
			continue
		
	print('win: ', win_num + loss_num)
	print('draw: ', draw_num)
	print('fail: ', fail_num, '\nfail rate: ', fail_num*100/total_num)
	print('total: ', total_num)
		
	return 
		
if __name__ == "__main__":
	dir = "E:\\git\\python\\py_code\\soccer"
	filename = "soccer.conf"
	section = 'odds'

	print_help()
	url_choice = input('please choice url:')

	match_dict = read_match_data(url_choice)
	odds_dict = read_match_odds(url_choice)
	if match_dict is None:
		print('read_match_data() Fail!!')
		sys.exit()
		
	if url_choice == 'jc':
		url = URL_JC
	elif url_choice == 'dch':
		url = URL_DCH
	else:
		print('url is wrong!')
		sys.exit()
	
	match_finished = get_match_finished(match_dict)
	match_result_parse(match_finished, odds_dict)

	
	
	
	
	
	
	
	
	