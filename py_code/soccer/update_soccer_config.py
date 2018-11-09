# -*- coding:utf-8 -*- 

import sys
sys.path.append("../py_comm")

from py_config import update_option
from read_match_data import read_match_data
import soccer_comm

#[input]	match_dict(dict)	{'736775': {'match_sequence': '周五003', 'match_type': '俄超', 'match_round': '第14轮', 'match_date': '11-10', 'match_time': '00:30', 'match_status': '0', 'match_result_finnal': '\xa0 ', 'team_one': '[12]图兵工厂', 'score': '-', 'team_two': '安郅[14]', 'match_result_half': ' - ', 'home_team_odds': 1.46, 'draw_odds': 3.99, 'visiting_team_odds': 6.95, 'lid': '67', 'fid': '736775', 'sid': '4849', 'infoid': '126811'}
#[output]	option(dict)	{'67': '俄超', '312': '澳超', '68': '苏超', ......}
def construct_option(match_dict):
	list = []
	option = {}
	for (k, item) in match_dict.items():
		if item['lid'] not in list:
			option[item['lid']] = item['match_type']
			list.append(item['lid'])
	
	#print(option)
	
	return option

#[input]	dir(str) 			"E:\\git\\python\\py_code\\soccer"
#			filename(str)  		"soccer.conf"
#			section(str) 		'odds'
#			match_dict(dict)	{'736775': {'match_sequence': '周五003', 'match_type': '俄超', 'match_round': '第14轮', 'match_date': '11-10', 'match_time': '00:30', 'match_status': '0', 'match_result_finnal': '\xa0 ', 'team_one': '[12]图兵工厂', 'score': '-', 'team_two': '安郅[14]', 'match_result_half': ' - ', 'home_team_odds': 1.46, 'draw_odds': 3.99, 'visiting_team_odds': 6.95, 'lid': '67', 'fid': '736775', 'sid': '4849', 'infoid': '126811'}
def update_section_league(dir, filename, section, match_dict):
	option = construct_option(match_dict)
	
	update_option(dir, filename, section, option)
		
	return
	
if __name__ == '__main__':	
	dir = "E:\\git\\python\\py_code\\soccer"
	filename = "soccer.conf"
	section = 'league'
	
	soccer_comm.print_help()
	url_choice = input('please choice url:')

	match_dict = read_match_data(url_choice)
	
	update_section_league(dir, filename, section, match_dict)