#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import datetime

# 是否打印返回结果
print_response = True

def getNowDateStr():
    return datetime.datetime.now().strftime("%Y-%m-%d_%H_%M_%S")
