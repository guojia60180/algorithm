#Author guo
#单例模式是一种设计模式，应用该模式的类只会生成一个实例
#保证程序在不同位置可以且仅可以取到同一个对象实例
#实例不存在，创建一个实例，已存在，返回这个实例

#使用函数装饰器实现单例

def singleton(cls):
    _instance={}

    def inner():
        if cls not in _instance:
            _instance[cls]=cls()
        return _instance[cls]
    return inner
#使用不可变的类地址作为键，实例作为值，每次创造实例时，查看查看该类是否存在实例
#存在话直接返回实例，否则新建一个实例存在字典中
@singleton
class Cls(object):
    def __init__(self):
        pass

cls1=Cls()
cls2=Cls()
print(id(cls1)==id(cls2))#指向同一个对象

#使用类装饰器实现单例

class Singleton(object):
    def __init__(self,cls):
        self._cls=cls
        self.instance={}
    def __call__(self):
        if self._cls not in self.instance:
            self.instance[self._cls]=self._cls()
        return self.instance[self._cls]

@Singleton
class Cls2(object):
    def __init__(self):
        pass

cls1=Cls2()
cls2=Cls2()
print(id(cls2)==id(cls1))


'''
new metaclss
 类和实例的方法是怎样顺序的创造的
 
 元类metaclass可以通过__metaclass__创造类
 类通过__new__创造了实例
 
 对创造类过程或对创造实例的过程加以控制，产生实例是相同的
'''

#使用new实现单例模式
class Single(object):
    _instance=None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance=object.__new__(cls, *args, **kwargs)
        return cls._instance
        #用_instance存放实例 返回_instance存放实例
    def __init__(self):
        pass

single1=Single()
single2=Single()
print(id(single1)==id(single2))


#使用metaclass实现
'''
def func(self):
    print("do sth")

Klass = type("Klass", (), {"func": func})

c = Klass()
c.func()
使用type来创造类的方法
'''

class Singleton(type):
    _instance={}
    def __call__(cls, *args, **kwargs):
        if cls not  in cls._instance:
            cls._instance[cls]=super(Singleton,cls).__call__( *args, **kwargs)
        return cls._instance[cls]

class Cls4(metaclass=Singleton):
    pass

cls1=Cls4()
cls2=Cls4()
print(id(cls2)==id(cls1))


#自己写的要记住的
class SingleTon(object):
    instance=None
    def __new__(cls, *args, **kwargs):
        if cls.instance==None:
            cls.instance=object.__new__(cls,*args,**kwargs)
        return cls.instance

a=SingleTon()
b=SingleTon()
print(id(a)==id(b))

def singeTon(cls):
    instance={}
    def inner():
        if cls not in instance:
            instance[cls]=cls()
        return instance[cls]
    return inner

@singeTon
class D():
    def __init__(self):
        pass

c=D()
e=D()
print(id(c)==id(e))

#还有这一种方法
#模块是天然的单例模式
#模块第一次导入时，会产生.pyc
#第二次导入时，直接加载.pyc，不会再次执行模块代码
#只需要把相关函数和定义放在一个模块中，导入就能实现单例