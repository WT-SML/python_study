import os
f=open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'w.text'),mode='a',encoding='utf-8')
f.write('wutong')
# print(f.read(8))
# print(f.tell())
f.close()