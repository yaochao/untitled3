#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Created by yaochao at 2017/12/18


a = 1
b = '1'
c = [1, 2, 3]
d = {'1': 1}
print(a, b, c, d)

for i in c:
    print(i)

while a < 10:
    print(a)
    a += 1

def hello():
    print('hello')

class Hello(object):
    def __init__(self, name):
        self.name = name

    def say(self):
        print('my name is ' + self.name)

if __name__ == '__main__':
    hello = Hello(name='sb')
    hello.say()
