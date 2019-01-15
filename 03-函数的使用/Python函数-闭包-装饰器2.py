
def checkLogin(func):
    def inner():
        print("登录验证...")
        func()
    return inner

# 定义两个功能函数
@checkLogin
def fss():
    print("发说说")

# fss = checkLogin(fss)

# fss = def inner():
#         print("登录验证...")
#         fss()
#
# print(fss)

# 语法糖 写法
@checkLogin
def ftp():
    print("发图片")
# ftp = checkLogin(ftp)



# 相关的逻辑代码
btnIndex = 1
if btnIndex == 1:
    fss()
else:
    ftp()


# 发说说, 发图片, 必须有一个前提, 就是, 用户必须登录之后,
# 登录验证的操作

# 1. 直接在业务逻辑代码里面去修改, 添加一个验证操作
#   因为业务逻辑代码非常多, 所以, 就造成了, 每一份, 逻辑代码, 在调用, 具体的功能函数之前, 都需要, 去做一个登录验证, 代码冗余度, 就比较大, 代码的复用性比较差, 代码的维护性比较差


# 2, 直接在功能函数里面, 去修改, 方便代码的重用





















