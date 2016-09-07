# -*- coding: utf-8 -*-
#!/usr/bin/python
# Filename: img2base64.py

import base64
import sys 

pwd=r''
pwd+=sys.argv[1]

print pwd

f=open(pwd,'rb') #二进制方式打开图文件
ls_f=base64.b64encode(f.read()) #读取文件内容，转换为base64编码
f.close()
print ls_f