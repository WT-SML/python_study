# import requests
# res=requests.get('https://vedio.jiudingfanyi.com/w/course',{'page':1})
# cate=res.json()['data']
# str=''
# for item in cate:
#   str+=item['name']+'\n'+'-----------------'+'\n'
# f = open('course.text',mode='a',encoding='utf-8')
# f.write(str)
# f.close()