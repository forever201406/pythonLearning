import jpype 
jvmPath = jpype.getDefaultJVMPath() 
jpype.startJVM(jvmPath) 
jpype.java.lang.System.out.println( "hello world!") 
print jpype.isJVMStarted() 
jpype.shutdownJVM() 