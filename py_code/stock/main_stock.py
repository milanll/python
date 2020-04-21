from filter_1 import *
from filter_2 import *
from filter_3 import *
from filter_4 import *
from filter_5 import *
from filter_6 import *
from filter_7 import *
from filter_9 import *

if __name__ == "__main__":
	stock_data = get_hist_data_()

	key_1 = filter_1(stock_data)
	key_2 = filter_2(stock_data)
	key_3 = filter_3(stock_data)
	key_4 = filter_4(stock_data)
	key_5 = filter_5(stock_data)
#	key_6 = filter_6(stock_data)
	key_7 = filter_7(stock_data)
#	key_9 = filter_9(stock_data)

    key_dict = {}
    key_dict['filter_1'] = key_1
    key_dict['filter_2'] = key_2
    key_dict['filter_3'] = key_3
    key_dict['filter_4'] = key_4
    key_dict['filter_5'] = key_5
    key_dict['filter_6'] = key_6
    key_dict['filter_7'] = key_7
    key_dict['filter_9'] = key_9