from filter_1 import *
from filter_2 import *
from filter_3 import *
from filter_4 import *
from filter_5 import *
from filter_6 import *
from filter_7 import *
from filter_9 import *
from _date import *

start_date, end_date = get_x_trade_days(x_trade_days)

#[brief]    get key list file name
def get_key_list_file_name():
    return f'key_list_{end_date}.json'
 
 
#[brief]    get key list file direct
def get_key_list_file_dir():
    return f'./sync_data/key_list_{end_date}.json'


#[brief]    save list to json file
#[input]    key_list_dict(dict)
#[return]   file_json(str)  the json file of the chosen stock key list
def save_key_list_list(key_list_dict):
    dir = 'E:\\git\\python\\py_code\\stock\\sync_data\\'
    files = file_name(dir)

    file_json = get_key_list_file_name()
    file_json_dir = get_key_list_file_dir()

    if (files is None) or (file_json not in files):     
        with open(file_json_dir, 'w') as f:
            data_dict = json.dumps(key_list_dict)
            json.dump(data_dict, f)
            f.close()
        print('Save \'%s\' successfully!!!' % file_json)
    else:
        print('\'%s\' exsit!!!\n' % file_json)

    return file_json

#[breif]    push the key list file (up to date) to git
def push_key_list_file_to_git():
    #file = get_key_list_file_dir()
    file = 'sync_data/key_list_2020-04-23.json'
    print(file)
    
    import os
    os.system(f'git add {file}')
    os.system('git commit . -m \'update\'')
    os.system('git push')


#[brief]    push the file to git
#[input]    file_name(str)
def git_push(file_name):
    os.system(f'git add {file_name}')
    os.system(f'git commit {file_name}')
    os.system('git push')
    
if __name__ == "__main__":
    key_list_dict = {}
    
    if 0:
        stock_data = get_hist_data_()

        key_list_1 = filter_1(stock_data)
        key_list_2 = filter_2(stock_data)
        key_list_3 = filter_3(stock_data)
        key_list_4 = filter_4(stock_data)
        key_list_5 = filter_5(stock_data)
        key_list_7 = filter_7(stock_data)

        key_list_dict['filter_1'] = key_list_1
        key_list_dict['filter_2'] = key_list_2
        key_list_dict['filter_3'] = key_list_3
        key_list_dict['filter_4'] = key_list_4
        key_list_dict['filter_5'] = key_list_5
        key_list_dict['filter_7'] = key_list_7

        save_key_list_list(key_list_dict)
        
    else:
        push_key_list_file_to_git()
    
    
    
    
    
    