# -*- coding: utf-8 -*-
import scrapy


class AbaikespiderSpider(scrapy.Spider):
    name = 'abaikespider'
    allowed_domains = ['www.a-hospital.com']
    start_urls = ['http://www.a-hospital.com/']

    def parse(self, response):
        print(response.text)
