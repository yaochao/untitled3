#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Created by yaochao at 2018/5/25
import csv

from requests_html import HTMLSession


def get_game(page):
    session = HTMLSession()
    try:
        response = session.post(
            url="http://182.131.21.139/gspt/ccm-action/domesticgame/searchGame",
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                "Origin": "http://182.131.21.139",
                "Cache-Control": "max-age=0",
                "Content-Type": "application/x-www-form-urlencoded",
                "Referer": "http://182.131.21.139/gspt/ccm-action/domesticgame/searchGame",
                "Host": "182.131.21.139",
                "Upgrade-Insecure-Requests": "1",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36",
                "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7",
                "Cookie": "JSESSIONID=9AE58B68949207A8141146212D0960F6.jvm6411",
            },
            data={
                "business_id": "052011",
                "game_name": "",
                "page": str(page),
            },
        )
        return response
    except Exception as e:
        print(e)


def main():
    # total page 85
    games = []
    for i in range(85):
        r = get_game(i + 1)
        pzwh = r.html.xpath('//*[@id="bawh"]/text()')
        yxmc = r.html.xpath('//*[@id="yxmc"]/text()')
        yydw = r.html.xpath('//*[@id="yydw"]/text()')
        pwrq = r.html.xpath('//*[@id="pwrq"]/text()')
        for i in range(len(yxmc)):
            game = []
            if i != 0:
                game.append(pzwh[i])
                game.append(yxmc[i])
                game.append(yydw[i])
                game.append(pwrq[i])
                games.append(game)

    # write to the xls
    with open('games.csv', 'w', encoding='utf-8') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(('批准文号','游戏名称', '运营单位', '批文日期'))
        f_csv.writerows(games)


if __name__ == '__main__':
    main()
