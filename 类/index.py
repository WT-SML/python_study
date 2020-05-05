# class
class W():
  name=''
  def __init__(self,name='wutong'):
    self.name=name
  def getName(self):
    return self.name
  def run(self):
    print(self.name+'正在跑步')

# 继承 多个父类可实现多重继承
class S(W):
  pass
w=W()
s=S('sumoli')
w.run()
s.run()
# 组合 横向组合 self.x=W()

