#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# created by yaochao at 2018/8/9

from flask import Flask
import random
import time

app = Flask(__name__)

@app.route('/')
def hello():
    time.sleep(3)
    return 'Hello!'


if __name__ == '__main__':
    app.run(threaded=True)
