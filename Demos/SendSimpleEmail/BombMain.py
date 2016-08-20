# -*- coding: utf-8 -*-
from Demos.SendSimpleEmail.SendSimpleEmail import send_mail
import json
import time
import urllib2
import random
from bs4 import BeautifulSoup

mail_server = "smtp-mail.outlook.com"

urls = ['http://news.sohu.com/',
        'http://news.qq.com/',
        'http://news.163.com/',
        'http://news.ifeng.com/',
        'http://www.xinhuanet.com/',
        'http://www.people.com.cn/',
        'http://www.chinanews.com/',
        'http://news.cctv.com/',
        'http://www.huanqiu.com/',
        'http://news.baidu.com/']


# outlook change

def readConfig():
    with open('mailUsers.json') as data_file:
        return json.load(data_file)


def generateContent():
    url = random.choice(urls)
    response = urllib2.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, "html.parser")
    text = ''
    for pSingle in soup.find_all('p'):
        text += pSingle.get_text()
    return text


if __name__ == '__main__':
    config = readConfig()

    for mail_to in config['mailto_list']:
        for mail_user in config["mail_users"]:
            for i in range(0, 10):
                html_text = generateContent()
                title = "Top Stories %s" % i
                if send_mail(mail_server, mail_user["name"], mail_user['pass'], mail_to, title, html_text):
                    print("发送成功")
                    time.sleep(20)
                else:
                    print("发送失败")

    print ('完成')
