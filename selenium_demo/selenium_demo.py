#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Created by yaochao at 2018/2/9
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get('http://app1.sfda.gov.cn/datasearch/face3/base.jsp?tableId=25&tableName=TABLE25&title=%B9%FA%B2%FA%D2%A9%C6%B7&bcId=124356560303886909015737447882')
assert '国家食品药品' in driver.title
trs = driver.find_elements_by_xpath('//*[@id="content"]/div/table[2]/tbody/tr/td/p/a')
for tr in trs:
    print(tr.text)



print(trs)
time.sleep(3)
driver.close()
