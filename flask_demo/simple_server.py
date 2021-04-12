#!/usr/bin/env python
# -*- coding: utf-8 -*-
# created by yaochao at 2019/2/18


from flask import Flask
from flask import request, make_response
import requests

app = Flask(__name__)


@app.route('/post_sms.do', methods=['POST'])
def hello():
    sms_url = 'http://sms.devops.ksyun.com:8901/post_sms.do'
    headers = {
        'content-type': request.content_type,
    }
    response = requests.post(sms_url, request.form.to_dict(), headers=headers)
    rsp = make_response(response.content, response.status_code)
    return rsp


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
