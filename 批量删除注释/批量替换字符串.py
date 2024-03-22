#!/usr/bin/env python
# -*- coding: utf-8 -*-
# created by yaochao at 2021/6/10


import os
import re

base_folder = '/Users/yaochao/java/masheng/servers/cclient-server'


def all_file(folder: str) -> list:
    files = []
    for dirpath, dirnames, filenames in os.walk(folder):
        for filename in filenames:
            ff = os.path.join(dirpath, filename)
            files.append(ff)
    return files


def all_folder() -> list:
    folders = []
    for dirpath, dirnames, filenames in os.walk(base_folder):
        for dirname in dirnames:
            sub_folder = os.path.join(dirpath, dirname)
            folders.append(sub_folder)
    return folders


def removeComment(fp: str = None):
    """
    删除文件中的注释
    """
    with open(fp, mode='r') as f:
        origin_content = f.read()

    new_content = re.sub(r'com.infoxmed.appserver', 'com.infoxmed.cclientserver', origin_content)

    with open(fp, mode='w') as f:
        f.write(new_content)


def main():
    all_files = []
    folders: list = all_folder()
    for sub_folder in folders:
        files = all_file(sub_folder)
        all_files.extend(files)
    for fp in all_files:
        if fp.endswith(".java"):
            print(fp)
            removeComment(fp)


if __name__ == '__main__':
    main()
