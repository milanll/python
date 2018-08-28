# -*- coding: UTF-8 -*-

from get_match_data import get_id
from sql_manage import sql_insert_into_table
from sql_manage import sql_select_all_from_table
from sql_manage import sql_select_item_from_table
from sql_manage import sql_update_table



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

def get_items_from_500():

	dict_item = {}
	dict_id = get_id('http://live.500.com')
	
	i = 0
	for (k,v) in dict_id.items():
		dict_item[i] = {
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
			'sid':v['sid'],
			'infoid':v['infoid']
		}
		
		i += 1
	print('match number: %d\n' % (i))		
	return dict_item

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
		#print(v['lid'],v['draw_odds'])
		for (m,n) in v.items():
			print(n)
#dict_item = get_items_from()

#print_items(dict_item)

#sql_insert_into_table('table_1',dict_item)

#sql_select_item_from_table('score','table_1')

#sql_update_table('table_1', dict_item, 'match_result_finnal')

#print('*' * 40)
#sql_select_item_from_table('score','table_1')







