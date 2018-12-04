#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# created by yaochao at 2018/10/19


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# created by yaochao at 2018/10/19

import requests
import logging
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

logger = logging.getLogger(__name__)


# image包可以发送图片形式的附件
# from email.mime.image import MIMEImage

# 可以查询文件对应的'Content-Type'
import mimetypes

mail_config = {
    'smtpserver': 'smtp.hichina.com',
    'smtpport': 465,
    'password': 'fuckU1314',
    'sender': 'admin@jishux.com',
    'receiver': ['yaochao365@qq.com'],
}

def sendmail(subject='', message='请及时查收，谢谢。', file_path=None):
    now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    sender = mail_config['sender']
    receiver = mail_config['receiver']
    smtpserver = mail_config['smtpserver']
    smtpport = mail_config['smtpport']
    password = mail_config['password']
    subject = '[每日签到]' + subject + ' - ' + now_time
    # 下面的to\cc\from最好写上，不然只在sendmail中，可以发送成功，但看不到发件人、收件人信息
    msgroot = MIMEMultipart('related')
    msgroot['Subject'] = subject
    msgroot['From'] = sender
    msgroot['To'] = ','.join(receiver)

    # MIMEText有三个参数，第一个对应文本内容，第二个对应文本的格式，第三个对应文本编码
    message = MIMEText('{}\n    {}\n    {}'.format(message, '本邮件由系统自动发送', now_time), 'plain', 'utf-8')
    msgroot.attach(message)

    if file_path:
        content_type = mimetypes.guess_type(file_path)
        # 读取xlsx文件作为附件，open()要带参数'rb'，使文件变成二进制格式,从而使'base64'编码产生作用，否则附件打开乱码
        att = MIMEText(open(file_path, 'rb').read(), 'base64', 'utf-8')
        att['Content-Type'] = content_type[0]
        # 下面的filename 等号(=)后面好像不能有空格
        attname = 'attachment; filename ="{}"'.format(file_path.split('/')[-1])
        att['Content-Disposition'] = attname
        msgroot.attach(att)

    # 阿里云邮箱的smtp服务器
    s = smtplib.SMTP_SSL(smtpserver, smtpport)
    s.connect(smtpserver)
    s.login(sender, password)

    # # 发送给多人、同时抄送给多人，发送人和抄送人放在同一个列表中
    s.sendmail(sender, receiver, msgroot.as_string())
    s.quit()





def send_request():
    # IT之家每日签到
    # GET https://my.ruanmei.com/api/usersign/sign

    try:
        response = requests.get(
            url="https://my.ruanmei.com/api/usersign/sign",
            params={
                "userhash": "0641b31cd590b5c53277fb7108bd0ae9a17a59ef86e08ead13ebcbebeef99df7f477ba862df682ba65919c2d3ab56f14",
                "type": "0",
                "appver": "632",
            },
            headers={
                "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 7.1.2; Redmi 5 Plus MIUI/8.10.11)",
                "Host": "my.ruanmei.com",
                "Cookie": "BEC=603d5f9c85f4ed8628aeb6dd0c7d2c9f|1539916536|1539916536",
            },
        )
        if response.status_code == 200:
            result = response.json()
            return result

    except requests.exceptions.RequestException as e:
        logger.error('签到失败', e)


def main():
    result = send_request()
    if result:
        if result['ok'] == 1:
            sendmail('IT之家' + result['title'], message='签到奖励:' + result['message']['签到奖励'])
        else:
            sendmail('IT之家签到失败', message=result['msg'])


if __name__ == '__main__':
    main()
