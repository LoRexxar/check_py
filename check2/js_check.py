# coding=utf-8

import os
import os.path
import re
import requests
import chardet
from check_A import check
from check_A import get_url

dir = "../subject1_sample/file"
black_list = ['<script src="http://www.005005e.com/9.js"></script>', '<script language="javascript" type="text/javascript" src="//js.users.51.la/17717427.js">']

def js_check(text, filename):

	# file = open(dir + '/' + filename, 'rb')
	try:
		# text = file.read()

		message = check(filename)

		mess = re.split(',', message)
		url = mess[-1]
		point = 0

		for black in black_list:
			point = point + text.count(black) + text.count(black.decode('utf-8', 'ignore').encode('gb2312'))


		if point > 0:
			return tuple([False, mess[0]+",d"])
		
		else:
			return tuple([True, mess[0]])

	except Exception as e: 
		print "[ERROR] "+str(e)
		exit(0)

	# finally:
	# 	file.close()

