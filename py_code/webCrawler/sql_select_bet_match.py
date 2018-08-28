
from sql_manage import sql_exec		#sql_exec(sql_cmd)

sql_cmd = "select * from table_2\
			where\
					((home_team_odds < 1.80\
					and\
					home_team_odds >1.35)\
				or\
					(visiting_team_odds < 2.0\
					and\
					visiting_team_odds > 1.35))\
			and\
				(match_date = '12-22'\
				or\
				match_date = '12-23')\
			order by match_sequence;"

sql_exec(sql_cmd)