#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Created by yaochao at 2017/10/19


# Install the Python Requests library:
# `pip install requests`

import requests


def send_request():
    # Request
    # POST http://old.med.wanfangdata.com.cn/Mesh/Index.aspx

    try:
        response = requests.post(
            url="http://old.med.wanfangdata.com.cn/Mesh/Index.aspx",
            headers={
                "Origin": "http://old.med.wanfangdata.com.cn",
                "Cookie": ".ASPXANONYMOUS=JZTSYad-0wEkAAAAYzQ3MzE4M2ItMDJmNy00NTZiLWEzNjgtYjkwOGRlMTM3OGJjMUfO4flLX74YvYGp4lVm2Bojgkc1; ASP.NET_SessionId=cv0lyw1i0fevwquzrn5maqec; MeshPrivilge=1; Hm_lvt_af200f4e2bd61323503aebc2689d62cb=1508333661,1508336266,1508336388,1508396419; Hm_lpvt_af200f4e2bd61323503aebc2689d62cb=1508398013; WFMed.Auth=%7b%22Context%22%3a%7b%22AccountIds%22%3a%5b%22MedPerson.xray887%22%5d%2c%22Data%22%3a%5b%7b%22Key%22%3a%22MedPerson.xray887.DisplayName%22%2c%22Value%22%3a%22%22%7d%5d%2c%22SessionId%22%3a%2253bc4c34-2308-439d-9bdf-11d882e47d24%22%2c%22Sign%22%3a%22EzmUz%2b%5c%2fnRvvkasvCOmTztB4TAWpywqJhKFWbjs%2bIDOmHZxDqVUjlpGYYYvq9QNYy%22%7d%2c%22LastUpdate%22%3a%222017-10-19T08%3a17%3a33Z%22%2c%22TicketSign%22%3a%22RN1rDFJHbW61KVF0ikZrTg%3d%3d%22%7d",
                "Content-Type": "text/plain; charset=UTF-8",
                "Referer": "http://old.med.wanfangdata.com.cn/Mesh/Index.aspx",
                "Host": "old.med.wanfangdata.com.cn",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
                "X-AjaxPro-Method": "GetMesh",
            },
            data="{\"initial\":\"A\"}"
        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')


send_request()