import re
import requests
from lxml import etree
import json
import time
import os
from time_manage import get_time_stamp
names = {
	"sp": "胜负奖金",
	"rqsp": "让球奖金",
	'0':"平均欧赔",
	"293": "威廉希尔",
	"5": "澳门彩票",
	"3":"bet365",
	"280": "皇冠",
}

def get_id():
	"""
		>>> get_id('http://live.500.com/')
		json out file to now path live.json
	:param url:
	:return:
	"""
	url = 'http://live.500.com/'
	try:
		html_text = requests.get(url).content.decode('gbk')
		x_response = etree.HTML(html_text)
		'''
		读取liveOddsList
		liveOddsList={
		"687616":{"0":[5.07,3.37,1.77],"3":[5.25,3.29,1.8],"5":[4.0,3.5,1.75],"rqsp":[2.02,3.20,3.11],"sp":[5.15,3.15,1.62],"280":[5.2,3.35,1.83],"1055":[5.5,3.48,1.81],"293":[5.5,3.25,1.75]}，
		"690176":{"0":[1.26,5.88,10.33],"3":[1.25,6.0,12.0],"5":[1.28,5.3,7.4],"rqsp":[2.55,4.10,2.03],"sp":[1.14,6.15,11.30],"280":[1.28,6.1,10.5],"1055":[1.28,6.34,12.01],"293":[1.25,6.0,11.0]}
		}
		'''
		id_dict = ''.join(re.findall(r'var.*?liveOddsList=(\{.*?\});', html_text, re.S))
		id_dict = json.loads(id_dict)
		
		#print(id_dict.keys())
		#print("element count:%d" % (len(id_dict)))
		data_dict = {}
		
		#liveOddsList中的某个key("687616","690176")值，在网页中有可能不存在，导致x_response.xpath(f'//tr[@fid="{key}"]/@gy')抛出异常。
		#所以，从网页中读取所有key值，然后再按key值查找。
		fid_list = x_response.xpath(f'//tr/@fid')
		
		for key in id_dict:
			# 比赛类型，球队一，球队二
			match_type, team_one_1, team_two_1 = x_response.xpath(f'//tr[@fid="{key}"]/@gy')[0].split(',')
		
	except:
		import traceback
		print(f"error: url: {url}\n")
		traceback.print_exc()
		time.sleep(10)

get_id()