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

	filter_1(stock_data)
	filter_2(stock_data)
	filter_3(stock_data)
	filter_4(stock_data)
	filter_5(stock_data)
#	filter_6(stock_data)
	filter_7(stock_data)
#	filter_9(stock_data)