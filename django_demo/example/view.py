#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Created by yaochao at 2018/3/20


from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView

def hello(request):
    return HttpResponse("Hello world!")

def hello2(request):
    students = ['yaochao', 'dengqx', 'xusha', 'lln']
    context = {
        'students': students
    }
    return render(request, 'hello.html', context)

class DiagnosisAPI(APIView):
    def get(self, request, *args, **kwargs):
        r = {
            'name': 'yaochao',
            'sex': 'male',
            'age': '28',
        }
        return JsonResponse(r)

    def post(self, request, *args, **kwargs):
        r = {
            'msg': 'success',
            'name': 'yaochao',
            'sex': 'male',
            'age': '28',
        }
        return JsonResponse(r)