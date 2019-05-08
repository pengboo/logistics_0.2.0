from django.shortcuts import render, redirect
from .models import UserInfo
from hashlib import sha1

# Create your views here.
def register(request):
    return render(request, 'l_user/register.html')


def register_handle(request):
    post = request.POST
    uname = post.get('user_name')
    upwd = post.get('pwd')
    upwd2 = post.get('cpwd')
    uphone = post.get('phone')

    # 判断两次密码
    if upwd != upwd2:
        return redirect('/user/register')

    # 密码加密
    # s1=sha1()
    # s1.update(upwd)
    # upwd3=s1.hexdigest()

    # 创建对象
    user = UserInfo()
    user.uname = uname
    user.upwd = upwd
    user.uphone = uphone
    user.save()
    # 注册成功，转到登录页面
    return redirect('/user/login')
