
from sql_manage import sql_exec			#sql_exec(sql_cmd)

sql_cmd_match_finish = "select * from table_2 where match_status = '完' order by match_sequence;"

sql_cmd_match_bet = "select * from table_2 \
					where \
						match_status = '完' \
					and \
						home_team_odds < 1.80\
					and\
						home_team_odds >1.35\
					order by match_sequence;"
sql_cmd_match = "select * from table_2 where (match_date = '12-22' or match_date = '12-23') and score != '-' order by match_sequence;"	

sql_cmd_match_italy = "select count(*) from table_2 where match_type = '意甲' and score != '-';"	

sql_cmd_drop_table = "drop table table_4;"

sql_cmd_column_minus = "select sid - lid from table_3;"
			

sql_exec(sql_cmd_column_minus)