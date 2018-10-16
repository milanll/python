
import sys
sys.path.append("../py_comm")
import py_time



#选择合适的场次的key，根据赔率
def find_key(dict):
	key = []
	i = 0
	
	for (k, v) in dict.items():
		#print(k,v)
		#防止赔率列表中没有平局赔率(key='0')一项
		if('0' in v):
			#选择主场赔率在[1.3,1.8]之间，和客场赔率在[1.3,2.0]之间的比赛场次，保存赔率。
			if ((v['0'][0] < 1.8) and (v['0'][0] > 1.4)) or ((v['0'][2] < 2.0) and(v['0'][2] > 1.4)):
				key.append(k)
			else:
				i += 1
		else:
			i += 1
	print('\n', sys._getframe().f_code.co_name)
	print('odds_del_key_count: %d' % i)
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
	print('key_temp len: ', len(key_temp))
	for key in key_temp:
		del key_time_1[key]

	#print('\n',key_time_1.keys())
	print('key_final:',len(key_time_1))
	print(key_time_1.keys())
		
	return key_time_1

#将key同比赛时间关联起来，生成一个新的字典key_time	
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
		'''
		match status:
			0	Unplayed match
			3  	Ongoing match
			4   Finishied match
			6 	Delayed match
		'''
		if '0' != match_dict[key]['match_status']:
			key_temp.append(key)
			i += 1
	
	print('del_key_count: ', i)
	print('loop count: ', j)
	
	for key in key_temp:
		key_list.remove(key)
		
	print('key_list_1:', len(key_list))	
		
	return key_list