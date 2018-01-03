# -*- coding: utf-8 -*-
import scrapy
from ..misc.utils import get_text
from urllib.parse import unquote, urljoin


class AbaikespiderSpider(scrapy.Spider):
    name = 'abaike'
    allowed_domains = ['www.a-hospital.com']
    start_urls = ['http://www.a-hospital.com/w/%E7%94%B5%E5%AD%90%E6%98%BE%E5%BE%AE%E9%95%9C']
    custom_settings = {
        'ITEM_PIPELINES': {
            'abaike.pipelines.AbaikePipeline': 300,
        },
    }

    def parse(self, response):
        url = response.url
        word = url.split('/w/')[1]
        text = get_text(response.text)
        yield {
            'url': url,
            'word': unquote(word),
            'text': text
        }
        # 其他的词语
        urls = response.xpath('//a[starts-with(@href, "/w/")]/@href').extract()
        urls = [urljoin('http://www.a-hospital.com/', url) for url in urls]
        print(urls)
        for url in urls:
            if '#' in url:
                continue
            request = scrapy.Request(url, callback=self.parse)
            yield request
