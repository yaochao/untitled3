#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Created by yaochao at 2018/5/4


from setuptools import setup


setup(
    name="img_to_txt",
    version="0.0.1",
    author="yaochao",
    author_email="yaochao365@qq.com",
    description="Any image transfer to txt",
    license="MIT",
    url="https://github.com/yaochao/img_to_txt",
    install_requires=['certifi','chardet','idna','numpy', 'Pillow', 'requests'],
    scripts="img_to_txt.py",
    py_modules=['urllib3'],
)