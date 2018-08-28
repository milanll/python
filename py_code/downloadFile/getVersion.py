import re,os

def getVersion(string):
	version = re.findall('band\d+_(\w+)', string, re.I)
	print(version)
	return version

if __name__ == '__main__':
	getVersion('PCT_bj_band3_zpj.rar')