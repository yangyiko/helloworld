# _*_ encoding:utf-8 _*_

# 计算器, 实现一些基本的操作, 加减乘除运算, 以及打印结果操作
#第8例是私有的
# ------------------------------------代码1--------------------------------------
class Caculater:
        #闭包 注意顺序不能错
    def checkNum(func):
        def inner(self,int_value):
            if not isinstance(int_value,int):
                raise TypeError("传入值不是",int)
            return func(self,int_value)
        return func
        
    """
    计算器编写方法
    """
    def __init__(self,init_value):
        if(init_value == None):
            self.__result = 0
        else:
            self.__result = init_value
            
    @checkNum       
    def jia(self,int_value):
        self.__result += int_value
        return self.__result
    
    @checkNum
    def jian(self,int_value):
        """
        解释器作前置验证
        """
        self.__result += int_value
#     return self.__result
    
    def showResult(self):
        print("计算结果:%d" % self.__result)
    
    
#     def raiseError(self,int_value,type_class):
#         """
#         :int_value 传入值
#         :type_class 验证类型
#         """
#         if not isinstance(int_value,type_class):
#             raise TypeError("传入值不是",type_class)
    

jsq1 = Caculater(1)
print("类1=",jsq1.jia(1))
jsq2 = Caculater(20)
print("类2=",jsq2.jia(20))
print("类1=",jsq1.jia(2))
jsq2.showResult()
#
# def first_value(v):
#     global result
#     result = v
#
# def jia(n):
#     global result
#     result += n
#
# def jian(n):
#     global result
#     result -= n
#
# def cheng(n):
#     global result
#     result *= n
#
#
# first_value(2)
# jia(6)
# result = 123
# jian(4)
# cheng(5)
# print(result)

# ------------------------------------代码3--------------------------------------


# class Caculator:
#     __result = 0
#
#     @classmethod
#     def first_value(cls, v):
#         cls.__result = v
#
#     @classmethod
#     def jia(cls, n):
#         cls.__result += n
#
#     @classmethod
#     def jian(cls, n):
#         cls.__result -= n
#
#     @classmethod
#     def cheng(cls, n):
#         cls.__result *= n
#
#     @classmethod
#     def show(cls):
#         print("计算的结果是:%d" % cls.__result)
#
# Caculator.first_value(2)
# Caculator.jia(6)
# Caculator.jian(4)
# Caculator.cheng(5)
# Caculator.show()

# ------------------------------------代码4--------------------------------------
#
# class Caculator:
#
#     def __init__(self, num):
#         self.__result = num
#
#     def jia(self, n):
#         self.__result += n
#
#     def jian(self, n):
#         self.__result -= n
#
#     def cheng(self, n):
#         self.__result *= n
#
#     def show(self):
#         print("计算的结果是:%d" % self.__result)
#
#
# c1 = Caculator(2)
# c1.jia(6)
# c1.jian(4)
# c1.cheng(5)
# c1.show()

# ------------------------------------代码5--------------------------------------


# class Caculator:
#     def check_num(self, num):
#         if not isinstance(num, int):
#             raise TypeError("当前这个数据的类型有问题, 应该是一个整型数据")
#
#     def __init__(self, num):
#         self.check_num(num)
#         self.__result = num
#
#     def jia(self, n):
#         self.check_num(n)
#         self.__result += n
#
#     def jian(self, n):
#         self.check_num(n)
#         self.__result -= n
#
#     def cheng(self, n):
#         self.check_num(n)
#         self.__result *= n
#
#     def show(self):
#         print("计算的结果是:%d" % self.__result)
#
#
# c1 = Caculator(2)
# c1.jia(6)
# c1.jian("a")
# c1.cheng(5)
# c1.show()

# ------------------------------------代码6--------------------------------------

class Caculator:
    def check_num_zsq(func):
        def inner(self, n):
            if not isinstance(n, int):
                raise TypeError("当前这个数据的类型有问题, 应该是一个整型数据")
            return func(self, n)
        return inner

    @check_num_zsq
    def __init__(self, num):
        self.__result = num

    @check_num_zsq
    def jia(self, n):
        self.__result += n

    @check_num_zsq
    def jian(self, n):
        self.__result -= n

    @check_num_zsq
    def cheng(self, n):
        self.__result *= n

    def show(self):
        print("计算的结果是:%d" % self.__result)


c1 = Caculator(2)
c1.jia(6)
c1.jian(4)
c1.cheng(5)
c1.show()

# ------------------------------------代码7--------------------------------------

# 
# class Caculator:
#     def __check_num_zsq(func):
#         def inner(self, n):
#             if not isinstance(n, int):
#                 raise TypeError("当前这个数据的类型有问题, 应该是一个整型数据")
#             return func(self, n)
#         return inner
# 
#     @__check_num_zsq
#     def __init__(self, num):
#         self.__result = num
# 
#     @__check_num_zsq
#     def jia(self, n):
#         self.__result += n
# 
#     @__check_num_zsq
#     def jian(self, n):
#         self.__result -= n
# 
#     @__check_num_zsq
#     def cheng(self, n):
#         self.__result *= n
# 
#     def show(self):
#         print("计算的结果是:%d" % self.__result)
# 
# 
# c1 = Caculator(2)
# c1.jia(6)
# c1.jian(4)
# c1.cheng(5)
# c1.show()


# ------------------------------------语音识别 代码8--------------------------------------
# import win32com.client

# # 1. 创建一个播报器对象
# speaker = win32com.client.Dispatch("SAPI.SpVoice")
#
# # 2. 通过这个播报器对象, 直接, 播放相对应的语音字符串就可以
# speaker.Speak("我的名字是sz")

# class Caculator:
#     def __check_num_zsq(func):
#         def inner(self, n):
#             if not isinstance(n, int):
#                 raise TypeError("当前这个数据的类型有问题, 应该是一个整型数据")
#             return func(self, n)
#
#         return inner
#
#     # def __say(self, word):
#     #     # 1. 创建一个播报器对象
#     #     speaker = win32com.client.Dispatch("SAPI.SpVoice")
#     #
#     #     # 2. 通过这个播报器对象, 直接, 播放相对应的语音字符串就可以
#     #     speaker.Speak(word)
#
#     def create_say_zsq(word=""):
#         def __say_zsq(func):
#             def inner(self, n):
#                 # 1. 创建一个播报器对象
#                 speaker = win32com.client.Dispatch("SAPI.SpVoice")
#                 # 2. 通过这个播报器对象, 直接, 播放相对应的语音字符串就可以
#                 speaker.Speak(word + str(n))
#                 return func(self, n)
#
#             return inner
#
#         return __say_zsq
#
#     @__check_num_zsq
#     @create_say_zsq()
#     def __init__(self, num):
#         self.__result = num
#
#     @__check_num_zsq
#     @create_say_zsq("加")
#     def jia(self, n):
#         self.__result += n
#
#     @__check_num_zsq
#     @create_say_zsq("减去")
#     def jian(self, n):
#         self.__result -= n
#
#     @__check_num_zsq
#     @create_say_zsq("乘以")
#     def cheng(self, n):
#         self.__result *= n
#
#     def show(self):
#         # self.__say("计算的结果是:%d" % self.__result)
#         print("计算的结果是:%d" % self.__result)
#
# c1 = Caculator(10)
# c1.jia(6)
# c1.jian(4)
# c1.cheng(5)
# c1.show()

# ------------------------------------代码9--------------------------------------
# import win32com.client
#
#
# class Caculator:
#     def __check_num_zsq(func):
#         def inner(self, n):
#             if not isinstance(n, int):
#                 raise TypeError("当前这个数据的类型有问题, 应该是一个整型数据")
#             return func(self, n)
#
#         return inner
#
#     def __say(self, word):
#         # 1. 创建一个播报器对象
#         speaker = win32com.client.Dispatch("SAPI.SpVoice")
#
#         # 2. 通过这个播报器对象, 直接, 播放相对应的语音字符串就可以
#         speaker.Speak(word)
#
#     def __create_say_zsq(word=""):
#         def __say_zsq(func):
#             def inner(self, n):
#                 self.__say(word + str(n))
#                 return func(self, n)
#
#             return inner
#         return __say_zsq
#
#     @__check_num_zsq
#     @__create_say_zsq()
#     def __init__(self, num):
#         self.__result = num
#
#     @__check_num_zsq
#     @__create_say_zsq("加")
#     def jia(self, n):
#         self.__result += n
#
#     @__check_num_zsq
#     @__create_say_zsq("减去")
#     def jian(self, n):
#         self.__result -= n
#
#     @__check_num_zsq
#     @__create_say_zsq("乘以")
#     def cheng(self, n):
#         self.__result *= n
#
#     def show(self):
#         self.__say("计算的结果是:%d" % self.__result)
#         print("计算的结果是:%d" % self.__result)
#
# c1 = Caculator(10)
# c1.jia(6)
# c1.jian(4)
# c1.cheng(5)
# c1.show()


# ------------------------------------代码10--------------------------------------
# import win32com.client
#
#
# class Caculator:
#     def __check_num_zsq(func):
#         def inner(self, n):
#             if not isinstance(n, int):
#                 raise TypeError("当前这个数据的类型有问题, 应该是一个整型数据")
#             return func(self, n)
#
#         return inner
#
#     def __say(self, word):
#         # 1. 创建一个播报器对象
#         speaker = win32com.client.Dispatch("SAPI.SpVoice")
#
#         # 2. 通过这个播报器对象, 直接, 播放相对应的语音字符串就可以
#         speaker.Speak(word)
#
#     def __create_say_zsq(word=""):
#         def __say_zsq(func):
#             def inner(self, n):
#                 self.__say(word + str(n))
#                 return func(self, n)
#
#             return inner
#         return __say_zsq
#
#     @__check_num_zsq
#     @__create_say_zsq()
#     def __init__(self, num):
#         self.__result = num
#
#     @__check_num_zsq
#     @__create_say_zsq("加")
#     def jia(self, n):
#         self.__result += n
#
#     @__check_num_zsq
#     @__create_say_zsq("减去")
#     def jian(self, n):
#         self.__result -= n
#
#     @__check_num_zsq
#     @__create_say_zsq("乘以")
#     def cheng(self, n):
#         self.__result *= n
#
#     def show(self):
#         self.__say("计算的结果是:%d" % self.__result)
#         print("计算的结果是:%d" % self.__result)
#
#     @property
#     def result(self):
#         return self.__result
#
# c1 = Caculator(10)
# c1.jia(6)
# c1.jian(4)
# c1.cheng(5)
# c1.show()
#
# print(c1.result)
# c1.result = 10

# ------------------------------------代码11--------------------------------------
import win32com.client


class Caculator:
    def __check_num_zsq(func):
        def inner(self, n):
            if not isinstance(n, int):
                raise TypeError("当前这个数据的类型有问题, 应该是一个整型数据")
            return func(self, n)

        return inner

    def __say(self, word):
        pass
        # 1. 创建一个播报器对象
        speaker = win32com.client.Dispatch("SAPI.SpVoice")

        # 2. 通过这个播报器对象, 直接, 播放相对应的语音字符串就可以
        speaker.Speak(word)

    def __create_say_zsq(word=""):
        def __say_zsq(func):
            def inner(self, n):
                self.__say(word + str(n))
                return func(self, n)

            return inner
        return __say_zsq

    @__check_num_zsq
    @__create_say_zsq()
    def __init__(self, num):
        self.__result = num

    @__check_num_zsq
    @__create_say_zsq("加")
    def jia(self, n):
        self.__result += n
        return self

    @__check_num_zsq
    @__create_say_zsq("减去")
    def jian(self, n):
        self.__result -= n
        return self

    @__check_num_zsq
    @__create_say_zsq("乘以")
    def cheng(self, n):
        self.__result *= n
        return self

    def show(self):
        self.__say("计算的结果是:%d" % self.__result)
        print("计算的结果是:%d" % self.__result)
        return self

    def clear(self):
        self.__result = 0
        return self

    @property
    def result(self):
        return self.__result

c1 = Caculator(10)
c1.jia(6).jian(4).cheng(5).show().clear().jia(555).jian(500).show()

print(c1.result)


