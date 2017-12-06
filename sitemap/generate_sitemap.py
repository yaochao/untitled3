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


def gen_sitemap(total):
    file_count = int(total / 50000)
    for index in range(1, file_count + 1):
        with open('sitemap_' + str((index - 1) * 50000 + 1) + '_' + str(index * 50000) + '.xml', 'a') as f:
            f.write('<?xml version="1.0" encoding="UTF-8"?>')
            f.write('\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
            for i in range((index - 1) * 50000 + 1, index * 50000 + 1):
                a_site = '''
<url>
<loc>http://www.jishux.com/plus/view-{}-1.html</loc>
<lastmod>2017-08-31</lastmod>
</url>'''.format(str(i))
                f.write(a_site)
            f.write('\n</urlset>')

if __name__ == '__main__':
    gen_sitemap(653727)
