#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by yaochao on 2017/8/17

from selenium import webdriver

phantomjs_path = '/usr/local/bin/phantomjs'
driver = webdriver.PhantomJS(executable_path=phantomjs_path)
driver.get('http://36kr.com/')
page_source = driver.page_source.encode('utf8')
print(type(page_source))
with open('test.html', 'wb') as f:
    f.write(page_source)
driver.close()