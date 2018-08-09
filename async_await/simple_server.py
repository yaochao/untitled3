#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# created by yaochao at 2018/8/9

from flask import Flask
import random
import time

app = Flask(__name__)

@app.route('/')
def hello():
    rand = random.randint(1, 10)
    print('randint: ', rand)
    time.sleep(rand)
    return 'Hello!'


if __name__ == '__main__':
    app.run(threaded=True)
