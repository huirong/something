#!/usr/bin/env python
#coding=utf-8

'''
脚本作用：以 subDomainsBrute-master 生成的 txt 为输入，根据里面的域名生成相应的 title 
'''

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

import pandas as pd
import requests
from bs4 import BeautifulSoup

def getTitleFromUrl(f):
    "根据 URL 获取 title"

    #定义保存结果的数据结构
    urlList = []
    titleList = []

    #读取每行数据
    for line in f:
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


if __name__ == "__main__":
    # 打开文件
    filename = "com_full.txt";
    with open(filename, "rU") as f:
        print "read URL from" + filename + "............."
        getTitleFromUrl(f)