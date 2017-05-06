# coding=utf-8

import os
import os.path


# def test(filename):
# file = open('file_list_20170430_new.txt', 'rb')
file = open('p.txt', 'rb')
file2 = open('d.txt', 'rb')
file2text = file2.read()


for p in file:
	if p[:-1] in file2text:
		continue
	print p[:-1]

file.close()
file2.close()

# while 1:
# 	r = file.readline()

# 	if r:
# 		if ",d," in r:
# 			print r
# 	else:
# 		break

# 	file.readline()

# file.close()