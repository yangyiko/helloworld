

#显示导入
# from com.jiuyu.module import a
from com.jiuyu.module import a
print(a.num)

#系统path可以修改
import site
print("site.getsitepackages=",site.getsitepackages())

import sys
print("sys.path==",sys.path)
print("需要注意的是如果已经在sys.path的下级目录中导入了，就会存放到内存，下一次再也找不到了")
print("此时我们可以打印已经导入了什么py文件")

# for m in sys.modules:
#     print(m)
print("sys.modules=",sys.modules)


