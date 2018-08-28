
from sql_manage import sql_exec	#sql_exec(sql_cmd)

sql_cmd = "select * from table_2 where home_team_odds < 1.80;"

sql_exec(sql_cmd)