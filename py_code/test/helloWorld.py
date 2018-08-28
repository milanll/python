
# coding=utf-8
from testString import *
from selenium import webdriver
import string
import os
from selenium.webdriver.common.keys import Keys
import time
import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)


district_navs = ['nav2','nav1','nav3','nav4','nav5','nav6','nav7','nav8','nav9','nav10']
district_names = ['福田区','罗湖区','南山区','盐田区','宝安区','龙岗区','光明新区','坪山新区','龙华新区','大鹏新区']


flag = 1
while (flag > 0):
    driver = webdriver.Chrome()
    driver.get("http://www.szmb.gov.cn/article/QiXiangJianCe/")
    # 选择降雨量
    driver.find_element_by_xpath("//span[@id='fenqu_H24R']").click()

    filename = time.strftime("%Y%m%d%H%M", time.localtime(time.time())) + '.txt'
    #创建文件
    output_file = open(filename, 'w')
    # 选择行政区
    for i in range(len(district_navs)):
        driver.find_element_by_xpath("//div[@id='" + district_navs[i] + "']").click()
        # print driver.page_source
        timeElem = driver.find_element_by_id("time_shikuang")
        #输出时间和站点名
        output_file.write(timeElem.text + ',')
        output_file.write(district_names[i] + ',')
        elems = driver.find_elements_by_xpath("//span[@onmouseover='javscript:changeTextOver(this)']")
        #输出每个站点的数据，格式为：站点名，一小时降雨量，当日累积降雨量
        for elem in elems:
            output_file.write(AMonitorRecord(elem.get_attribute("title")) + ',')
        output_file.write('\n')
    output_file.close()
    driver.close()
    time.sleep(3600)