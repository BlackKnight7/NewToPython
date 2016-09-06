# -*- coding: utf-8 -*-
from Demos.SendSimpleEmail.SimulateSendEmailByHand import send_mail
import json
import time
import urllib2
import random
from bs4 import BeautifulSoup

mail_server = "smtp-mail.outlook.com"

urls = ['http://www.chinadaily.com.cn/',
        'http://www.cbsnews.com/',
        'http://www.nbcnews.com/',
        'http://www.foxnews.com/',
        'http://www.huffingtonpost.com/'
        ]


# outlook change

def readConfig():
    with open('mailUsers.json') as data_file:
        return json.load(data_file)


def generateContent():
    try:
        url = random.choice(urls)
        response = urllib2.urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html, "html.parser")
        text = ''
        for pSingle in soup.find_all('p'):
            if len(text) < 100:
                text += pSingle.get_text()
        return text
    except:
        print("生成内容失败， 重新生成")
        return generateContent()


if __name__ == '__main__':
    config = readConfig()

    for mail_to in config['mailto_list']:
        for mail_user in config["mail_users"]:
            for i in range(0, 10):
                html_text = generateContent()
                title = "Top Stories %s" % i
                if send_mail(mail_server, mail_user["name"], mail_user['pass'], mail_to, title, html_text):
                    print("发送成功")
                    time.sleep(2)
                else:
                    print("发送失败")

    print ('完成')
