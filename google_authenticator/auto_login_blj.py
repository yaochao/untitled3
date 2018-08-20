#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# created by yaochao at 2018/8/20


import pyotp
import pexpect


def get_passwd():
    totp = pyotp.TOTP('xxx')
    passwd = 'xxx' + totp.now()
    return passwd


def main():
    child = pexpect.spawn('ssh xxx@xxx.xxx.xxx.xxx')
    child.expect('Passwd')
    child.sendline(get_passwd())
    child.interact()
    child.close()

if __name__ == '__main__':
    main()
