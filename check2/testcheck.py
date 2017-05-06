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

def ccheck(filename):

	file = open(dir + '/' + filename, 'rb')
	try:
		text = file.read()

		message = check(filename)

		mess = re.split(',', message)
		url = mess[-1]
		point = 0
		

		for black in black_list:

			# if black not in text and black.decode('utf-8', 'ignore').encode('gb2312') not in text:
				# return tuple([True, mess[0]])
			point = point + text.count(black) + text.count(black.decode('utf-8', 'ignore').encode('gb2312'))


		# f.write(message)

		if point > 0:
		# print text

		# match = re.match( r'^\s*<script.*src\s*=\s*"(http:)?(https:)?\/\/.*<\/script>', text)
		# match = re.match('script', text)

		# if match:

		# 	if get_url(url) not in match.group():
			print message
		# 	print match.group()
			return tuple([False, mess[0]+",d"])
		
		
		# return tuple([True, mess[0]])

			# f.write(message)

			# s = requests.Session()

			# try:
			# 	header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36'}

			# 	r = s.get(url[:-1], headers=header, timeout=10)

			# 	for black in black_list:
			# 		point2 = point2 + r.content.count(black)+ r.content.count(black.decode('utf-8', 'ignore').encode('gb2312'))

			# 	if 1 > (point2+1)/point:

			# 		if '<meta http-equiv="refresh" content="0;' in r.content:
			# 			print message
			# 			print "[INFO] the point is " + str(point)
			# 			print "[INFO] the point2 is " + str(point2)
			# 			return tuple([False, mess[0]+",d"])
				
			# 	return tuple([True, mess[0]])
			
			# except requests.exceptions.ConnectTimeout:
			# 	# print message
			# 	# print "[ERROR] timeout error..."
			# 	return tuple([True, mess[0]])

			# except requests.exceptions.ConnectionError:
			# 	# print "[ERROR]  error..."
			# 	# print message
			# 	return tuple([True, mess[0]])

			# except requests.exceptions.Timeout:
			# 	return tuple([True, mess[0]])

			# except Exception as e: 
			# 	print "[ERROR] "+str(e)
			# 	exit(0)

		else:
			return tuple([True, mess[0]])

	# except Exception as e: 
	# 	print "[ERROR] "+str(e)
	# 	exit(0)

	finally:
		file.close()


dir = "../../subject1_sample/file"

# f = open("d.txt", 'w+')

for parent, dirnames, filenames in os.walk(dir):
	for filename in filenames:

		result = ccheck(filename)

		if not result[0]:
			# f.write(result[1])
			print result[1]

# f.close()
# ccheck('048fb4edced22562f0c1693535518cbf')