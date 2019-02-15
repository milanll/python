# -*- coding: UTF-8 -*-

import sys
sys.path.append("../py_comm")

from get_match_data import get_id
import re

'''
{
	"match_day":match_day,
	"match_order":match_order,
	"match_round": match_round,
	"match_status": match_status,
	"match_type":match_type,
	"match_date":match_date,				
	"match_time":match_time,
	"team_one": team_one,				
	"team_one_score": team_one_score,
	"team_two_score": team_two_score,
	"team_two": team_two,
	"match_result_half": match_result_half,
	"match_result_finnal": match_result_finnal,
	"match_score_finnal": match_score_finnal
}
'''

#[brief]	change the match result to 3,1,0, if the match finished.
#[input]	match_info(str)		{'736775': ..., {'match_result_half': '5-4'}, ...}
#[output]	match_info(str)		{'736775': ..., {'match_result_half': '3'}, ...}
def tanslate_score(match_info):
	
	for (k, v) in match_info.items():
		#match finished
		if '4' == v['match_status']:
			#half 
			score = v['match_result_half']
			score_home = re.search('(\d+)(.)(-)(.)(\d+)', score).group(1)
			score_visiting = re.search('(\d+)(.)(-)(.)(\d+)', score).group(5)
			score_int = int(score_home) - int(score_visiting)
			
			if score_int > 0:
				v['match_result_half'] = '3'
			elif score_int < 0:
				v['match_result_half'] = '0'
			else:
				v['match_result_half'] = '1'
			
			#finish
			score_1 = v['score']
			score_home_1 = re.search('(\d+)(-)(\d+)', score_1).group(1)
			score_visiting_1 = re.search('(\d+)(-)(\d+)', score_1).group(3)
			score_int_1 = int(score_home_1) - int(score_visiting_1)
			
			if score_int_1 > 0:
				v['match_result_finnal'] = '3'
			elif score_int_1 < 0:
				v['match_result_finnal'] = '0'
			else:
				v['match_result_finnal'] = '1'
			
			#print(v['team_one'], score_1, score_int_1, match_info[k]['match_result_finnal'])
		
	return match_info

def get_items_from_500(url):

	dict_item = {}
	dict_id, odds = get_id(url)

	i = 0
	for (k,v) in dict_id.items():
		if '平均欧赔' in v.keys():
			dict_item[v['fid']] = {
				'match_sequence'		: v['match_sequence'],
				'match_type'			: v['match_type'],
				'match_round'			: v['match_round'],
				'match_date'			: v['match_date'],
				'match_time'			: v['match_time'],
				'match_status'			: v['match_status'],
				'match_result_finnal'	: v['match_result_finnal'],
				'team_one'				: v['team_one'],
				'score'					: v['team_one_score'] + '-' + v['team_two_score'],
				'team_two'				: v['team_two'],
				'match_result_half'		: v['match_result_half'],
				'home_team_odds'		: v['平均欧赔'][0],
				'draw_odds'				: v['平均欧赔'][1],
				'visiting_team_odds'	: v['平均欧赔'][2],
				'lid':v['lid'],
				'fid':v['fid'],
				'sid':v['sid']
				#'infoid':v['infoid']
			}
		
		if 'zqdc.php' not in url:
			dict_item[v['fid']]["infoid"] = v['infoid']
		
		i += 1
	print('match number: %d\n' % (i))
	
	dict_item = tanslate_score(dict_item)
	#print(dict_item)		
	return dict_item, odds

def chinese(data):  
    count = 0  
    for s in data:  
        if ord(s) > 127:  
            count += 1  
    return count  
'''  
print('----通过函数计算长度格式化：----')  
for x in range(len(c)):  
    number = chinese(c[x])  
    newStr = '{0:{wd}}'.format(c[x],wd=20-number)  
    print('|%s|' % newStr) 
'''	
def parse_items(dict_id):
	for (k,v) in dict_id.items():
		#if(v['match_type'] == '法甲'):
		print(v.items())

def display_match_result(dict_id):
	for (k,v) in dict_id.items():
		#print("%-10s%-10s%s%s%s%s" % (v['match_type'],v['team_one'],v['team_one_score'],'-',v['team_two_score'],v['team_two']))
		number = chinese(v['match_type'])  
		newStr = '{0:{wd}}'.format(v['match_type'],wd=20-number)  
		print("%s" % newStr)

#display_match_result(dict_id)
#parse_items(dict_id)


def print_items(dict_item):
	#for i in range(0,len(dict_item)):
	for (k,v) in dict_item.items():
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
			print(v['match_date'].ljust(5),v['match_status'].ljust(2),v['team_one'].ljust(16), v['match_result_half'].ljust(2), v['match_result_finnal'].ljust(2))
		
def count_match_finish(match_dict):
	i = 0
	j = 0
	for(k,v) in match_dict.items():
		if v['match_status'] == u'完':
			i += 1
		else:
			j += 1
	print('match_not_finish:%d, match_finish:%d' % (i,j))
	return i, j

if __name__ == '__main__':
	url_dch = "http://live.500.com/zqdc.php"
	dict_item, odds = get_items_from_500(url_dch)
	print_items(dict_item)
	#count_match_finish(dict_item)









