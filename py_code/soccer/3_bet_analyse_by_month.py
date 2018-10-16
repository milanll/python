##################		analyse the bet money group by month		###########################################
#Author: 	chenll
#Date: 		2018-10-15

import csv
import copy
from datetime import datetime

import sys;
sys.path.append("../py_comm")
from py_time import get_month_from_date
from py_csv import open_csv
from soccer_comm import PY_CODE
from soccer_comm import C_CODE
from soccer_comm import read_record

#order bet_data by month
#[input]: data(dict)		{date:[count, cost]}
#return	: data_month(dict)	{month:[[count, cost], [count, cost], ....]}
def order_data_by_month(data):
	i = j = 0
	count = cost = 0
	data_month = {}
	data_day = []
	data_day_1 = []
	data_one_month = []
	data_one_month_1 = []
	m = 0

	for (k, v) in data.items():
		count = v[0].strip('\t')
		cost = v[1].strip('\t')
		m += 1
		
		data_day.clear()
		data_day_1.clear()

		#the first item
		if i == 0:
			i = get_month_from_date(k)
			j = i
			data_day.append(count)
			data_day.append(cost)
			data_day_1 = copy.deepcopy(data_day)
			data_one_month.append(data_day_1)
		#other item
		else:
			i = get_month_from_date(k)
			if i == j:
				data_day.append(count)
				data_day.append(cost)
				data_day_1 = copy.deepcopy(data_day)
				data_one_month.append(data_day)
			else:
				data_one_month_1 = copy.deepcopy(data_one_month)
				data_month[j] = data_one_month_1
				#print(data_month.items())
				data_one_month.clear()

				j = i
				data_day.append(count)
				data_day.append(cost)
				data_day_1 = copy.deepcopy(data_day)
				data_one_month.append(data_day)
	
	#add data of last month
	data_month[i] = data_one_month
	print(m)
	print(data_month.values())
	return data_month

#calculate profit every month
#[input]:	data_month(dict)	{month:[count,count, ......]}
#[output]:  profit_month(dict)	{month:profit}
def calc_profit_every_month(data_month):
	profit_month = {}
	for (k, v) in data_month.items():
		profit = int(v[-1]) - int(v[0])
		profit_month[k] = profit
	
	print(profit_month)
	return profit_month

if __name__ == '__main__':
	filename = PY_CODE + '/soccer/bet_record/bet_record_week_18-19.csv'
	reader = open_csv(filename)
	data = read_record(reader)

	data_month = order_data_by_month(data)
	#profit_month = calc_profit_every_month(data_month)
	#draw_chart(data)
	#read_data_every_month(dates)

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	