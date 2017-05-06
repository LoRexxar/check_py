# coding=utf-8

import os
import os.path
import re
import requests
from check_A import check


# dir = "../subject1_sample/file"

black_word = '<div style="position: absolute; top: -999'
black_list = ['娱乐', '赌', '澳门', '皇冠', '援交']


def f_check(text, filename):

	# file = open(dir + '/' + filename, 'rb')
	try:
		# text = file.read()

		message = check(filename)

		mess = re.split(',', message)
		url = mess[-1]
		point = 0

		if black_word not in text and black_word.decode('utf-8', 'ignore').encode('gb2312') not in text:
			return tuple([True, mess[0]])	

		else:
			for black in black_list:
				point = point + text.count(black) + text.count(black.decode('utf-8', 'ignore').encode('gb2312'))
					

		if point > 10:
			return tuple([False, mess[0]+",d"])

		else:
			return tuple([True, mess[0]])


	except Exception as e: 
		print "[ERROR] "+str(e)
		exit(0)

	# finally:
	# 	file.close()
