#!/usr/bin/env python
#_*_coding:utf-8 _*_

import  re
import urllib2  
import json 

def parse(ip):
  """
  get locate of each ip
  """
	apiurl = "http://ip.taobao.com/service/getIpInfo.php?ip=%s" % ip
	content = urllib2.urlopen(apiurl).read() 
	data = json.loads(content)['data']  
	code = json.loads(content)['code']

	if code == 0:
		locate = data["country"].encode('utf-8') + data["region"].encode('utf-8') + data["city"].encode('utf-8')
	else:
		locate = data.encode('utf-8')
	return locate

def getIpNum(filename):
  """
  Extract ip and number from filename
  """
	num = {}
	with open(filename,'r') as f:    
	    for line in f.readlines():
	        result2 = re.findall('[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}', line)
	        if not result2  == []:
	            result = result2[0]
	            if(result not in num.keys()):
	            	num[result] = 1
	            else:
	            	num[result] = num[result] + 1
	    
	    #Sort by num of each ip
      sorted_ips = sorted(num.items(), lambda x, y: cmp(x[1], y[1]), reverse=True)
	    return sorted_ips
	return []

def main():
	ips = getIpNum("mongod.log")
	for index in ips:
		print index[0] + "	" + str(index[1]) + "	" + parse(index[0])
if __name__=="__main__":
	main()
