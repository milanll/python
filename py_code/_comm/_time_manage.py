
import datetime
import time

def time_compare_am10():
	'''
	功能：	比较当前时间是10之前，还是10点之后
	返回：	< 0，10点之前
			> 0，10点之后
	'''
	strTime_10 = time.strftime("%Y%m%d",time.localtime()) + '100000'
	strTime_now = time.strftime("%Y%m%d%H%M%S",time.localtime())

	#print(strTime_10,strTime_now)

	#字符串变成时间数据结构
	struTime_10 = time.strptime(strTime_10,'%Y%m%d%H%M%S')
	struTime_now = time.strptime(strTime_now,'%Y%m%d%H%M%S')

	#从时间数据结构转换成时间戳
	time_10 = time.mktime(struTime_10)
	time_now = time.mktime(struTime_now)

	#时间戳可以直接相减，得到以秒为单位的差额
	return time_now - time_10

def get_time_stamp():
	time_now = time.strftime("%Y-%m-%d",time.localtime())
	if(time_compare_am10() < 0):
		time_str = time_now + '_match_result'
	else:
		time_str = time_now + '_match'
	
	return time_str

	
def get_next_day_am9():
	today = datetime.date.today()
	tomorrow = today + datetime.timedelta(days=1)
	yestoday = today - datetime.timedelta(days=1)
	
	tomorrow = tomorrow.strftime('%Y-%m-%d')
	next_am9 = tomorrow + ' ' + '09:00:00'
	next_am9 = datetime.datetime.strptime(next_am9, "%Y-%m-%d %H:%M:%S")
	
	return next_am9

#Return：True(before am9:00 next day),False(after am9:00 next day)	
def compare_to_next_am9(time):
	next_am9 = get_next_day_am9()
	
	if time > next_am9:
		return True
	else:
		return False

#
def date_time_struct(date, time):
	year = datetime.datetime.now().year
	date = str(year) + '-' + date + ' ' + time
	date = datetime.datetime.strptime(date,"%Y-%m-%d %H:%M:%S")

	return date
	
	
if __name__ == "__main__":
	#time  = datetime.datetime.now()
	#compare_to_next_am9(time)
	date_time_stuct('10-18', '10:00:00')
	print(time)
	
	









	
	
	