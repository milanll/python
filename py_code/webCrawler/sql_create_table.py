
from sql_manage import sql_create_tabel		#sql_create_tabel(sql_cmd)

#联合主键
#CREATE TABLE STUDENTS (subjectId TEXT,studentid TEXT,studentname TEXT, constraint pk_id primary key (subjectId,studentid))

sql_cmd_create_table_1 = "create table table_1(match_sequence varchar(19) unique primary key not null,\
										match_type varchar(8),\
										match_date varchar(5),\
										match_time varchar(5),\
										match_status varchar(4),\
										team_one varchar(16),\
										score varchar(5),\
										team_two varchar(16),\
										match_result_half varchar(2),\
										match_result_finnal varchar(2),\
										home_team_odds int,\
										draw_odds int,\
										visiting_team_odds int);"

										
sql_cmd_create_table_2 = "create table table_2(match_sequence varchar(19),\
										match_type varchar(8),\
										match_date varchar(5),\
										match_time varchar(5),\
										match_status varchar(4),\
										team_one varchar(16),\
										score varchar(5),\
										team_two varchar(16),\
										match_result_half varchar(2),\
										match_result_finnal varchar(2),\
										home_team_odds int,\
										draw_odds int,\
										visiting_team_odds int,\
										constraint pk_id primary key (match_sequence,team_one,team_two));"

'''
"lid":lid,
"sid":sid,
"fid":fid,
"infoid":infoid,
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
										
sql_cmd_create_table_3 = "create table table_3(\
										lid int,\
										fid int,\
										sid int,\
										infoid int,\
										match_sequence varchar(19),\
										match_type varchar(8),\
										match_date varchar(5),\
										match_time varchar(5),\
										match_status varchar(4),\
										team_one varchar(16),\
										score varchar(5),\
										team_two varchar(16),\
										match_result_half varchar(2),\
										match_result_finnal varchar(2),\
										home_team_odds int,\
										draw_odds int,\
										visiting_team_odds int,\
										constraint pk_id primary key (lid,fid,infoid));"
										
'''
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
			'lid'	: v['lid'],
			'fid'	: v['fid'],
			'sid'	: v['sid'],
			'infoid': v['infoid']
'''
sql_cmd_create_table_4 = "create table table_5(\
										match_sequence varchar(9),\
										match_type varchar(8),\
										match_round varchar(6),\
										match_date varchar(5),\
										match_time varchar(5),\
										match_status varchar(4),\
										match_result_finnal varchar(2),\
										team_one varchar(16),\
										score varchar(5),\
										team_two varchar(16),\
										match_result_half varchar(5),\
										home_team_odds float,\
										draw_odds float,\
										visiting_team_odds float,\
										lid int,\
										fid int,\
										sid int,\
										infoid int,\
										constraint pk_id primary key (lid,fid,infoid));"

sql_create_tabel(sql_cmd_create_table_4) 


