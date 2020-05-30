# # 三元操作符
# w=1 if True else 2
# print(w)

# # 断言 assert 自动崩溃 AssertionError
# assert 3>4

# # for range
# for item in range(1,10,2):
#   print(item)

# 列表 list
# mix=[1,True,'str']
# mix.append('append')
# mix.extend([2,3])
# mix.insert(0,'first') #['first', 1, True, 'str', 'append', 2, 3]
# mix.remove('str')#需要提供元素
# del mix[0]
# mix.pop(0)
# print(mix[:])# 拷贝 切片
# print(mix) # ['first', True, 'append', 2, 3]
# list = [1, 2, 3, 4, 5]
# print(1 in list)
# print(list.count(3))  # 1
# print(list.index(3))  # 2
# list.reverse() # 翻转
# list.sort() # 参数 func   key   reverse
# print(list)

# 元组 tuple 不可改变
# tuple1=(1,2,3,4,5)
# tuple2=(3,)
# print(tuple1[3:])
# print(tuple2)


# str 方法

# str1='wutong'
# print(str1.capitalize()) # 首字母大写
# print(str1.casefold()) # 变为小写
# print(str1.center(20)) # 居中 两侧填充空格
# print(str1.count('w')) # 出现次数
# print(str1.endswith('g'))
# print(str1.startswith('w'))
# print(str1.find('w')) # 找不到返回 -1

# print(str1.index('w'))# 会产生异常
# print('-'.join('sumoli'))
# print('https://www.bilibili.com/video/BV1xs411Q799?p=15'.split('/'))
# print('{a},{b},{c}'.format(a=1,b='222',c=3))# format
# print('%c %c %c ' % (97,98,99))

# # len max
# l='123'
# l=list(l)
# print(l)
# print(max(l))
# print(min(l))
# nums=[1,2,3,4,5,6,7]
# print(sum(nums))
# print(sorted(nums))
# print(list(reversed(nums)))
# print(list(enumerate(nums)))
# print(list(zip([1,2],[3,4])))

# # 函数

# def func(m=0,n=2 ,*args):
#   '默认参数，关键字参数 收集参数'
#   print(args)
#   return m**n
# print(func.__doc__) # 函数文档
# print(func(2,2,3,4))

# # global
# count =5
# def func():
#   global count
#   count=10
# func()
# print(count)

# 内嵌函数和闭包

# 内嵌函数
# def func1():
#   print('func1')
#   def func2():
#     print('func2')
#   func2()
# func1()

# # 闭包
# def func():
#     count = 1

#     def func1():
#         nonlocal count
#         count += 1
#         return count
#     return func1
# f = func()
# print(f())
# print(f())

# # lambda 表达式
# p=lambda x:x**2
# print(p(5))

# filter
# l = filter(lambda x: x < 3, [1, 2, 3, 4, 5])
# print(list(l))
# print(list(filter(lambda x: x % 2==0, range(10))))
# print(1==True)

# 自己实现
# def m_filter(func=None,list=[]):
#   _list=[]
#   if(func!=None):
#     for item in list:
#       if(func(item)==True):
#         _list.append(item)
#   else:
#     _list=list
#   return _list
# l = m_filter(lambda x: x < 5, [1, 2, 3, 4, 5])
# print(list(l))

# map
# print(list(map(lambda item: item*2,[1,2,3,4,5])))

# 递归
# # 循环版本
# def func(n):
#   '求 n 的阶乘'
#   res=1
#   for each in range(1,n+1):
#     res*=each
#   return res
# # 递归版本
# def func(n):
#     '求 n 的阶乘'
#     if n == 1:
#         return 1
#     else:
#         return n*func(n-1)
# print(func(200))

# 斐波那契数列
# def fb(n):
#     '递归方式'
#     if n == 1or n == 2:
#         return 1
#     else:
#         return fb(n-1)+fb(n-2)
# def fb(n):
#     '迭代方式'
#     x = 1
#     y = 1
#     z = 0
#     print(list(range(n)))
#     for item in range(n):
#         x = y
#         y = z
#         z = x+y
#     return z
# print(fb(40))

# txt = '123\n\t456a'
# print(txt.replace('\n', '').replace('\r', ''))

