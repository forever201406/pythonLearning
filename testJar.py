#!/usr/bin/env python  
#coding : utf-8  
  
from jpype import *  
  
# jvmpath = getDefaultJVMPath()  
# startJVM(jvmpath, "-ea", "-Djava.class.path=.")  
# TA = JPackage('test2').TestApi  
# jd = TA()  
# jd.printData('1234')  
# s = jd.getData('a')  
# print s  
# shutdownJVM(); 


jvmpath = getDefaultJVMPath()  
startJVM(jvmpath, "-ea", "-Djava.class.path=commons-codec-1.10.jar:")  
TA = JPackage('org').apache.commons.codec.binary.Base64  
jd = TA()  
javaClass = JClass('myutils.Tools')  
message = "144315122284714065"
key = "49475fd41c9120f652c3284993bb8596ab34aceb"
hmacSha1 = javaClass.getHmacSHA1(message, key)
print hmacSha1
shutdownJVM(); 
