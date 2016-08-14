# -*- coding: utf-8 -*-
from Demos.SendSimpleEmail.SendSimpleEmail import send_mail
import json

mail_server = "smtp.163.com"
# outlook change

def readConfig():
    with open('mailUsers.json') as data_file:
        return json.load(data_file)


def generateHtml():
    return "Amazon Web Services Billing Statement Available2"


if __name__ == '__main__':
    config = readConfig()

    for mail_to in config['mailto_list']:
        for mail_user in config["mail_users"]:
            if send_mail(mail_server, mail_user["name"], mail_user['pass'], [mail_to], "Amazon Web Services",
                         generateHtml()):
                print("发送成功")
            else:
                print("发送失败")
