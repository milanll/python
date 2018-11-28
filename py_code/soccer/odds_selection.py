
import sys
sys.path.append("../py_comm")

import py_time
import py_config

dir = "E:\\git\\python\\py_code\\soccer"
filename = "soccer.conf"
section = 'odds'

#选择合适的场次的key，根据赔率
#[input]	odds_dict(dict)
def find_key(odds_dict):
	key = []
	i = 0
	
	#read odds config
	#home_team_odds_low 		= 1.40
	#home_team_odds_high 		= 1.85
	#visiting_team_odds_low 	= 1.50
	#visiting_team_odds_high 	= 2.00
	home_team_odds_low, home_team_odds_high, visiting_team_odds_low, visiting_team_odds_high = py_config.read_config(dir, filename, section)
	
	#单场
	#"730519":{
	#"0":[1.48,3.89,6.83],		平局赔率
	#"3":[1.55,3.8,6.5],		bet365
	#"5":[1.46,3.8,6.28],		澳门彩票
	#"rqsp":[2.86,4.48,2.33],	参考SP值
	#"280":[1.45,4.05,6.0],		皇冠
	#"1055":[1.49,4.03,8.22],
	#"293":[1.5,4.2,6.5]		威廉希尔
	#}
	
	#竞彩
	#"730519":{
	#"0":[1.49,3.89,6.82],		
	#"3":[1.55,3.8,6.5],
	#"5":[1.46,3.8,6.28],
	#"rqsp":[2.28,3.15,2.68],	让球奖金
	#"sp":[1.34,4.00,7.50],		胜负奖金
	#"280":[1.45,4.05,6.0],
	#"293":[1.5,4.2,6.5],
	
	for (k, v) in odds_dict.items():
		#print(k,v)
		#防止赔率列表中没有平局赔率(key='0')一项
		if('0' in v):
			#选择主场赔率在[1.3,1.8]之间，和客场赔率在[1.3,2.0]之间的比赛场次，保存赔率。
			if ((v['0'][0] < home_team_odds_high) and (v['0'][0] > home_team_odds_low)) or ((v['0'][2] < visiting_team_odds_high) and(v['0'][2] > visiting_team_odds_low)):
				key.append(k)
			else:
				i += 1
		else:
			i += 1
	print('\n', sys._getframe().f_code.co_name)
	print('delete key by odds, count: %d' % i)
	print('odds_save_key: %d\n' % len(key))
	#print(key)
	return key
	
#删除第二天9点以后比赛的key	
def del_key_next_day_match(key_time_1, match_dict):
	key_temp = []
	i = 0
	
	for key in key_time_1:
		#次日9点之后的比赛，删除
		if py_time.compare_to_next_am9(key_time_1[key]):
			key_temp.append(key)
						
	#print('key_temp:\n',key_temp)
	print('\n', sys._getframe().f_code.co_name)
	#print(key_time_1.keys())
	print('delete key which match is in next day, count: ', len(key_temp))
	for key in key_temp:
		del key_time_1[key]

	#print('\n',key_time_1.keys())
	print('key_final:',len(key_time_1))
	print(key_time_1.keys())
		
	return key_time_1

#将key同比赛时间关联起来，生成一个新的字典key_time
#[input]:	odds_dict(dict)
#			match_dict(dict)
#[output]:	key_final	
def get_key_match_time(key_list, match_dict):
	key_time = {}
	
	for key in key_list:
		if key in match_dict:
			datetiem_1 = py_time.date_time_struct(match_dict[key]['match_date'], match_dict[key]['match_time'] + ':00')
			key_time[key] = datetiem_1
			#print(datetiem_1)
	
	print('\n', sys._getframe().f_code.co_name)	
	print('match_time: %d' % len(key_time))
	return key_time

#删除已经结束的比赛的key
def del_key_match_finish(key_list, match_dict):
	print('\n', sys._getframe().f_code.co_name)	
	print('key_list:', len(key_list))
	
	i = 0
	j = 0
	key_temp = []
	for key in key_list:
		j += 1
		
		if key not in match_dict.keys():
			print('fid %s is not in match dict' % (key))
			continue
			
		'''
		match status:
			0	Unplayed match
			3  	Ongoing match
			4   Finishied match
			6 	Delayed match
		'''
		#if the match is unplayed, it will be deleted.
		if '0' != match_dict[key]['match_status']:
			key_temp.append(key)
			i += 1
	
	print('delete key that match finished, count: ', i)
	print('loop count: ', j)
	
	for key in key_temp:
		key_list.remove(key)
		
	print('key_list_1:', len(key_list))	
		
	return key_list


#[input]:	odds_dict(dict)
#			match_dict(dict)
#[output]:	key_final
def get_key_final(odds_dict, match_dict):
	
	key_list = find_key(odds_dict)
	
	key_del_finish = del_key_match_finish(key_list, match_dict)
	
	key_time_2 = get_key_match_time(key_del_finish, match_dict)
	
	key_final = del_key_next_day_match(key_time_2, match_dict)
	
	return key_final

#[brief]:	delete the match finished	
#[input]:	match_info(dict)
#[output]:	match_finished(dict)
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

#[brief]:	delete the match finished	
#[input]:	match_info(dict)
#			odds(list)
#[output]:	match_finished(dict)
def get_final_odds(match_info, odds):
	odds_ret = []
	
	for e in odds:
		if e in match_info.keys():
			odds_ret.append(e)
	
	print(odds_ret)
	return odds_ret

#[brief]:	select the match finished ,and odds is appropriate, for analyse	
#[input]:	odds_dict(dict)
#			match_dict(dict)
#[output]:	odds(list)	
def get_match_finished_parse(odds_dict, match_dict):

	odds = find_key(odds_dict)
	
	match_finished = get_match_finished(match_dict)
	
	odds = get_final_odds(match_finished, odds)
	
	return odds
	
if __name__ == "__main__":
	from soccer_comm import print_help
	from read_match_data import read_match_data, read_match_odds
	
	print_help()
	url_choice = input('please choice url:')
	
	match_dict = read_match_data(url_choice)
	odds_dict = read_match_odds(url_choice)
	if match_dict is None:
		print('read_match_data() Fail!!')
		sys.exit()	
	
	#get_key_final(odds_dict, match_dict)	
	get_match_finished_parse(odds_dict, match_dict)
		
		
		
		
		
		
		
		
		
		
		
		
		