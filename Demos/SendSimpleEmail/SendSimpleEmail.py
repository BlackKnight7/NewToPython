# -*- coding: utf-8 -*-
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

def send_mail(mail_server, mail_user, mail_pass, mail_to, subject, content):
    msg = MIMEMultipart()
    msg['From'] = mail_user
    msg['To'] = mail_to
    msg['Subject'] = subject
    msg.attach(MIMEText(content))

    try:
        mailServer = smtplib.SMTP(mail_server, 587)
        mailServer.ehlo()
        mailServer.starttls()
        mailServer.ehlo()
        # mailServer.set_debuglevel(1)
        mailServer.login(mail_user, mail_pass)
        mailServer.sendmail(mail_user, mail_to, msg.as_string())
        mailServer.close()

        return True
    except Exception as e:
        print(str(e))
        return False