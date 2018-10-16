
##################		analyse the bet result		###########################################
#Author: 	chenll
#Date: 		2018-10-15


# -*- coding:utf-8 -*-
import copy

import sys
sys.path.append("../py_comm")
from py_csv import open_csv
from soccer_comm import PY_CODE
from soccer_comm import read_result

#print bet_data
def print_bet_data(list):
	total_earning_rate = 0
	#DATE,			Bet Number,		Result_A,	Result_B,	Bet Money,	Money Obtained
	#2018-10-11,	2018-10-001,	3,			3,			90,			140
	print('DATE\t\tBet Number\tEarning Rate\tResult_A\tResult_B\tMoney Bet\tSeed Money\tEarning Money')
	for e in list:
		print("%s\t%s\t%s\t\t%s\t\t%s\t\t%s\t\t%s\t\t\t" % (e[0],e[1],e[8],e[2],e[3],e[4],e[5]),e[6])
		total_earning_rate = total_earning_rate + e[8] - 1
	
	print("\nTotal Earning Rate: %.2f\n" % total_earning_rate)
	print("Sum of Bet Groups: %d\n" % len(list))
	print("Average Earning Rate: %.2f" % round(total_earning_rate/len(list), 2))

		
#read data from bet_result_record_18-19.csv, caculate yield rate
#[input]:	bet_result(list)	[Date,Bet Number, Result_A, Result_B, Bet Money, Seed Money, Earning Money, Team]
#[output]:	bet_data(list)		[Date,Bet Number, Result_A, Result_B, Bet Money, Seed Money, Earning Money, Team, Earning Rate]
def analyse_bet_result(bet_result):
	#	0				1				2			3			4			5			6			7
	#DATE,			Bet Number,		Result_A,	Result_B,	Bet Money,	Seed Money,	Earning Money,	Team
	#2018-10-11,	2018-10-001,	3,			1,			85,			27,			112,			鹿岛鹿角
	#2018-10-12,	2018-10-002,	3,			3,			50,			50,			75,				浦和红钻
	#2018-10-12,	2018-10-002,	1,			3,			85,			0,			0,				全北现代
		
	bet_data = []
	data = []
	for row in bet_result:
		data.clear()

		#get one row data
		for r in row:
			r = r.strip('\t')
			data.append(r);
		
		#caculate the result of one bet
		result_a = int(row[2])
		result_b = int(row[3])
		result = result_a * result_b
		
		earning_money = int(row[6])
		seed_money = int(row[5])
		bet_money = int(row[4])
		if result > 1:
			odds_obtain = round( (earning_money + seed_money) / bet_money, 2)
		else:
			odds_obtain = 0
		
		#Earning Rate
		data.append(odds_obtain)
		
		data_1 = copy.deepcopy(data)
		#add every row to bet_data(list)
		bet_data.append(data_1)
	
	return bet_data


if __name__ == '__main__':
	filename = PY_CODE + '/soccer/bet_record/bet_result_record_18-19.csv'
	reader = open_csv(filename)
	bet_data = read_result(reader)
	data = analyse_bet_result(bet_data)
	print_bet_data(data)

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	