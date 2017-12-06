#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Created by yaochao at 2017/10/23


import pytesseract
from PIL import Image
import requests

# code_url = 'https://www.wocloud.com.cn/webclient/wocloud/secucode'
# code_url = 'http://aidemo.youdao.com/images/demo/d_3.jpg'
# result = requests.get(code_url)
# with open('code.png', 'wb') as f:
#     f.write(result.content)

code = Image.open('/Users/yaochao/Desktop/hello.png')
code = code.convert("L")
code.save('code.png')

result = pytesseract.image_to_string(image=code, lang='chi_sim')
print(result)