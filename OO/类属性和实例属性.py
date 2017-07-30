# /usr/bin/env python3
class People(object):
    country = 'Chian'      #------->这是公有的类属性
    __address = "Beijing"  #------->这是私有的类属性

    def __init__(self):
        self.name = "xiaoli"  #--->实例属性(对象属性)
        self.age = 20         #--->实例属性(对象属性)

p=People()

#类属性的使用
print(People.country)  #正确
print(p.country)       #正确,country是类属性，可以继承给对象
#print(People.__address)   错误，不能在类外通过类对象访问类的私有属性
#print(p.__address)        错误，不能在类外通过实例对象访问类的私有属性

#实例属性的使用
print(p.name)
print(p.age)

#print(People.name)    错误,父类无法获得子类的属性
#print(People.age)     错误,父类无法获得子类的属性
