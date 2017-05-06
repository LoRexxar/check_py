# coding=utf-8

import os
import os.path
import re
import requests
import HTMLParser 
import chardet
from check_A import check
from check_A import check_whois

# dir = "../subject1_sample/file"
black_list = ['手机', '银行版权所有']

def bank_check(text, filename):

	# file = open(dir + '/' + filename, 'rb')
	# try:
		# text = file.read()

	if '&#34892' in text or '&#38134' in text:
		try:
			# print chardet.detect(text)
			t = HTMLParser.HTMLParser();
			text = t.unescape(text)

			message = check(filename)

			mess = re.split(',', message)
			url = mess[-1]		
			# print message
			
			for black in black_list:
				if black not in text:
					return tuple([True, mess[0]])

			
			if check_whois(["银行", "Bank", "bank", "BANK"], url):
				return tuple([True, mess[0]])
			else:
				# print message
				return tuple([False, mess[0]+",p"])

		except UnicodeDecodeError:
			pass

	
	else:		
		message = check(filename)

		mess = re.split(',', message)
		url = mess[-1]		

		for black in black_list:
			if black not in text and black.decode('utf-8', 'ignore').encode('gb2312') not in text:
				return tuple([True, mess[0]])

		
		if check_whois(["银行", "Bank", "bank", "BANK"], url):
			return tuple([True, mess[0]])
		else:
			# print message
			return tuple([False, mess[0]+",p"])