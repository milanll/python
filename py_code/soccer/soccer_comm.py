
import sys
import copy
sys.path.append("../py_comm")
from py_csv import open_csv

#print help
def print_help():
	print('精彩比分：jc')
	print('单场比分：dch')

#print match_status
def print_match_status_usage():
	print('\nmatch_status:')
	print('0    Unplayed match\n3    Ongoing match\n4    Finishied match\n6    Delayed match\n')
			
def print_match_odds(odds_dict):
	for (key, v) in odds_dict.items():
		print(key, v['0'])

'''
	"lid":lid[0],
	"sid":sid[0],
	"fid":fid[0],
	"match_sequence":match_sequence,
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
'''		
#print match_data		
def print_match_data(match_result_dict):

	print_match_status_usage()
	
	i = 0
	for (key, v) in match_result_dict.items():
		#print(key.ljust(10),v['match_date'].ljust(8),v['match_status'].ljust(2),v['match_result_finnal'].ljust(2),v['team_one'].ljust(16))
		print('%-4s%-8s%6s%4s%4s%-16s' % (i,key,v['match_date'],v['match_status'],v['match_result_finnal'],v['team_one']))
		i += 1
		pass


#print match_result		
def print_match_result(match_result_dict, odds_dict):

	print_match_status_usage()
	
	i = 0
	for (key, v) in match_result_dict.items():
		#print(key.ljust(10),v['match_date'].ljust(8),v['match_status'].ljust(2),v['match_result_finnal'].ljust(2),v['team_one'].ljust(16))
		print('%-4s%-8s%6s%4s%4s%-20s%-16s%+16s' % (i,key,v['match_date'],v['match_status'],v['match_result_finnal'],odds_dict[key]['0'],v['team_one'],v['team_two']))
		i += 1
		pass

#print odds
def print_match_odds(odds_dict):
	for (key, v) in odds_dict.items():
		print(key, v['0'])


#######################################	COMMON MACRO	#################################################
PY_CODE = 'E:/git/python/py_code'
C_CODE = 'E:/git/python/c_code'



#read csv files

#read data from bet_record.csv, return return the content
#[input]:	reader(csv reader)
#[output]:	bet_data(dict)	{date:[count, cost]}
def read_record(reader):
	'''
	0				1			2		3
	Data,			Balance,	Cost,	Mark	
	2018-10-9,		310,		200,	0
	2018-10-11,		742,		500,	0
	2018-10-17,		351,		-700,	15号提取700
	'''
		
	cost = 0
	bet_data = {}
	data = data_1 = []
	
	first_row = next(reader)
	if len(first_row) != 4:
		print('File length is :%d' % len(first_row))
		print('File is wrong!!!')
		return bet_data
	
	for row in reader:
		data.clear()
		
		if len(row) == 0:
			continue
		
		date = row[0]
		
		data.append(row[1])
		data.append(row[2])
		
		data_1 = copy.deepcopy(data)
		bet_data[date] = data_1
	
	#print(bet_data)
	return bet_data


#read data from bet_result_record.csv, return the content
#[input]:	reader(csv reader)
#[output]:	bet_data(list)	[Date,Bet Number, Result_A, Result_B, Bet Money, Seed Money, Earning Money, Team]
def read_result(reader):
	'''
	2018-10-14,		2018-10-010,	3,			3,			69,			30,			124,			松本山雅 & 千叶市原
	2018-10-14,		2018-10-011,	0,			0,			61,			0,			0,				沙佩科恩斯 & 克鲁塞罗
	2018-10-14,		2018-10-011,	3,			1,			95,			20,			113,			瑞士 & 白俄罗斯
	'''
		
	cost = 0
	bet_data = []
	data = data_1 = []
	
	first_row = next(reader)
	if len(first_row) != 8:
		print('File length is :%d' % len(first_row))
		print('File is wrong!!!')
		return bet_data

	for row in reader:
		data.clear()
		
		if len(row) == 0:
			continue
			
		data.append(row[0])
		data.append(row[1])
		data.append(row[2])
		data.append(row[3])
		data.append(row[4])
		data.append(row[5])
		data.append(row[6])
		data.append(row[7])

		data_1 = copy.deepcopy(data)
		bet_data.append(data_1)
	
	#print(bet_data)
	return bet_data
	
	
	
	

	
if __name__ == '__main__':
	filename = PY_CODE + '/soccer/bet_record/bet_record_week_18-19.csv'
	reader = open_csv(filename)
	read_record(reader)



