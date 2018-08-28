
# -*- coding: utf-8 -*-

#from get_match_data import get_id			#get_id(url)
import read_match_data
import soccer_comm
import re

soccer_comm.print_help()
choice = input('please choice url:')

match_data_dict, odds_dict = read_match_data.read_match_data(choice)

print('\n')
for (k,v) in match_data_dict.items():
	if ']' in v['team_one']:
		team_one = re.split(r']',v['team_one'])
		v['team_one'] = team_one[1]

#
for (k,v) in match_data_dict.items():
	if '[' in v['team_two']:
		team_two = re.findall(u"[\u4e00-\u9fa5]+",v['team_two'])
		v['team_two'] = team_two[0]
		
for (k,v) in match_data_dict.items():
	#print(soccer_comm.myAlign(v["team_one"], 20) + soccer_comm.myAlign(v['team_two'], 10))
	print("{0:<2}\t{1:{3}<8}\t{2:{3}<8}\t".format(len(v["team_one"]),v["team_one"],v['team_two'],chr(12288)))
















