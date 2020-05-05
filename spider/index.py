# 爬取中美医学的课程名称
import requests
import os
res=requests.get('https://vedio.jiudingfanyi.com/w/course',{'page':1})
cate=res.json()['data']
str=''
for item in cate:
  str+=item['name']+'\n'+'-----------------'+'\n'
# f = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'zmyx-course.txt'),mode='a',encoding='utf-8')
f = open(os.path.join(os.path.dirname(__file__), 'zmyx-course.txt'),mode='a',encoding='utf-8')
f.write(str)
f.close()