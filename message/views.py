# coding:utf-8
from django.shortcuts import render

# Create your views here.


def getform(request):
    return render(request, '留言板.html')
