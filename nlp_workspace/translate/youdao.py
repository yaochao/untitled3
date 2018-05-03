#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Created by yaochao at 2018/5/3


import requests
import hashlib
from urllib.parse import quote
import random

APP_KEY = '215128c625d9edc6'
SECRET_KEY = 'UbAIP8JXaPEQU2PtCrkmfZfET2tEa19N'
FROM = 'EN'
TO = 'zh-CHS'


def get_sign(q, salt):
    '''
    获得sign，签名，通过md5(appKey+q+salt+应用密钥)生成
    :return:
    '''
    s = APP_KEY + q + salt + SECRET_KEY
    m = hashlib.md5(s.encode()).hexdigest().upper()
    return m


def main(q):
    salt = str(random.randint(1, 65536))
    sign = get_sign(q, salt)

    rquest_url = 'https://openapi.youdao.com/api'
    response = requests.get(rquest_url, params={
        'q': quote(q.encode('utf-8')),
        'from': FROM,
        'to': TO,
        'appKey': APP_KEY,
        'salt': salt,
        'sign': sign})
    if response.status_code == 200:
        r = response.json()
        if r['errorCode'] == '0':
            translation = r['translation']
            if translation:
                print(translation[0])


if __name__ == '__main__':
    q = '''
    Alexa began a partnership with Google in early 2002, and with the web directory DMOZ in January 2003.[1] In December 2005, Alexa opened its extensive search index and Web-crawling facilities to third-party programs through a comprehensive set of Web services and APIs. These could be used, for instance, to construct vertical search engines that could run on Alexa's own servers or elsewhere. In May 2006, Google was replaced with Bing (at the time known as Windows Live Search) as a provider of search results.[11] In December 2006, Amazon released Alexa Image Search. Built in-house, it was the first major application built on the company's Web platform. In May 2007, Alexa changed their API to limit comparisons to three websites, reduce the size of embedded graphs in Flash, and add mandatory embedded BritePic advertisements.

In April 2007, the company filed a lawsuit, Alexa v. Hornbaker, to stop trademark infringement by the Statsaholic service.[12] In the lawsuit, Alexa alleged that Ron Hornbaker was stealing traffic graphs for profit, and that the primary purpose of his site was to display graphs that were generated by Alexa's servers.[13] Hornbaker removed the term Alexa from his service name on March 19, 2007.[14] On November 27, 2008, Amazon announced that Alexa Web Search was no longer accepting new customers, and that the service would be deprecated or discontinued for existing customers on January 26, 2009.[15] Thereafter, Alexa became a purely analytics-focused company.

On March 31, 2009, Alexa launched a major website redesign. The redesigned site provided new web traffic metrics—including average page views per individual user, bounce rate (the rate of users who come to, and then leave a webpage), and user time on website.[16] In the following weeks, Alexa added more features, including visitor demographics, clickstream and web search traffic statistics.[17] Alexa introduced these new features to compete with other web analytics services.
    '''
    main(q)
