import pickle
import os
# my_list=[1,'2',True,'wutong',[1,2]]
# f=open(os.path.join(os.path.dirname(__file__),'list.pkl') ,mode='wb')
# pickle.dump(my_list,f)
# f.close()

# 读取
f=open(os.path.join(os.path.dirname(__file__),'list.pkl') ,mode='rb')
list=pickle.load(f)
print(list,type(list))
f.close()