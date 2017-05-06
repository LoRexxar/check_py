# coding=utf-8

import os
import os.path
import re
import requests
from check_A import check


# dir = "../subject1_sample/file"
black_list = ['Apple ID', 'Apple Inc']


def apple_check(text, filename):
	# file = open(dir + '/' + filename, 'rb')
	try:
		# text = file.read()

		message = check(filename)

		mess = re.split(',', message)
		url = mess[-1]


		for black in black_list:
			if black not in text and black.decode('utf-8', 'ignore').encode('gb2312') not in text:
				return tuple([True, mess[0]])
		
		try:
			r = requests.get(url, timeout=3)
			if "apple.com" in r.url:
				# print "[INFO]not p page:" + message
				return tuple([True, mess[0]])
			else:
				# print message
				return tuple([False, mess[0]+",p"])
		except requests.exceptions.ConnectTimeout:
			# print message
			# print "[ERROR] timeout error..."
			return tuple([False, mess[0]+",p"])

		except requests.exceptions.ConnectionError:
			# print "[ERROR]  error..."
			# print message
			return tuple([False, mess[0]+",p"])

		except requests.exceptions.Timeout:
			return tuple([False, mess[0]+",p"])

		except Exception as e: 
			print "[ERROR] "+str(e)
			exit(0)
		

	except Exception as e: 
		print "[ERROR] "+str(e)
		exit(0)

	# finally:
	# 	file.close()


# dir = "../../subject1_sample/file"

# for parent, dirnames, filenames in os.walk(dir):
# 	for filename in filenames:

# 		result = apple_check(filename)

# 		if not result[0]:
# 			print result[1]
