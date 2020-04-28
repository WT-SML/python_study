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



















