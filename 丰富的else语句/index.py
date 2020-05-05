# while...else 语法 for...else 语法
# 当 while/for 循环正常执行完的情况下，执行 else 输出；
# 如果当 while/for 循环中执行了跳出循环的语句，比如 break，将不执行 else 代码块的内容；

# 异常
# try:
#   print(int('abc'))
# except ValueError as reason:
#   print('出错啦'+reason)
# else:
#   print('没有异常')

# with 关闭文件
# import os
# with open(os.path.realpath(__file__),'r',encoding='utf=8') as f:
#   print(f.read())