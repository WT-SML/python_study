from django.shortcuts import render, HttpResponse, redirect
from app01 import models
# Create your views here.


def handleIndex(req):
    # models.User.objects
    # models.User.objects.filter()
    # models.User.objects.get()
    # obj={'username':'wutong','password':'123456'}
    # models.User.objects.save(obj)
    print(models.User.objects.all())
    # return HttpResponse(models.User.objects.all())
    # return HttpResponse([{'a':1},{'b':2}])
    return render(req, 'mikutap/Mikutap.html')
