#!/usr/bin/env python
# -*- coding: utf-8 -*-
# created by yaochao at 2019/7/26


import socket
from threading import Thread


def HTTPServer(port: int):
    server_socket = socket.socket()
    server_socket.bind(('127.0.0.1', port))
    server_socket.listen(10)  # 表示可以使用10个监听

    def method(client_socket: socket):
        try:
            # 接受客户端发来的字节
            data = client_socket.recv(1024)
            data = data.decode('utf-8')
            # 拿到URI
            uri = data.split('\r\n')[0].split(' ')[1]
            # 先把URI?后面的去掉，参数暂未处理
            uri = uri.split('?')[0]
            if uri == '/':
                uri += 'index.html'
            print(addr[0] + ' Request: ' + uri)
            with open('moban' + uri, 'rb') as f:
                content = f.read()
            # 向客户端发送字节
            client_socket.send(b'HTTP/1.1 200 OK\r\n')
            client_socket.send(('Content-Type: ' + get_mime(uri) + '\r\n').encode('utf-8'))
            client_socket.send(b'\r\n')
            client_socket.send(content)
            # 释放资源
            client_socket.close()
        except Exception as e:
            print(e)

    while True:
        client_socket, addr = server_socket.accept()
        Thread(target=method, args=(client_socket,)).start()


def get_mime(filepath: str) -> str:
    mime = "text/html; charset=utf-8"
    if filepath.endswith(".css"):
        mime = "text/css; charset=utf-8"
    elif filepath.endswith(".jpg") or filepath.endswith(".jpeg"):
        mime = "image/jpeg"
    elif filepath.endswith(".js"):
        mime = "text/javascript"
    elif filepath.endswith(".woff2"):
        mime = "font/woff2"
    return mime


if __name__ == '__main__':
    HTTPServer(8888)
