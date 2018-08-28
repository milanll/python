# -* - coding: UTF-8 -* -  
'''
[section1]
name = tank
age = 28

[section2]
ip = 192.168.1.1
port = 8080
'''
import configparser

conf = configparser.ConfigParser()

def readConfig(configFile,Section,Option):
    conf.read(configFile)
    # 获取指定的section， 指定的option的值
    optionValue = conf.get(Section, Option)
    
    return int(optionValue)

def writeConfig(configFile,Section,Option,OptionValue):
    # 更新指定section, option的值
    conf.set(Section,Option,OptionValue)
    # 写回配置文件
    conf.write(open(configFile,"w"))
    
'''
import configparser

conf = ConfigParser.ConfigParser()
conf.read("version.conf")

# 获取指定的section， 指定的option的值
name = conf.get("section1", "name")
print(name)
age = conf.get("section1", "age")
print(age)

#获取所有的section
sections = conf.sections()
print(sections)

#写配置文件

# 更新指定section, option的值
conf.set("section2", "port", "8081")

# 写入指定section, 增加新option的值
conf.set("section2", "IEPort", "80")

# 添加新的 section
conf.add_section("new_section")
conf.set("new_section", "new_option", "http://www.cnblogs.com/tankxiao")

# 写回配置文件
conf.write(open("c:\\test.conf","w"))
'''


