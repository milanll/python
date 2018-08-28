
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