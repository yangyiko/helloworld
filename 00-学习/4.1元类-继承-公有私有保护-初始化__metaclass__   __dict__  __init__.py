#__type __bases__
#内置__metaclass__   __dict__  __init__
#metaclass 公有
#_metaclass 保护 
#__metaclass 私有
#动态创建类 元类
# -----------------------------类的创建方式---------------------------
def run(self):
    print("使用Type创建类---", self)

class_self = type("Dog",(),{"count": 0, "run": run})
print(class_self.__dict__)
print(class_self)
class_self.run(1)


# -----------------------------类的创建流程---继承---------------

class Test():
    pass
__metaclass__ = Test

class Animal:
    height = 10 #公有
    _age  = 5#保护
    __color = 'yellow'    #私有
    def __init__(self):
        print("我是__init__初始化方法")
        
        

class Person(Animal):
    __metaclass__ = Test
    pass

#
class Dog(Animal):
    __metaclass__ = 10
    pass
 
print(Person.__metaclass__)

# -----------------------------公有、保护、私有---------------
dog = Dog()
print("继承于Animal的公有属性=",dog.height)
print("继承于Animal的保护属性= ",dog._age)
#print("继承于Animal的私有属性= ",dog.__color)
print("继承于Animal的访问私有属性的办法= ",dog._Animal__color)













