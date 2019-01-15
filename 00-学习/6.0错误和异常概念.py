from _csv import Error
#-------------------------------自定义异常---------------------------
print("------------------自定义异常-------------------------")
class BusinessException(Exception):
    def __init__(self,errorCode,errorMes=""):
        self.__errorCode = errorCode
        self.__errorMes = errorMes
    def __str__(self):
        return "errorCode="+str(self.__errorCode)+",errorMes="+str(self.__errorMes)

try:
    raise BusinessException("0001")
except Exception as ze:
    print("自定义异常BusinessException=",ze)
#-------------------------------异常 捕获---------------------------
print("------------------异常 捕获-------------------------")
try:
    1/0
except Exception as ze:
    print("Exception",ze)
finally:
    print("异常被处理完毕")
#----------------------------------------------------------
print("------------------捕获-------------------------")
try:
    f = open("xx.jpg", "r")
    f.readlines()
except Exception as e:
    print("这里应用用rb来读取===",e)
finally:
    print("文件--异常处理完毕")
    f.close()


# class Test:
#     def __enter__(self):
#         print("enter")
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print(self, exc_type, exc_val, exc_tb)
#         import traceback
#         print(traceback.extract_tb(exc_tb))
#         print("exit")
#         return True
#
# with Test() as x:
#     # print("body", x)
#     1 / 0


import contextlib


class Test:
    def t(self):
        print("tttttt")

    def close(self):
        print("资源释放")

    # def __enter__(self):
    #     return self
    #
    # def __exit__(self, exc_type, exc_val, exc_tb):
    #     self.close()
# import contextlib
# with contextlib.closing(Test()) as t_obj:
#     t_obj.t()


# with open("xx.jpg", "rb") as from_file:
#     with open("xx2.jpg", "wb") as to_file:
#         from_contents = from_file.read()
#         to_file.write(from_contents)
# with open("xx.jpg", "rb") as from_file, open("xx2.jpg", "wb") as to_file:
#     from_contents = from_file.read()
#     to_file.write(from_contents)
# import contextlib
# with contextlib.nested(open("xx.jpg", "rb"), open("xx2.jpg", "wb")) as (from_file, to_file):
#     from_contents = from_file.read()
#     to_file.write(from_contents)

class LessZero(Exception):
    def __init__(self, msg, error_code):
        self.msg = msg
        self.ec = error_code

    def __str__(self):
        return self.msg + str(self.ec)
    pass


def set_age(age):
    if age <=0 or age > 200:
        # print("值错误")
        raise LessZero("小于零, 错误", 404)
    else:
        print("给张三的年龄设置为", age)


try:
    set_age(-18)
except LessZero as e:
    print("x", e)



















