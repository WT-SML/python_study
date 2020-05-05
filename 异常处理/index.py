import os
_dir = os.path.join(os.path.dirname(__file__),'w.txt')
print(_dir)
# AssertionError -> 断言失败
try:
  raise BaseException # 自己引发异常
  f = open('w.txt')
  print(f.read())
  c.close()
except OSError as err:
  print('文件出错啦', '错误地原因是'+str(err))
except BaseException:
  print('BaseException')
finally:
  print('无论如何都会执行我')