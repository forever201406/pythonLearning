# -*- coding: utf-8 -*-
#!/usr/bin/python
# Filename: backup_ver1.py

import hashlib
import hmac
import time
# 14428073652182
# MzI3NGQyYWRhMDYyZTk5MzI0YzgwMDM2MmRjNDkzMjBmNGZjYWE3NA==
# signature:MzI3NGQyYWRhMDYyZTk5MzI0YzgwMDM2MmRjNDkzMjBmNGZjYWE3NA%3D%3D

secretkey = '49475fd41c9120f652c3284993bb8596ab34aceb'
signature = '14428073652182'
signature = hmac.new(secretkey,signature,hashlib.sha1).digest().encode('base64').rstrip()
print signature

timestamp = str(long(time.time()*1000))

print timestamp
print time.time()
print '+' in 'lL1W6t1xN0pBi6aa52xFucK7ZI='

test()

def test():
	print 'aaa'