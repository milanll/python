# -*- coding: utf-8 -*-   
      
import os, sys

#[brief]    get the file names of all the files under current direct
#[input]    file_dir(str)   'E:\\git\\python\\py_code\\stock\\data\\'
#[return]   files(list)     ['count_grow_2_days.csv', 'hist_data_2019-05-17.json', 'stock_basic_info.csv', 'stock_detail_info.csv']
def file_name(file_dir):
    
    for root, dirs, files in os.walk(file_dir):  
        #print(files) #当前路径下所有非目录子文件
        pass

    return files

##其中os.path.splitext()函数将路径拆分为文件名+扩展名        
def file_name_(file_dir):   
    L=[]   
    for root, dirs, files in os.walk(file_dir):  
        for file in files:  
            if os.path.splitext(file)[1] == '.jpeg':  
                L.append(os.path.join(root, file))  
    return L

#递归输出当前路径下所有非目录子文件
def listdir(path, list_name):  #传入存储的list
    for file in os.listdir(path):  
        file_path = os.path.join(path, file)  
        if os.path.isdir(file_path):  
            listdir(file_path, list_name)  
        else:  
            list_name.append(file_path)


if __name__ == '__main__':
    #print(sys.path[0])
    dir = 'E:\\git\\python\\py_code\\stock\\data\\'
    files = file_name(dir)
    
        
    

