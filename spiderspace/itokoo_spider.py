#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# created by yaochao at 2018/8/5


from requests_html import HTMLSession
import pymysql

MYSQL_CONF = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'passwd': 'toor',
    'db': 'yaochao',
    'charset': 'utf8',
    'cursorclass': pymysql.cursors.DictCursor,
}


class ItokooSpider:
    def __init__(self):
        self.connect = pymysql.connect(**MYSQL_CONF)
        self.cursor = self.connect.cursor()

    def get_html(self, url):
        '''
        获取html
        :param url: 请求的url
        :return: html对象
        '''
        session = HTMLSession(mock_browser=True)
        response = session.get(url)
        return response.html

    def parse(self, html):
        baidupan = html.xpath("//a[text()='百度网盘']")
        if baidupan:
            baidupan = baidupan[0]
            print(dir(baidupan))
            download_url = baidupan.links.pop()
            download_passwd = html.xpath('//*[@id="read_tpc"]/text()')[1]
            download_title = html.xpath('//*[@id="subject_tpc"]/text()')[0]
            thumbs = html.xpath('//*[@class="f12"]//img/@src')
            item = {
                'download_url': download_url,
                'download_passwd': download_passwd,
                'download_title': download_title,
                'thumbs': thumbs
            }
            return item

    def pipeline(self, item):
        sql = 'INSERT INTO itokoo (baidupan_url, baidupan_passwd, title) values (%s,%s,%s)'
        self.cursor.execute(sql, (item['download_url'], item['download_passwd'], item['download_title']))
        sql2 = 'SELECT LAST_INSERT_ID() lastid'
        self.cursor.execute(sql2)
        itokoo_id = self.cursor.fetchone()['lastid']
        sql3 = 'INSERT INTO itokoo_dxzb (itokoo_id, thumb_url) values (%s,%s)'
        for i in item['thumbs']:
            self.cursor.execute(sql3, (itokoo_id, i))
        self.connect.commit()

    def __del__(self):
        self.cursor.close()
        self.connect.close()


def main():
    itokoospider = ItokooSpider()

    itokoospider.get_html('http://www.itokoo.com/thread.php?fid=108').xpath('')


if __name__ == '__main__':
    main()
