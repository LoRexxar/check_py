# coding=utf-8

import os
import os.path
import re
import requests
from check_A import check


dir = "../subject1_sample/file"
black_list = ['澳门赌场', '成人', '性', '激情', '娱乐', '黄色图片', '博彩']

def h_check(text, filename):

	# file = open(dir + '/' + filename, 'rb')
	try:
		# text = file.read()

		message = check(filename)

		mess = re.split(',', message)
		url = mess[-1]
		point = 0

		for black in black_list:

			# if black not in text and black.decode('utf-8', 'ignore').encode('gb2312') not in text:
			# 	return tuple([True, mess[0]])
			point = point + text.count(black) + text.count(black.decode('utf-8', 'ignore').encode('gb2312'))

		# f.write(message)

		if point > 400:
			# f.write(message)
			# print message
			# print "[INFO] the point is " + str(point)
			return tuple([False, mess[0]+",d"])
		else:
			return tuple([True, mess[0]])

	except Exception as e: 
		print "[ERROR] "+str(e)
		exit(0)

	# finally:
	# 	file.close()


# dir = "../../subject1_sample/file"

# f = open("d.txt", 'w+')

# for parent, dirnames, filenames in os.walk(dir):
# 	for filename in filenames:

# 		result = ccheck(filename)

# 		if not result[0]:
# 			# f.write(result[1])
# 			print result[1]

# f.close()
# ccheck('00078edb0b0a989b5b141bfe5e7d72d6')