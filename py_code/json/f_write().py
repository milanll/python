
import os
import json
from time_manage import get_time_stamp		#get_time_stamp()
from get_match_data import get_id			#get_id(url)


dict_items = get_id('http://live.500.com')

time_str = get_time_stamp()

with open(f'./match_data/{time_str}.json', 'wb') as f:
	f.truncate()
	f.write(json.dumps(dict_items, ensure_ascii=False).encode())
	# json.dump(f, dict_items), ensure_ascii=False)

print(f"OK!!\ndata file path: {os.getcwd()}\match_data/{time_str}.json")