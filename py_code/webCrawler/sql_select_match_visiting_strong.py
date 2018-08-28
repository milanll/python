
from sql_manage import sql_exec	#sql_exec(sql_cmd)

sql_cmd = "select * from table_2 where visiting_team_odds < 2.36;"

sql_exec(sql_cmd)