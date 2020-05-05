# dict

# dict1 = {
#     '李宁': '一切皆有可能',
#     '耐克': 'just do it'
# }
# print(dict1)
# print({}.fromkeys((1, 2, 3), 'val'))  # fromkeys
# print(dict1.get('3'))  # get
# print(dict1.get('李宁'))
# print('李宁' in dict1)  # in

# # dict1.popitem() # 随机弹出一个
# dict1.pop('李宁') # 弹出一个
# print('删除之后',dict1)
# dict2=dict1.copy() # 浅拷贝
# dict1.clear()  # 清空


# for each in dict1.keys():
#   print(each)
# for each in dict1.values():
#   print(each)
# for each in dict1.items():
#   print(each)

# # update
# a = {1: 1, 2: 2}
# b = {3: 3}
# a.update(b)  # 用 b 扩展 a 
# print(a,b)

# # 集合 set
# set1={1,1,2,3,4,4,5,5}
# set1.add(6)
# set1.remove(6)
# print(set1)
# set2=set([1,2,3,3,4,4,5,6])
# print(set2)
# print(1 in set1) # in 

# # 不可变集合
# set3=frozenset([1,2,3,4,5])