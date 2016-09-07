import jpype 

def test():
	jvmPath = jpype.getDefaultJVMPath() 
	ext_classpath = "commons-codec-1.10.jar:"
	jvmArg = "-Djava.class.path="+ext_classpath 
	if not jpype.isJVMStarted(): 
	    jpype.startJVM(jvmPath,jvmArg) 
	print jpype.isJVMStarted()
	javaClass = jpype.JClass('myutils.Tools')

	TA = jpype.JPackage('test2').TestApi  
	jd = TA()  
	jd.printData('1234')  

	print 'qqqqq'
	message = "144315122284714065"
	key = "49475fd41c9120f652c3284993bb8596ab34aceb"
	hmacSha1 = javaClass.getHmacSHA1(message, key)
	print hmacSha1
	jpype.shutdownJVM()