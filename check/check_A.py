# coding=utf-8

import os
import os.path
import urllib
import requests
import time
import sys

defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)

def check(filename):
	file = open('../subject1_B/file2_list.txt', 'rb')

	
	for eachline in file:
		if filename in eachline:
			message = eachline

	file.close( )
	return message

def check_whois(keyword, url):

	proto, rest = urllib.splittype(url)
	res, rest = urllib.splithost(rest)

	if res.count('.') !=1:
		index = res.find('.')
		url = res[index+1:]
	else:
		url = res

	while 1:
		try:

			header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36'}

			s = requests.Session()
			r = s.get("http://api.hackertarget.com/whois/?q="+url, headers=header)

			# print r.text

			if "Connection reset by peer" in r.text:
				time.sleep(3)
				continue

			for key in keyword:

				if key in r.text:
					return True

		except Exception as e: 
			print "[ERROR] "+str(e)
			time.sleep(3)
			continue

		return False
