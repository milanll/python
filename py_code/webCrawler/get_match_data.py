import re
import requests
from lxml import etree
import json
import time
import os

names = {
	"sp": "胜负奖金",
	"rqsp": "让球奖金",
	'0':"平均欧赔",
	"293": "威廉希尔",
	"5": "澳门彩票",
	"3":"bet365",
	"280": "皇冠",
}

def check_http(url):
	if 'http' not in url:
		url = 'http://' + url
	return url

def get_id(url):
	"""
	>>> get_id('http://live.500.com/')
	json out file to now path live.json
	:param url:
	:return:
	"""

	url = check_http(url)

	try:
		html_text = requests.get(url).content.decode('gbk')
		x_response = etree.HTML(html_text)
		id_dict = ''.join(re.findall(r'var.*?liveOddsList=(\{.*?\});', html_text, re.S))
		id_dict = json.loads(id_dict)
		data_dict = {}
		for key in id_dict:
			# 比赛类型，球队一，球队二
			try:
				match_type, team_one_1, team_two_1 = x_response.xpath(f'//tr[@fid="{key}"]/@gy')[0].split(',')
			except:
				continue
			# 球队一得分
			team_one_score = ''.join(x_response.xpath(f'//tr[@fid="{key}"]/td/div[@class="pk"]/a[1]/text()'))
			# 球队二得分
			team_two_score = ''.join(x_response.xpath(f'//tr[@fid="{key}"]/td/div[@class="pk"]/a[3]/text()'))
			# 比赛日
			match_sequence = ''.join(x_response.xpath(f'//tr[@fid="{key}"]/td[1]/text()'))
			# 比赛场次
			# match_order_1 = ''.join(x_response.xpath(f'//tr[@fid="{key}"]/td[2]/text()'))
			# 比赛轮次
			match_round = ''.join(x_response.xpath(f'//tr[@fid="{key}"]/td[3]/text()'))
			# 比赛时间
			match_time_1 = ''.join(x_response.xpath(f'//tr[@fid="{key}"]/td[4]/text()'))
			# 比赛状态
			match_status_1 = ''.join(x_response.xpath(f'//tr[@fid="{key}"]/td[5]/text()'))
			match_status_2 = ''.join(x_response.xpath(f'//tr[@fid="{key}"]/td/span[@class="red"]/text()'))
			# 全场比分
			match_score_finnal = ''.join(x_response.xpath(f'//tr[@fid="{key}"]/td/div[@class="pk"]/a[2]/text()'))
			# 半场结果
			match_result_half = ''.join(x_response.xpath(f'//tr[@fid="{key}"]/td[@class="red"][1]/text()'))
			# 全场结果
			match_result_finnal = ''.join(x_response.xpath(f'//tr[@fid="{key}"]/td[@class="red"][2]/text()'))
			# 球队排名
			team_ranking = ''.join(x_response.xpath(f'//tr[@fid="{key}"]/td[@class="p_lr01"]/span[@class="gray"]/text()'))
			
			#lid 联赛id
			lid = x_response.xpath(f'//tr[@fid="{key}"]/@lid')
			#fid 联赛id
			fid = x_response.xpath(f'//tr[@fid="{key}"]/@fid')
			#sid 联赛场次id
			sid = x_response.xpath(f'//tr[@fid="{key}"]/@sid')
			#infoid 比赛id
			infoid =x_response.xpath(f'//tr[@fid="{key}"]/@infoid')
			# 拆分比赛日和比赛场次
			match_day = match_sequence[0:2]
			match_order = match_sequence[2:5]

			# 拆分比赛日期和比赛时间
			match_date = match_time_1[0:5]
			match_time = match_time_1[6:11]

			# 拆分‘周三’‘001’
			team_one_ranking = team_ranking[0:4]
			team_two_ranking = team_ranking[4:8]
			team_one = team_one_ranking + team_one_1
			team_two = team_two_1 + team_two_ranking

			if match_status_1:
				match_status = match_status_1
			else:
				match_status = match_status_2
			try:
				data_dict[f"{match_type}_{team_one} vs {team_two}"] = {
					"lid":lid[0],
					"sid":sid[0],
					"fid":fid[0],
					"infoid":infoid[0],
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
				}
				
			except:
				continue

			for _key in id_dict[key]:
				try:
					name_ = names[str(_key)]
				except:
					continue
				data_dict[f"{match_type}_{team_one} vs {team_two}"].update(**{name_:id_dict[key][_key]})
			#break
		#print(data_dict)

		#time.sleep(10)
		return data_dict
	except:
		import traceback
		print(f"error: url: {url}\n")
		traceback.print_exc()
		time.sleep(10)

#get_id(input('url: '))
#get_id('http://live.500.com')


