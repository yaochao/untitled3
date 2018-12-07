#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by yaochao on 2017/8/17

from selenium import webdriver


options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=/Users/yaochao/test/chromedriverdir')
options.add_argument('--headless')
options.add_argument('--window-size=1920x1080')
options.add_argument('--blink-settings=imagesEnabled=true')
options.add_argument('--lang=zh_CN')
options.add_argument('--ignore-certificate-errors')
# options.add_argument('--user-agent="Mozilla/5.0 (iPod; U; CPU iPhone OS 2_1 like Mac OS X; ja-jp')

driver = webdriver.Chrome(options=options)
driver.get('http://www.baidu.com/')
page_source = driver.page_source
with open('test.html', 'w') as f:
    f.write(page_source)

driver.save_screenshot('screenshot2.png')


driver.quit()
