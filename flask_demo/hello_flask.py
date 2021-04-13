#!/usr/bin/env python
# -*- coding: utf-8 -*-
# created by yaochao at 2019/2/18


from flask import Flask
from flask import request, make_response
from flask_demo import generate_poster
from random import choice

app = Flask(__name__)


@app.route('/getHaiwangImg', methods=['POST'])
def hello():
    nickname = request.form['nickname']
    header = request.form['header']
    words = [{
        "desciption_img_path": "assets/顶级海王.png",
        "fish_nums": "10000",
        "rank": "顶级海王",
        "potential": "100%",
        "love_demand": "100%",
        "strength": "爆表",
        "time_management": "爆表",
    }, {
        "desciption_img_path": "assets/寡王继承人.png",
        "fish_nums": "-10000",
        "rank": "寡王继承人",
        "potential": "-11%",
        "love_demand": "39%",
        "strength": "0%",
        "time_management": "99%",
    }, {
        "desciption_img_path": "assets/不花心小塘主.png",
        "fish_nums": "1",
        "rank": "不花心小塘主",
        "potential": "100%",
        "love_demand": "50%",
        "strength": "100%",
        "time_management": "98%",
    }, {
        "desciption_img_path": "assets/最强寡王.png",
        "fish_nums": "-10000",
        "rank": "最强寡王",
        "potential": "-100%",
        "love_demand": "50%",
        "strength": "1%",
        "time_management": "99%",
    }, {
        "desciption_img_path": "assets/捕鱼达人.png",
        "fish_nums": "999999",
        "rank": "捕鱼达人",
        "potential": "1000%",
        "love_demand": "81%",
        "strength": "1001%",
        "time_management": "98%",
    }]

    # 随机选一个词组
    word = choice(words)

    byte_array = generate_poster(
        user_avatar_url=header,
        user_nickname=nickname,
        desciption_img_path=word["desciption_img_path"],
        fish_nums=word["fish_nums"],
        rank=word["rank"],
        potential=word["potential"],
        love_demand=word["love_demand"],
        strength=word['strength'],
        time_management=word['time_management']
    )
    response = make_response(byte_array, 200)
    response.mimetype = 'image/jpg'
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=False)
