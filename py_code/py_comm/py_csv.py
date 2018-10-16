import csv

#filename = 'F:/Jupyter Notebook/matplotlib_pygal_csv_json/sitka_weather_2014.csv'
#[input]: 	fielname(str)
#return: 	reader(csv reader)
def open_csv(filename):
	f =  open(filename, 'r', encoding = 'utf-8')
	reader = csv.reader(f)
	#print(list(reader))
	return reader

if __name__ == '__main__':
	PY_CODE = 'E:/git/python/py_code'
	C_CODE = 'E:/git/python/c_code'

	filename = PY_CODE + '/soccer/bet_record/bet_record_week_18-19.csv'
	reader = open_csv(filename)
	read = next(reader)