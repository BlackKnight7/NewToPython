# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText

def send_mail(mail_server, mail_user, mail_pass, to_list, sub, content):
    me = "wangyi_news_7" + "<" + mail_user + ">"
    msg = MIMEText(content, _subtype='html', _charset='gb2312')  # 创建一个实例，这里设置为html格式邮件
    msg['Subject'] = sub  # 设置主题
    msg['From'] = me
    msg['To'] = ";".join(to_list)

    try:
        s = smtplib.SMTP()
        s.connect(mail_server)  # 连接smtp服务器
        s.set_debuglevel(1)
        s.login(mail_user, mail_pass)  # 登陆服务器
        s.sendmail(me, to_list, msg.as_string())  # 发送邮件
        s.close()
        return True
    except Exception as e:
        print(str(e))
        return False


