#!/usr/bin/env python  
#coding : utf-8  
  
import jpype 
import multiprocessing
from tools import *
# jvmpath = jpype.getDefaultJVMPath()  
# jpype.startJVM(jvmpath, "-ea", "-Djava.class.path=.")  
# javaClass = jpype.JClass('test.TestApi') 
# value = "oldvalue" 
# javaInstance = javaClass(value)
# print javaInstance.getData(value) 
# javaInstance.printData("newvalue") 
# jpype.shutdownJVM();
# def test():
# 	jvmPath = jpype.getDefaultJVMPath() 
# 	ext_classpath = "commons-codec-1.10.jar:"
# 	jvmArg = "-Djava.class.path="+ext_classpath 
# 	if not jpype.isJVMStarted(): 
# 	    jpype.startJVM(jvmPath,jvmArg) 
# 	print jpype.isJVMStarted()
# 	javaClass = jpype.JClass('myutils.Tools')

# 	TA = jpype.JPackage('test2').TestApi  
# 	jd = TA()  
# 	jd.printData('1234')  

# 	print 'qqqqq'
# 	message = "144315122284714065"
# 	key = "49475fd41c9120f652c3284993bb8596ab34aceb"
# 	hmacSha1 = javaClass.getHmacSHA1(message, key)
# 	print hmacSha1
print jpype.isJVMStarted()
p1 = multiprocessing.Process(target=test,args=())
p1.daemon = True
p1.start()
p1.join()
print "p1.is_alive:", p1.is_alive()
# jpype.shutdownJVM()
print jpype.isJVMStarted()
p2 = multiprocessing.Process(target=test,args=())
p2.daemon = True
p2.start()
p2.join()
print jpype.isJVMStarted()
print "p2.is_alive:", p2.is_alive()

# jvmPath = jpype.getDefaultJVMPath() 
# ext_classpath = "commons-codec-1.10.jar:"
# jvmArg = "-Djava.class.path="+ext_classpath 
# if not jpype.isJVMStarted(): 
#     jpype.startJVM(jvmPath,jvmArg) 
# javaClass = jpype.JClass('myutils.Tools') 
# message = "144315122284714065"
# key = "49475fd41c9120f652c3284993bb8596ab34aceb"
# hmacSha1 = javaClass.getHmacSHA1(message, key)
# print hmacSha1
# jpype.shutdownJVM();