'''
函数说明：
1.driver.find_element*():定位元素，详看另外一篇博文：Selenuim+Python之元素定位总结及实例说明
2.driver.get(url):浏览器加载url。
实例：driver.get("http//:www.baidu.com")
3.driver.forward()：浏览器向前（点击向前按钮）。
4.driver.back()：浏览器向后（点击向后按钮）。
5.driver.refresh()：浏览器刷新（点击刷新按钮）。
6.driver.close()：关闭当前窗口，或最后打开的窗口。
7.driver.quit():关闭所有关联窗口，并且安全关闭session。
8.driver.maximize_window():最大化浏览器窗口。
9.driver.set_window_size(宽，高)：设置浏览器窗口大小。
10.driver.get_window_size()：获取当前窗口的长和宽。
11.driver.get_window_position()：获取当前窗口坐标。
12.driver.get_screenshot_as_file(filename):截取当前窗口。
实例：driver.get_screenshot_as_file('D:/selenium/image/baidu.jpg')
13.driver.implicitly_wait(秒)：隐式等待，通过一定的时长等待页面上某一元素加载完成。
若提前定位到元素，则继续执行。若超过时间未加载出，则抛出NoSuchElementException异常。
实例：driver.implicitly_wait(10) #等待10秒
14.driver.switch_to_frame(id或name属性值)：切换到新表单(同一窗口)。若无id或属性值，可先通过xpath定位到iframe，再将值传给switch_to_frame()
15.driver.switch_to.parent_content():跳出当前一级表单。该方法默认对应于离它最近的switch_to.frame()方法。
16.driver.switch_to.default_content():跳回最外层的页面。
17.driver.switch_to_window(窗口句柄)：切换到新窗口。
18.driver.switch_to.window(窗口句柄):切换到新窗口。
19.driver.switch_to_alert():警告框处理。处理JavaScript所生成的alert,confirm,prompt.
20.driver.switch_to.alert():警告框处理。
21.driver.execute_script(js):调用js。
22.driver.get_cookies():获取当前会话所有cookie信息。
23.driver.get_cookie(cookie_name)：返回字典的key为“cookie_name”的cookie信息。
实例：driver.get_cookie("NET_SessionId")
24.driver.add_cookie(cookie_dict):添加cookie。“cookie_dict”指字典对象，必须有name和value值。
25.driver.delete_cookie(name,optionsString):删除cookie信息。
26.driver.delete_all_cookies():删除所有cookie信息。
'''

from selenium import webdriver
from lxml import etree
import requests,re,json
from selenium.webdriver.support.ui import Select

import chardet

from read_match_data import read_match_data

import soccer_comm
from odds import get_key_final

#竞彩比分
url_jc = "https://live.500.com"
#单场比分
url_dch = "http://live.500.com/zqdc.php"

#根据赔率列表，在网页中选择合适的场次
def match_select(odds_choice, url):
	driver = webdriver.Chrome()
	#隐性等待时间为30秒
	#driver.implicitly_wait(3) 
	
	#打开网页，并使窗口最大化
	driver.get(url)
	driver.maximize_window()
	
	#根据赔率列表，勾选选中的场次
	for key in odds_choice:
		driver.find_elements_by_xpath(f'//tr[@fid="{key}"]/td')[0].find_element_by_name('check_id[]').click()
	
	#点击“保留选中”
	driver.find_element_by_id('btn_match_show').click()
	
	#选择“平局赔率”
	Select(driver.find_element_by_id('sel_odds')).select_by_value("0")
	
	input('press enter key to exit.....')
	
if __name__ == "__main__":
	soccer_comm.print_help()
	url_choice = input('please choice url:')

	match_dict, odds_dict = read_match_data(url_choice)
	
	if url_choice == 'jc':
		url = url_jc
	elif url_choice == 'dch':
		url = url_dch
	else:
		print('url is wrong!')
		sys.exit()
	
	key_final = get_key_final(odds_dict, match_dict)
	
	match_select(key_final, url)
	
	
	
		
		


