# coding=utf-8

import os
import os.path
import re
import requests
import chardet
from check_A import check


dir = "../subject1_sample/file"
black_list = ['皇冠', '澳门赌场', '娱乐场', '真钱', '备用网址']

def h_check2(text, filename):

	# file = open(dir + '/' + filename, 'rb')
	# try:
		# text = file.read()

	message = check(filename)

	mess = re.split(',', message)
	url = mess[-1]
	point = 0
	point2 = 0

	for black in black_list:

		# if black not in text and black.decode('utf-8', 'ignore').encode('gb2312') not in text:
		# 	return tuple([True, mess[0]])
		point = point + text.count(black) + text.count(black.decode('utf-8', 'ignore').encode('gb2312'))

	# f.write(message)

	if point > 10:
		# f.write(message)

		s = requests.Session()

		try:
			header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36'}

			r = s.get(url[:-1], headers=header, timeout=10)

			# print r.content
			for black in black_list:
				point2 = point2 + r.content.count(black)+ r.content.count(black.decode('utf-8', 'ignore').encode('gb2312'))

			if 1 > (point2+1)/point:

				if '<meta http-equiv="refresh" content="0;' in r.content:
					print message
					print "[INFO] the point is " + str(point)
					print "[INFO] the point2 is " + str(point2)
					return tuple([False, mess[0]+",d"])
			
			return tuple([True, mess[0]])
		
		except requests.exceptions.ConnectTimeout:
			# print message
			# print "[ERROR] timeout error..."
			return tuple([True, mess[0]])

		except requests.exceptions.ConnectionError:
			# print "[ERROR]  error..."
			# print message
			return tuple([True, mess[0]])

		except requests.exceptions.Timeout:
			return tuple([True, mess[0]])

		except requests.exceptions.ContentDecodingError:
			return tuple([True, mess[0]])

		# except Exception as e: 
		# 	print "[ERROR] "+str(e)
		# 	exit(0)

	else:
		return tuple([True, mess[0]])

	# except Exception as e: 
	# 	print "[ERROR] "+str(e)
	# 	exit(0)

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
# ccheck('12659b53d4554fbab7e4f1a3cc881815')