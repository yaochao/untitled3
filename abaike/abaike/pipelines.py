# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

mysql_config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'db': 'abaike',
    'charset': 'utf8',
    'cursorclass': 'pymysql.cursors.DictCursor',
}


class AbaikePipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(**mysql_config)
        self.cursor = self.conn.cursor()
        self.count = 0

    def process_item(self, item, spider):
        sql = "INSERT INTO item (word, text, url) VALUES (%s, %s, %s)"
        self.cursor.execute(sql, item)
        self.conn.commit()
        # if self.count >= 100:
        #     self.conn.commit()
        #     self.count = 0
        return item

    def __del__(self):
        self.cursor.close()
        self.conn.close()
