# -*- coding: utf-8 -*-

import json
import smtplib
from email.mime.text import MIMEText
from constant import SMTP_HOST
from constant import SMTP_USER
from constant import SMTP_PWD
from constant import SMTP_PORT
from constant import RECEIVER
from constant import EMAIL_TITLE


def read_spider_result():

    with open('./spider_result.json', 'r', encoding='utf-8') as f:

        datas = f.readlines()
        # print(datas)

    # data_format = [json.loads(data) for data in datas]

    if not datas:
        return "没有符合条件的爬虫结果。"

    data_str = ''

    for data in datas:
        item = json.loads(data)
        # print(item)
        contents = item['title'] + '\t--->\t' + item['link'] + '\n'
        data_str += contents

    return data_str


def send_email(body):

    message = MIMEText(body, 'plain', 'utf-8')      # 邮件内容，格式，编码
    message['From'] = SMTP_USER                     # 发件人
    message['To'] = ', '.join(RECEIVER)             # 收件人列表
    message['Subject'] = EMAIL_TITLE                # 邮件标题
    try:
        # 实例化一个SMTP_SSL对象
        smtp_ssl_client = smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT)

        # 登录smtp服务器
        loginRes = smtp_ssl_client.login(SMTP_USER, SMTP_PWD)
        # loginRes = (235, b'Authentication successful')
        # print("登录结果：loginRes = {loginRes}")

        if loginRes and loginRes[0] == 235:
            print("登录成功，code = {loginRes[0]}")
            smtp_ssl_client.sendmail(SMTP_USER, RECEIVER, message.as_string())
            print("mail has been send successfully. message:{message.as_string()}")
        else:
            print("登陆失败，code = {loginRes[0]}")
    except Exception as e:
        print("发送失败，Exception: e={e}")

if __name__ == '__main__':
    c = read_spider_result()
    print(c)

    # body = "这是一个测试。\n 换行测试。\n http://www.zjzfcg.gov.cn/innerUsed_noticeDetails/index.html?noticeId=2350480"
    # title = "爬虫结果"
    send_email(c)

