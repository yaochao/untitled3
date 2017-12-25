#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Created by yaochao at 2017/12/25


import tkinter as tk

window = tk.Tk()
window.title('hello')
window.geometry('400x200')

# 这里是窗口内容
# Label
s = tk.StringVar()
l = tk.Label(window,
             textvariable=s,  # 文字
             bg='green',  # 背景
             # font=('Arial', 12), # 字体和大小
             width=30, height=2  # label宽高
             )
l.pack()  # 固定窗口位置

# Button
is_hit = False


def hit_me():
    global is_hit
    if not is_hit:
        is_hit = True
        s.set('恭喜您获得一个"大傻逼"称号！')
        s2.set('点击关闭')
    else:
        is_hit = False
        s.set('')
        s2.set('点击打开')

s2 = tk.StringVar(value='点击打开')
b = tk.Button(window,
              textvariable=s2,
              width=15, height=2,
              command=hit_me
              )
b.pack() # 固定到窗口上

window.mainloop()
