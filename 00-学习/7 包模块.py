#--------------上下文3-------------------
import contextlib
@contextlib.contextmanager
def ze():
    try:
        print("1 进入到ze()的上下文之中")
        yield
    except Exception as e:
        print("3 有一个Exception异常",e)
    finally:
        print("4 ze 的上下文执行完毕")

with ze() as ze2:
    print("2 打印1/0====",1/0)
#--------------上下文1-------------------
class withcontent:
    def __enter__(self):
        print("withcontent_enter方法")
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("withcontent_exit方法",exc_type, exc_val, exc_tb)
        import traceback
        print("traceback方法",traceback.extract_tb(exc_tb))
        print("exit")
        return True
    
with withcontent() as w:
    print("withcontent_body方法")
    1/0
#--------------上下文2-------------------
@contextlib.contextmanager
def withcontent2():
    print(1)
    yield
    print(3)
    
with withcontent2() as w2:
    print(2,w2)
    
