from filter_1 import *
from filter_2 import *
from filter_3 import *
from filter_4 import *
from filter_5 import *
from filter_6 import *
from filter_7 import *
from filter_9 import *
from _date import *

#[brief]    save list to json file
#[input]    key_list_dict(dict)
#[return]   file_json(str)  the json file of the chosen stock key list
def save_key_list_list(key_list_dict):
    start_date, end_date = get_x_trade_days(x_trade_days)

    dir = 'E:\\git\\python\\py_code\\stock\\sync_data\\'
    files = file_name(dir)

    file_json = f'key_list_list_{end_date}.json'
    file_json_dir = f'./sync_data/{file_json}'

    if (files is None) or (file_json not in files):     
        with open(file_json_dir, 'w') as f:
            data_dict = json.dumps(key_list_dict)
            json.dump(data_dict, f)
            f.close()
        print('Save \'%s\' successfully!!!' % file_json)
    else:
        print('\'%s\' exsit!!!\n' % file_json)

    return file_json

#[brief]    push the file to git
#[input]    file_name(str)
def git_push(file_name):
    os.system(f'git add {file_name}')
    os.system(f'git commit {file_name}')
    os.system('git push')
    
if __name__ == "__main__":
    stock_data = get_hist_data_()

    key_list_1 = filter_1(stock_data)
    key_list_2 = filter_2(stock_data)
    key_list_3 = filter_3(stock_data)
    key_list_4 = filter_4(stock_data)
    key_list_5 = filter_5(stock_data)
    key_list_7 = filter_7(stock_data)

    
    key_list_dict = {}
    key_list_dict['filter_1'] = key_list_1
    key_list_dict['filter_2'] = key_list_2
    key_list_dict['filter_3'] = key_list_3
    key_list_dict['filter_4'] = key_list_4
    key_list_dict['filter_5'] = key_list_5
    key_list_dict['filter_7'] = key_list_7

    save_key_list_list(key_list_dict)

    