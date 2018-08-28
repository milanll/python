
#打印help
def print_help():
	print('精彩比分：jc')
	print('单场比分：dch')

#打印match_status
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
#打印match_data		
def print_match_data(match_result_dict):

	print_match_status_usage()
	
	i = 0
	for (key, v) in match_result_dict.items():
		#print(key.ljust(10),v['match_date'].ljust(8),v['match_status'].ljust(2),v['match_result_finnal'].ljust(2),v['team_one'].ljust(16))
		print('%-4s%-8s%6s%4s%4s%-16s' % (i,key,v['match_date'],v['match_status'],v['match_result_finnal'],v['team_one']))
		i += 1
		pass


#打印match_result		
def print_match_result(match_result_dict, odds_dict):

	print_match_status_usage()
	
	i = 0
	for (key, v) in match_result_dict.items():
		#print(key.ljust(10),v['match_date'].ljust(8),v['match_status'].ljust(2),v['match_result_finnal'].ljust(2),v['team_one'].ljust(16))
		print('%-4s%-8s%6s%4s%4s%-20s%-16s%+16s' % (i,key,v['match_date'],v['match_status'],v['match_result_finnal'],odds_dict[key]['0'],v['team_one'],v['team_two']))
		i += 1
		pass

#打印odds
def print_match_odds(odds_dict):
	for (key, v) in odds_dict.items():
		print(key, v['0'])





