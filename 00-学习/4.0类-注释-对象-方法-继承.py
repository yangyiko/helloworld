#默认属性 self  __dict__ self.__name __class__
#{'_Person__name': '初始化用户名', '_Person__count': 1, '_count': 1, 'age': 100, 'sex': '女'}
 #__dict__ : 类的属性
#  __bases__ : 类的所有父类构成元组
#  __doc__ :类的文档字符串
#  __name__: 类名
#  __module__: 类定义所在的模块
#  __dict__ : 实例的属性
#  __class__: 实例对应的类
 
class Person:
    """
    1   类属性相当于是 java静态属性，可以在任何时候命名或修改 修改用 update
    2   对象属性相当于是java的属性，不能提前命名他赋值
    3  类和对象默认有    属性 self  __dict__ self.__name __class__
    4   元类  __class__.__class__
    关于这个类的描述, 类的作用, 类的构造函数等等; 类属性的描述
    """
    # 类属性
    addAttr1 = "类属性相当于是 java静态变量"
    @property
    def getName(self):
        return self.addAttr1
    
    def run(self, distance, step):
        """
        这个方法的作用效果
        :param distance: 步了多少数
        :param step:步数
        :return: 返回的结果的含义(时间), 返回数据的类型int
        """
        print(self.__name,"步长为" + str(distance / step))
        return distance / step
    
    def __init__(self):
        self.__name = "这是实例方法"
        self.__count=1
        self._count=1
        print("这是初始化的实例方法",self)
    
    @classmethod
    def lff(cls,tx):
        print("这是类方法",tx)
    
    @staticmethod
    def jtff():
        print("这是静态方法")
        
# help(Person)
p2 = Person()
print("读取属性property=getAddAttr1",p2.getName)
Person.addAttr2 = "类添加的属性2"
p1 = Person()
p1.run(1000, 3)
p1.addAttr2 = "对象添加的属性"
p1.age=100
p1.age=1001
p1.sex="女"
print(Person.__dict__)
print(p1.__dict__,p1.addAttr2,p1.addAttr1,p1.addAttr2)
p1.lff("")
p1.jtff()

print("---------------------------------继承--------------------------------")
class A(Person):
    pass
a = A()
a.lff("A继承了 Person的类方法，普通方法是不能被继承的")
a.run(11,11) 
l=[1,4,3,2]

