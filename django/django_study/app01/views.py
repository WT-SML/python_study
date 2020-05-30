from django.shortcuts import render, HttpResponse, redirect
from app01 import models
import requests
# Create your views here.


def handleIndex(req):
    # models.User.objects
    # models.User.objects.filter()
    # models.User.objects.get()
    # obj={'username':'wutong','password':'123456'}
    # models.User.objects.save(obj)
    # print(models.User.objects.all())
    # return HttpResponse(models.User.objects.all())
    url = 'https://zh.moegirl.org/%E5%B7%A5%E4%BD%9C%E7%BB%86%E8%83%9E:%E8%A1%80%E5%B0%8F%E6%9D%BF'
    res = requests.get(url)
    res.encoding = 'utf=8'
    html = res.text.replace('href="/', 'href="https://zh.moegirl.org/')
    html = html.replace('src="/', 'src="https://zh.moegirl.org/')
    return HttpResponse(html)
