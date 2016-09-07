#!/usr/bin/env python  
#-*- coding: UTF-8 -* 
import random
import time
import hashlib
import hmac
import jpype 
  
# jvmPath = jpype.getDefaultJVMPath() 
# ext_classpath = "dist/commons-codec-1.10.jar:dist/httpclient-4.5.1.jar:dist/commons-logging.jar:dist/httpcore-4.4.3.jar:dist/log4j-1.2.17.jar:"
# jvmArg = "-Djava.class.path="+ext_classpath 
# if not jpype.isJVMStarted(): 
#     jpype.startJVM(jvmPath,jvmArg) 
# javaClass = jpype.JClass('sendmessage2user.Sendmessage') 
# # javaClass.send()
# print javaClass
# jpype.shutdownJVM();

# 生成时间戳
def getTimestamp():
	return str(long(time.time()*1000))

# 生成随机数
def getRandom(num):
	nonce = ''
	for i in range(1,num):
		nonce += str(random.randint(0,9))
	return nonce

# 用key对message进行hmac-sha1加密
def getHmacSHA1(key, message):
	result = hmac.new(key,message,hashlib.sha1).digest().encode('base64').rstrip()
	return result

# 发送消息给用户
def sendMessage(openId, message):
    testPostUrl = 'http://test-public-txt.pingan.com.cn:10080/HMP/rest/sendMessage'
    proPostUrl = 'http://public-txt.pingan.com.cn/HMP/rest/sendMessage'
    appid = '10001862'
    secretkeyTest = '123456'
    secretkeyPrd = '49475fd41c9120f652c3284993bb8596ab34aceb'
    postUrl = testPostUrl

    timestamp = getTimestamp()
    nonce = getRandom(6)
    # 时间戳和随机数的连接串（timestamp+nonce）与共享密钥做一次HMAC-SHA1加密得到签名串
    signature = timestamp + nonce
    signature = getHmacSHA1(secretkeyTest, signature)
    while '+' in signature:
        timestamp = getTimestamp()
        nonce = getRandom(6)
        signature = timestamp + nonce
        signature = getHmacSHA1(secretkeyTest, signature)

    jvmPath = jpype.getDefaultJVMPath()
    ext_classpath = "dist/httpclient-4.5.1.jar:dist/commons-logging.jar:dist/httpcore-4.4.3.jar:dist/log4j-1.2.17.jar:"
    jvmArg = "-Djava.class.path="+ext_classpath 
    if not jpype.isJVMStarted(): 
        jpype.startJVM(jvmPath,jvmArg) 
    javaClass = jpype.JClass('sendmessage2user.Sendmessage') 
    print javaClass
    javaClass.send(postUrl, appid, timestamp, nonce, signature, openId, message)
    print 'success'
    jpype.shutdownJVM();

openId = '2DD6788DE0570F33730FA685AE66EF12ADE34AD8DB3367D0'

message = '你好!hello++++'.decode('utf-8')

sendMessage(openId, message)