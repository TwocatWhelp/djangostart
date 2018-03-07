# coding:utf-8
from django.shortcuts import render

from .models import UserMessage

# Create your views here.


def getform(request):
    # 查询
    message = None
    all_message = UserMessage.objects.filter(name='bobbytest')
    if all_message:
        message = all_message[0]


    # if request.method == 'POST':
    #     name = request.POST.get('name', '')
    #     message = request.POST.get('message', '')
    #     address = request.POST.get('address', '')
    #     email = request.POST.get('email', '')
    #
    #     # 保存数据
    #     user_message = UserMessage()
    #     user_message.name = name
    #     user_message.message = message
    #     user_message.address = address
    #     user_message.email = email
    #     user_message.object_id = 'helloworld3'
    #
    #     user_message.save()

    return render(request, '留言板.html', {
        'my_message': message
    })
