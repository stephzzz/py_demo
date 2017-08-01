# /usr/bin/env python3
'''
确保某一个类只有一个实例，而且自行实例化并向整个系统提哦哪个这个实例，
这个类成为单例类，单例模式是一种对象创建型模式
'''


#方法1 使用__new__
class Singleton(object):
    '''
    将类的实例和一个类变量 _instance 关联起来，如果 cls._instance 为 None 则创建实例
    否则直接返回 cls._instance
    '''
    _instance = None
    def __new__(cls, *args, **kw):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kw)  
        return cls._instance  
 
class MyClass(Singleton):  
    a = 1


********************************************


# 方法2 使用装饰器
from functools import wraps
 
def singleton(cls):
    instances = {}
    @wraps(cls)
    def getinstance(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return getinstance
 
@singleton
class MyClass(object):
    a = 1
    
********************************************

 
# 方法3 使用metaclass
'''
元类（metaclass）可以控制类的创建过程，它主要做三件事：
a.拦截类的创建
b.修改类的定义
c.返回修改后的类
'''
class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

# Python2
class MyClass(object):
    __metaclass__ = Singleton

# Python3
# class MyClass(metaclass=Singleton):
#    pass

