#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
pip3 install requests
"""
import requests

res = requests.get('https://s25-15131255089-1585271608-1251317460.cos.ap-chengdu.myqcloud.com/1585286041171_12.png')

print(res.content)
