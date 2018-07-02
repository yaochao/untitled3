#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by yaochao on 2017/9/3


# with open('sitemap_1_50000.xml', 'a') as f:
#     f.write('<?xml version="1.0" encoding="UTF-8"?>')
#     f.write('\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
#     for i in range(1, 50001):
#         a_site = '''
# <url>
#   <loc>https://www.jishux.com/plus/view-{}-1.html</loc>
#   <lastmod>2017-08-31</lastmod>
# </url>'''.format(str(i))
#         f.write(a_site)
#     f.write('\n</urlset>')
import pymysql


def gen_sitemap(total):
    file_count = int(total / 50000)
    for index in range(1, file_count + 1):
        with open('sitemap_' + str((index - 1) * 50000 + 1) + '_' + str(index * 50000) + '.xml', 'a') as f:
            f.write('<?xml version="1.0" encoding="UTF-8"?>')
            f.write('\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
            for i in range((index - 1) * 50000 + 1, index * 50000 + 1):
                a_site = '''
<url>
<loc>https://www.jishux.com/plus/view-{}-1.html</loc>
<lastmod>2018-03-27</lastmod>
</url>'''.format(str(i))
                f.write(a_site)
            f.write('\n</urlset>')


def gen_sitemap2():
    '''
    新版技术栈sitemap生成函数
    :return:
    '''
    MYSQL_CONFIG_SERVER = {
        'host': '47.93.232.8',
        'port': 3306,
        'user': 'root',
        'passwd': 'W$udzpgobz#4evVs',
        'db': 'jishux_server',
        'charset': 'utf8',
        'cursorclass': pymysql.cursors.DictCursor,
    }
    connect = pymysql.connect(**MYSQL_CONFIG_SERVER)
    cursor = connect.cursor()
    sql = 'SELECT arc_id FROM jishux_article_info'
    sql2 = 'SELECT COUNT(1) cnt FROM jishux_article_info'
    cursor.execute(sql2)
    result = cursor.fetchone()
    cnt = result['cnt']
    print(cnt)
    cursor.execute(sql)
    result = cursor.fetchall()
    for i in range(int(cnt / 50000) + 1):
        start = i * 50000
        end = (i + 1) * 50000
        if end > cnt:
            end = cnt
        arc_id_50000 = result[start:end]
        write_to_xml(start, end, arc_id_50000)


def write_to_xml(start, end, arc_id_50000):
    with open('sitemap_' + str(start) + '_' + str(end) + '.xml', 'a') as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        for arc_id in arc_id_50000:
            a_site = '<url>\n<loc>https://www.jishux.com/p/{}</loc>\n<lastmod>2018-07-02</lastmod>\n</url>\n'.format(arc_id['arc_id'])
            f.write(a_site)
        f.write('</urlset>\n')


if __name__ == '__main__':
    # gen_sitemap(750000)
    gen_sitemap2()
