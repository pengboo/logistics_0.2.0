# coding=utf-8
from django.db import models


# Create your models here.
class UserInfo(models.Model):
    uname = models.CharField('用户名', max_length=20)
    upwd = models.CharField('密码', max_length=40)
    uphone = models.CharField('手机号码', max_length=11)
    udepartment = models.CharField('部门', max_length=20, default='')
