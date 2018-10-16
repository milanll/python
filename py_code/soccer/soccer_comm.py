
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
	0				1			2		3
	Data,			Balance,	Cost,	Mark	
	2018-10-9,		310,		200,	0
	2018-10-11,		742,		500,	0
	2018-10-17,		351,		-700,	15号提取700
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
	
	
	
	
'''

from matplotlib import pyplot as plt
from datetime import datetime

 
#根据数据绘制图形
fig=plt.figure(dpi=128,figsize=(10,6))
plt.plot(dates,highs,c='red',alpha=0.5)#实参alpha指定颜色的透明度，0表示完全透明，1（默认值）完全不透明
plt.plot(dates,lows,c='blue',alpha=0.5)
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1) #给图表区域填充颜色
plt.title('Daily high and low temperature-2004',fontsize=24)
plt.xlabel('',fontsize=16)
plt.ylabel('Temperature(F)',fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=16)
fig.autofmt_xdate()  #绘制斜的日期标签
plt.show()


(1)figure语法说明

figure(num=None, figsize=None, dpi=None, facecolor=None, edgecolor=None, frameon=True)

num:图像编号或名称，数字为编号 ，字符串为名称
figsize:指定figure的宽和高，单位为英寸；
dpi参数指定绘图对象的分辨率，即每英寸多少个像素，缺省值为80
facecolor:背景颜色
edgecolor:边框颜色
frameon:是否显示边框

(2) 绘制曲线
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import spline
 
T = np.array([6, 7, 8, 9, 10, 11, 12])
power = np.array([1.53E+03, 5.92E+02, 2.04E+02, 7.24E+01, 2.72E+01, 1.10E+01, 4.70E+00])
xnew = np.linspace(T.min(),T.max(),300) #300 represents number of points to make between T.min and T.max
 
power_smooth = spline(T,power,xnew)
 
plt.plot(xnew,power_smooth)
plt.show()

(3)设置坐标轴刻度

my_x_ticks = np.arange(-5, 5, 0.5)      #显示范围为-5至5，每0.5显示一刻度
my_y_ticks = np.arange(-2, 2, 0.2)      #显示范围为-2至2，每0.2显示一刻度
plt.xticks(my_x_ticks)
plt.yticks(my_y_ticks)

(4)设置网格
matplotlin.pyplot.grid(b, which, axis, color, linestyle, linewidth， **kwargs)

grid()参数有很多，这里只列举了我此次工作中用到的几个：

    b : 布尔值。就是是否显示网格线的意思。官网说如果b设置为None， 且kwargs长度为0，则切换网格状态。但是没弄明白什            么意思。如果b设置为None，但是又给了其它参数，则默认None值失效。

    which : 取值为'major', 'minor'， 'both'。 默认为'major'。看别人说是显示的我的是Windows7下，用Sublime跑的，minor                 只是一个白画板，没有网格，major和both也没看出什么效果，不知道为什么。

    axis : 取值为‘both’， ‘x’，‘y’。就是想绘制哪个方向的网格线。不过我在输入参数的时候发现如果输入x或y的时候，             输入的是哪条轴，则会隐藏哪条轴

    color : 这就不用多说了，就是设置网格线的颜色。或者直接用c来代替color也可以。

    linestyle :也可以用ls来代替linestyle， 设置网格线的风格，是连续实线，虚线或者其它不同的线条。 | '-' | '--'                        | '-.' | ':' | 'None' | ' ' | '']

    linewidth : 设置网格线的宽度

'''
#draw chart according to dict
#param [in]: data(dict)
def draw_chart(data):
	import matplotlib.pyplot as plt #importing matplot lib library
	import numpy as np
	from scipy.interpolate import spline

	fig=plt.figure(dpi=80,figsize=(10,6))
	x = data.keys()
	y = data.values()

	print(len(x))
	plt.plot(x,y) #plotting x and y
	fig.autofmt_xdate()  #绘制斜的日期标签

	#设置网格
	plt.grid(axis = 'y')
	plt.show()
	
if __name__ == '__main__':
	filename = PY_CODE + '/soccer/bet_record/bet_record_week_18-19.csv'
	reader = open_csv(filename)
	read_record(reader)



