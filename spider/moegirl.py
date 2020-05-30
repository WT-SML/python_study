import requests
import os

# url = 'https://zh.moegirl.org/%E7%82%AE%E5%A7%90'
url = 'https://zh.moegirl.org/%E5%B7%A5%E4%BD%9C%E7%BB%86%E8%83%9E:%E8%A1%80%E5%B0%8F%E6%9D%BF'
filepath = os.path.join(os.path.dirname(__file__), 'ret/moegirl.html')
res = requests.get(url)
res.encoding = 'utf=8'
html = res.text.replace('href="/', 'href="https://zh.moegirl.org/')
html = html.replace('src="/', 'src="https://zh.moegirl.org/')
f = open(filepath, mode='w', encoding='utf-8')
f.write(html)
f.close()
