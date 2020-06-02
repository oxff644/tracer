#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import sys
import django

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tracer.settings")
django.setup()  # os.environ['DJANGO_SETTINGS_MODULE']


from web import models
# 往数据库添加数据：链接数据库、操作、关闭链接
models.UserInfo.objects.create(username='0xff', email='afubread@163.com', mobile_phone='1222222228', password='123123')
