from django.shortcuts import render, render_to_response, redirect
from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect
from User.models import *
from django.http import JsonResponse


# Create your views here.

def index(request):
    if request.session.get('username', None):
        return render(request, 'User/main.html')
    else:
        return render(request, 'User/sign_in.html')


# 登录
def sign_in(request):
    if request.method == "GET":
        return render(request, 'User/sign_in.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('inputPassword')
        # 查看用户是否存在
        user = User.objects.filter(username=username, password=password).first()
        if user:
            request.session['user_id'] = user.id
            request.session['username'] = user.username
            request.session.set_expiry(1000000)
            return HttpResponseRedirect('/index/')
        else:
            Log_Dict = {
                'username': username,
                'password': password,
                'login_err': "用户名或密码错误",
            }

            return render(request, 'User/sign_in.html', Log_Dict)


# 注册
def sign_up(request):
    if request.method == "GET":
        return render(request, 'User/sign_up.html')
    else:
        username = request.POST.get('username')
        phone = request.POST.get('Phone')
        password1 = request.POST.get('inputPassword')
        password2 = request.POST.get('inputPasswordConfirm')

        Reg_Dict = {
            'username': username,
            'phone': phone,
            'password1': password1,
            'password2': password2,
        }

        user1 = User.objects.filter(phone=phone)
        user2 = User.objects.filter(username=username)

        if user1:
            Reg_Dict['register_err'] = "手机号已被注册"
            return render(request, 'User/sign_up.html', Reg_Dict)
        elif user2:
            Reg_Dict['register_err'] = "用户名已存在"
            return render(request, 'User/sign_up.html', Reg_Dict)
        elif password1 != password2:
            Reg_Dict['register_err'] = "两次密码不匹配"
            return render(request, 'User/sign_up.html', Reg_Dict)
        else:
            User.objects.create(username=username, phone=phone, password=password1)
            return render(request, 'User/sign_in.html')


# 登出:清除所有缓存的session
def sign_out(request):
    request.session.clear()
    return HttpResponseRedirect('/User/sign_in/')
