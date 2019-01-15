"""时间"""
#=====================================时间==========================================
# print(time.strftime("%y===%m-%d %H:%M:%S", time.localtime()))
#end = time.clock();
#time.sleep()
#===============================================================================
from unittest.util import sorted_list_difference
print ("===================================时间====================================")
import time
start = time.clock();
for i in range(1,100):
    print(time.strftime("%y===%m-%d %H:%M:%S", time.localtime()))
end = time.clock();
print("耗时"+str(end-start))



"""函数"""
#=====================================函数==========================================
#注释
#偏函数 重写
# 匿名函数
# 闭包 nonlocal num 
# 装饰 @checklogin  AOP
#===============================================================================
print ("===================================函数   注释====================================")

#元组参数用*  字典参数用**  数据也可以()
def mySum(*t):
    print(t, type(t))
    result = 0
    for v in t:
        result += v
    print("可变参数=",str(type(t)))
mySum(1,2,3)
#mySum((1,2,3))    def mySum(t):

  # 拆包
def test(a,b,c,d):
    # 拆包
    print("完成了对args的拆包=", a,b,c,d)
    
    # mySum((1, 2, 3, 4))
    # mySum(args[0], args[1], args[2], args[3])
args = (1,2,3,4)
test(*args)  #完成了拆包

  # 排序函数
result=sorted([1,4,2,9,6],reverse=True)
print("排序函数="+str(result))

#默认参数
def hit(somebody="豆豆"):
    print("排序参数 豆豆="+str(somebody))
   
hit()

#函数注释
def funhelp(somebody="函数注释"):
    """
    函数注释
#     计算两个数据的和, 以及差
#     :param a: 数值1, 数值类型, 不可选, 没有默认值
#     :param b: 数值2, 数值类型, 可选, 默认值: 1
#     :return: 返回的是计算的结果, 元组 : (和, 差)
    """
    print("函数注释="+str(somebody))
funhelp()
#函数注释
help(funhelp)

# 1. 偏函数 当要给一个函数设备一个默认值时
#
def test(a, b, c, d=1):
    print(a + b + c + d)

import functools

newFunc = functools.partial(test, c=5)
print(newFunc, "偏爱函数="+str(type(newFunc)))

# 匿名函数
result = (lambda x, y : x + y)(1, 2)
print("匿名函数="+str(result))

newFunc = lambda x, y : x + y
print("匿名函数="+str(newFunc(4, 5)))


# 闭包
def test():
    num = 10
    def test2():
        nonlocal num #加了这个参数num不会被覆盖
        num = 666
        # print(a)
        print(num)

    print(num)
    test2()
    print(num)

    return test2
print("闭包===========")
result = test()


# def mySum(**kwargs):
#     print(kwargs, type(kwargs))
#
#
# # mySum(1, 2, 3)
# mySum(name="sz", age=12)
# def mySum(a, b, c):
#     print(a + b + c)
#
#

# def mySum(a, b, c, d):
#     print(a + b + c + d)
#
#

#
# test(1, 2, 3, 4)

# def mySum(a, b):
#     print(a)
#     print(b)
#
#
# def test(**kwargs):
#     print(kwargs)
#
#     # 拆包操作
#     # 应该使用 ** 进行拆包操作
#     # print(**kwargs)
#     # a=1, b=2
#     mySum(**kwargs)
#     # mySum(a=1, b=2)
#
# test(a=1, b=2)



#
# result = sorted([1, 3, 2, 5, 4], reverse=True)
# print(result)



# def hit(somebody="豆豆"):
#     print("我想打", somebody)


# def hit(somebody):
#     print("我想打", somebody)
# hit()





# def change(num):
#     print(id(num))
#     # print(num)
#     num = 666
#     print(id(num))
#
#
# b = 10
# print(id(b))
# change(b)
# print(b)



# def change(num):
#     print(id(num))
#     num.append(666)
#     print(id(num))
#
#
# b = [1, 2, 3]
# print(id(b))
# change(b)
# print(b)


# ------------------------函数的返回值-------------------------------


# def mySum(a, b):
#     result = a + b
#
#     return result
#     return 666
#     print("xxx")
#     # print(result)
#     # print(a + b)
#
# res = mySum(6, 7)
# print(res)

# 针对于计算的结果, 不一定想要打印, 就比如, 我要乘以4, 或者  除以5, 外界的业务逻辑来的,
# print()


# def caculate(a, b=1):
#     """
#     计算两个数据的和, 以及差
#     :param a: 数值1, 数值类型, 不可选, 没有默认值
#     :param b: 数值2, 数值类型, 可选, 默认值: 1
#     :return: 返回的是计算的结果, 元组 : (和, 差)
#     """
#     he = a + b
#     cha = a - b
#     return (he, cha)
#
#
# # res = caculate(6, 7)
# # he, cha = caculate(6, 7)
# # print(he)
# # print(cha)
#
# # help(caculate)
#
#
#
# import functools
# newFunc = functools.partial(caculate, a=3)
# result = newFunc()
# print(result)





# ----------------------------函数的高级使用-----------------------------------

# 1. 偏函数
#
# def test(a, b, c, d=1):
#     print(a + b + c + d)
#
# # test(1, 2, 3)
#
# # def test2(a, b, c=5, d=1):
# #     test(a, b, c, d)
#
#
# # test2(1, 2)
#
# import functools
#
# newFunc = functools.partial(test, c=5)
# print(newFunc, type(newFunc))
#
# newFunc(1, 2)


# numStr = "100010"
# result = int(numStr, base=2)
# print(result)
#
# # 在往后的一段时间内, 我都需要把一个二进制的字符串, 转换成为对应的十进制数据
# import functools
# int2 = functools.partial(int, base=2)
# print(int2(numStr))



# 2. 高阶函数




# a, b 形参, 变量
# 传递数据, 就是指, 给变量赋值

# 函数本身, 也可以作为数据, 传递给另外一个变量
# def test(a, b):
#     print(a + b)
#
#
#
# print(test)
# print(id((test)))
#
# test2 = test
# test2(1, 2)

# l = [{"name": "sz", "age": 18}, {"name": "sz2", "age": 19}, {"name": "sz3", "age": 18.5}]
#
# def getKey(x):
#     return x["name"]
#
# result = sorted(l, key=getKey)
# print(result)


# def caculate(num1, num2, caculateFunc):
#     result = caculateFunc(num1, num2)
#     print(result)
#
#
# def sum(a, b):
#     return  a + b
#
# def jianfa(a, b):
#     return  a - b
#
# caculate(6, 2, jianfa)



# 返回函数




# def getFunc(flag):
#     # 1. 再次定义几个函数
#     def sum(a, b, c):
#         return a + b + c
#     def jian(a, b, c):
#         return a - b - c
#
#     # 2. 根据不同的flag值, 来返回不同的操作函数
#     if flag == "+":
#         return sum
#     elif flag == "-":
#         return jian
#
#
#
# result = getFunc("-")
# # print(result, type(result))
# res = result(1, 3, 5)
# print(res)



# 匿名函数


# result = (lambda x, y : x + y)(1, 2)
#
# print(result)
#
# newFunc = lambda x, y : x + y
# print(newFunc(4, 5))


#
# l = [{"name": "sz", "age": 18}, {"name": "sz2", "age": 19}, {"name": "sz3", "age": 18.5}]
#
# # def getKey(x):
# #     return x["name"]
#
# # result = sorted(l, key=getKey)
# result = sorted(l, key=lambda x: x["age"])
# print(result)


# 闭包


# def test():
#     a = 10
#     def test2():
#         print(a)
#
#     return test2
#
#
# newFunc = test()
# newFunc()



# print("---------------------123-------------------------")

# def line_config(content, length):
#
#     def line():
#         print("-"*(length // 2) + content + "-"*(length // 2))
#     return line
#
#
# line1 =  line_config("闭包", 40)
#
#
# line1()
# line1()
# line1()
# line1()
#
# line2 = line_config("xxxx", 80)
#
# line2()
# line2()
# line2()






# def test():
#     num = 10
#     def test2():
#         nonlocal num
#         num = 666
#         # print(a)
#         print(num)
#
#     print(num)
#     test2()
#     print(num)
#
#     return test2
#
#
#
# result = test()

# result()





# def test():
#     a = 1
#     def test2():
#         print(a)
#     a = 2
#
#     # a = 2
#
#     return test2
#
# newFunc = test()
#
# newFunc()

# 函数, 什么时候,才会确定, 内部, 变量标识, 对应的值
# 当函数被调用的时候, 才会真正的确定, 对应的值, 到底是什么, 之前,, 都是以普通的变量标识名称而存在
# def test():
#     print(b)
#
# print("xxxx")
# test()













# def test():
#     funcs = []
#     for i in range(1, 4):
#         def test2():
#             print(i)
#         funcs.append(test2)
#     return funcs
#
# newFuncs = test()
#
# print(newFuncs)
#
# newFuncs[0]()
# newFuncs[1]()
# newFuncs[2]()


#
# def test():
#     funcs = []
#     for i in range(1, 4):
#         def test2(num):
#             # num = 1
#             def inner():
#                 print(num)
#             return inner
#         funcs.append(test2(i))
#     return funcs
#
# newFuncs = test()
#
# print(newFuncs)
#
# newFuncs[0]()
# newFuncs[1]()
# newFuncs[2]()






































