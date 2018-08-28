# -*- coding: UTF-8 -*-

from get_match_data import get_id

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

def get_items_from_500(url):

	dict_item = {}
	dict_id, odds = get_id(url)
	
	i = 0
	for (k,v) in dict_id.items():
		#dict_item[i] = {
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
		
		print(v['match_date'].ljust(8),v['match_status'].ljust(2),v['team_one'].ljust(16))
		
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
	dict_item = get_items_from_500(url_dch)
	#print_items(dict_item)
	count_match_finish(dict_item)









