#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by yaochao at 2018/3/20


from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hello world!")

def hello2(request):
    students = ['yaochao', 'dengqx', 'xusha', 'lln']
    context = {
        'students': students
    }
    return render(request, 'hello.html', context)