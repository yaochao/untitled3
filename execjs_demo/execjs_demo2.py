#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Created by yaochao at 2018/2/28

import execjs


def get_js(jsfile):
    with open(jsfile, encoding='utf-8') as f:
        js = f.read()
        return js


def exec_my_js(jsfile, func_str, *params):
    js = get_js(jsfile)
    ctx = execjs.compile(js)
    r = ctx.call(func_str, *params)
    return r

def get_links(links):
    jsfile = '/Users/yaochao/test/movie.js'
    diff = exec_my_js(jsfile, 'hello', links)
    return diff


def __main():
    # links = '{"ct":"3sYyqU8ge+AXzZTq2g2nvHlAfOqH52hiKG310Tm3Wz3nClXwi7wKs/Y3ncdpJ6SbQl0tk7a6rD/iymJ9A+ipux99CIr9unGA55Jf9pBkPjSrDqyqbUHzX2cui0NSVN8qP7Hw2dtR5ZyfhiTcgM4mTfAksFqiyWtlwMiRFQTyy35AMmoU8KQlaTSIR7tCS+pq33ug/I1QwQdhlLmgdF7Qf+eocpRrQePQA/DzivnmPyFI0ZkCHT2fOtZxeS2VAepHqRruGsX9qphUSXRkc6AeOOlEjTKJvZ5cqw9MPhkoskhEV593i8n379oT80PDrRL2tAQuQw7GNB7rqyWyOT5unx/B6F+uI+ZTgOgDqUWuTpSQxzB3p+abvTFQDvcWihHWoc3MUxiyefibYGPYRgIgjQ==","iv":"8d062c7789e1f709ae9aa8005b6f73a7","s":"028c0b9a431693aa"}'
    links = '{"ct":"NL78yG8ewsRrRRGToB4/kSfS/Qp4VSezcig/Poc2oP98oKecpG/elybzJrsXZ4g8UDBGtTYmTRBIpZSdK10LpILdxtR1jXJK7qY+VMtfsWk=","iv":"25718331b38dcbf7de8ff63428e8d135","s":"52b331d74b0eea33"}'
    links = get_links(links=links)
    print(links)


if __name__ == '__main__':
    __main()
