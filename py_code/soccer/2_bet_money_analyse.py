##################		analyse the bet money		###########################################
#Author: 	chenll
#Date: 		2018-10-15

import sys;
sys.path.append("../py_comm")
from py_csv import open_csv
from soccer_comm import PY_CODE
from soccer_comm import read_record
from soccer_comm import draw_chart

#[input]:	data(dict)		{date:[count, cost]}
#[output]:	profit(dict)	{date:profit}
def calculate_profit(data):
	count = cost = 0
	profit = {}
	for (k, v) in data.items():
		cost += int(v[1])
		count = int(v[0]) - cost
		profit[k] = count
	print(profit)	
	return profit
		
if __name__ == '__main__':
	filename = PY_CODE + '/soccer/bet_record/bet_record_week_18-19.csv'
	reader = open_csv(filename)
	data = read_record(reader)
	profit = calculate_profit(data)
	draw_chart(profit)

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	