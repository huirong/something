#!/usr/bin/env python
#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

import pandas as pd
import requests
from bs4 import BeautifulSoup

try:
    file = open("163.com_full.txt", "rU")
except Exception as e:
    print('file open error', e)
    exit()

urlList = []
titleList = []

for line in file:
    url = "http://" + line.rstrip("\n").split()[0] + "/"
    print url

    try:
    	req = requests.get(url, timeout=0.5)
        #req.encoding = 'utf-8'
    	#print req.encoding
    	bs = BeautifulSoup(req.text, "html.parser")
    	if(bs.title):
    		title = bs.title.text
    	try:
    		title.encode('latin1').encode('utf-8','ignore')
    	except:
    		print ""

    	# 写入文件
    	'''
    	file_name = "test.txt"
    	with open(file_name, 'a+') as file:
    		file.write(url + ": " +title+'\n')
    	'''

    	# 使用 pandas 数据结构 DataFrame
    	urlList.append(url)
    	titleList.append(title)
    	
    except requests.exceptions.ConnectionError as e:
        print "cannot access"
    except requests.exceptions.ReadTimeout as e:
    	print "time out"

d = {}
d["url"] = urlList
d["title"] = titleList
df = pd.DataFrame(d)
df.to_excel("output111.xlsx",index=False)


file.close()
