# -*- coding: utf-8 -*-
#!/usr/bin/python
# Filename: testDecorator.py
import functools
# # 定义装饰函数，被装饰函数作为参数
# def decorator_one(f1):
#     print('start')
#     print('call ' + f1.__name__)
#     print('end')
#     # 被装饰函数不带参数，返回被装饰函数,最外层函数必须接受一个返回函数
#     return f1


# @decorator_one
# # 采取和上面定义不同的名字，否则会出错
# def f1():
#     pass


# f1()

# P2——装饰函数不带参数，被装饰函数带参数

# 定义装饰函数，被装饰函数作为参数
# def decorator_two(f2):
#     # 定义包装函数，用于传递给被装饰函数当做参数,使用可变参数和关键字参数可以提升灵活性
#     def wrapper_two(*args, **kw):
#         print('start')
#         print('call' + f2.__name__)
#         return f2(*args, **kw)
#         print('end')

#     # 这里的return返回的是decorator_two这个函数的返回值
#     return wrapper_two


# @decorator_two
# def f():
#     print()


# # '''流程是:f2=decorator_two(f2),然后运行wrapper_two函数，在f2执行前后进行
# # 处理,最后还要把函数最为一个返回值，这个是装饰函数要求的'''

# f()



def log(func):
	def wrapper(*args, **kw):
		print('call %s():' % func.__name__)
		return func(*args, **kw)
	return wrapper

@log
def now():
	print '2015-10-22'

# =>>now =  log(now)
now()


# def log(text):
# 	def decorator(func):
# 		@functools.wraps(func)
# 		def wrapper(*args, **kw):
# 			print('%s %s' % (text,func.__name__))
# 			return func(*args, **kw)
# 		return wrapper
# 	return decorator

# @log('execute')
# def now():
# 	print '2015-10-22'

# #=>>now =  log('execute')(now)
# now()
# print now.__name__