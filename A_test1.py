# coding=utf-8

import os
import os.path
import re
import requests
import Queue
import threading

# dir = "../subject1_sample/file"
dir = "../subject1_B/file2"

f = open("result.txt", 'w+')

words = Queue.Queue()


check_list = ['apple_check', 'apple_check2', 'qqanquan_check', 'qq_check', 'qq_check2', 'aliplay_check', 'bank_check', 'bank_check2']
check_list2 = ['js_check', 'f_check', 'f_check2', 'h_check', 'h_check2']

checkdic = {}

for check_poc in check_list:
	checkfile = "check." + check_poc
	checkdic[check_poc]=__import__(checkfile)


for check_poc in check_list2:
	checkfile = "check2." + check_poc
	checkdic[check_poc]=__import__(checkfile)


file_re = {}

for parent, dirnames, filenames in os.walk(dir):
	for filename in filenames:

		file_re[filename] = [False]
		
		words.put(filename)

print "words put success"


def check(words):
	
	while not words.empty():

		filename = words.get()

		file = open(dir + '/' + filename, 'rb')

		text = file.read()

		# print filename

		for check_poc in checkdic:
			p = getattr(getattr(checkdic[check_poc], check_poc), check_poc)

			# print check_poc
			result = p(text, filename)
			if not result[0]:
				file_re[filename][0] = True
				file_re[filename].append(result[1])
				# f.write(result[1] + "\n")
				print result[1]
				break


threads = []

for i in xrange(20):
	try:
		t = threading.Thread(target=check, args=(words,))
		t.start()
		threads.append(t)
	except:
		logger.error('Thread error...')


for t in threads:
	t.join()


print "run success"

for key in file_re:
	f.write(file_re[key][1]+'\n')

f.close()